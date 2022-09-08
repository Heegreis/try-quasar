import { app, BrowserWindow, nativeTheme, dialog } from 'electron'
import path from 'path'
import os from 'os'
import { spawn } from 'child_process'

// needed in case process is undefined under Linux
const platform = process.platform || os.platform()

try {
  if (platform === 'win32' && nativeTheme.shouldUseDarkColors === true) {
    require('fs').unlinkSync(
      path.join(app.getPath('userData'), 'DevTools Extensions')
    )
  }
} catch (_) {}

let mainWindow
let pythonBackgroundProcess

function createWindow() {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    icon: path.resolve(__dirname, 'icons/icon.png'), // tray icon
    width: 1000,
    height: 600,
    useContentSize: true,
    webPreferences: {
      contextIsolation: true,
      // More info: /quasar-cli/developing-electron-apps/electron-preload-script
      preload: path.resolve(__dirname, process.env.QUASAR_ELECTRON_PRELOAD),
    },
  })

  mainWindow.loadURL(process.env.APP_URL)

  let pythonScriptPath
  let pythonCommand
  if (process.env.DEBUGGING) {
    // if on DEV or Production with debug enabled
    mainWindow.webContents.openDevTools()

    pythonScriptPath = path.resolve(__dirname, '../src-python', 'server.py')
    console.log('pythonScriptPath', pythonScriptPath)
    pythonCommand = 'python ' + pythonScriptPath
    pythonBackgroundProcess = spawn('python', [pythonScriptPath])
  } else {
    // we're on production; no access to devtools pls
    mainWindow.webContents.on('devtools-opened', () => {
      mainWindow.webContents.closeDevTools()
    })

    pythonScriptPath = path.resolve(
      __dirname,
      '../../../../../dist/server/server.exe'
    )
    pythonCommand = pythonScriptPath
    pythonBackgroundProcess = spawn(pythonCommand)
  }

  mainWindow.on('closed', () => {
    mainWindow = null
  })

  pythonBackgroundProcess.stdout.on('data', (data) => {
    console.log(data.toString())
  })

  pythonBackgroundProcess.stderr.on('data', (data) => {
    console.log(data.toString())
    dialog.showErrorBox('Python Error', data.toString())
  })

  pythonBackgroundProcess.on('exit', (code) => {
    console.log(`Python process exited with code ${code}`)
  })
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})
