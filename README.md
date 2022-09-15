# try-quasar

## The create env

OS: windows 11

```bash
$ node -v
v14.17.1

$ yarn -v
1.22.4

$ yarn global list
yarn global v1.22.4
info "@quasar/cli@1.3.2" has binaries:
   - quasar
...
```

## The create config

```bash
$ yarn create quasar
√ What would you like to build? » App with Quasar CLI, let's go!
√ Project folder: ... try-quasar
√ Pick Quasar version: » Quasar v2 (Vue 3 | latest and greatest)
√ Pick script type: » Javascript
√ Pick Quasar App CLI variant: » Quasar App CLI with Webpack (stable)
√ Package name: ... try-quasar
√ Project product name: (must start with letter if building mobile apps) ... Quasar App
√ Project description: ... A Quasar Project
√ Author: ... Heegreis <run3113214@gmail.com>
√ Pick your CSS preprocessor: » Sass with SCSS syntax
√ Check the features needed for your project: » ESLint, State Management (Pinia), Axios, Vue-i18n
√ Pick an ESLint preset: » Prettier
√ Install project dependencies? (recommended) » Yes, use yarn
```

<details>
<summary>Complete log</summary>

```bash
$ yarn create quasar
yarn create v1.22.4
[1/4] Resolving packages...
[2/4] Fetching packages...
info fsevents@1.2.9: The platform "win32" is incompatible with this module.
info "fsevents@1.2.9" is an optional dependency and failed compatibility check. Excluding it from installation.
info fsevents@2.1.2: The platform "win32" is incompatible with this module.
info "fsevents@2.1.2" is an optional dependency and failed compatibility check. Excluding it from installation.
[3/4] Linking dependencies...
[4/4] Building fresh packages...

success Installed "create-quasar@1.0.17" with binaries:
      - create-quasar


 .d88888b.
d88P" "Y88b
888     888
888     888 888  888  8888b.  .d8888b   8888b.  888d888
888     888 888  888     "88b 88K          "88b 888P"
888 Y8b 888 888  888 .d888888 "Y8888b. .d888888 888
Y88b.Y8b88P Y88b 888 888  888      X88 888  888 888
 "Y888888"   "Y88888 "Y888888  88888P' "Y888888 888
       Y8b

√ What would you like to build? » App with Quasar CLI, let's go!
√ Project folder: ... try-quasar
√ Pick Quasar version: » Quasar v2 (Vue 3 | latest and greatest)
√ Pick script type: » Javascript
√ Pick Quasar App CLI variant: » Quasar App CLI with Webpack (stable)
√ Package name: ... try-quasar
√ Project product name: (must start with letter if building mobile apps) ... Quasar App
√ Project description: ... A Quasar Project
√ Author: ... Heegreis <run3113214@gmail.com>
√ Pick your CSS preprocessor: » Sass with SCSS syntax
√ Check the features needed for your project: » ESLint, State Management (Pinia), Axios, Vue-i18n
√ Pick an ESLint preset: » Prettier

 Quasar • Generating files...

 - babel.config.js
 - quasar.config.js
 - README.md
 - .editorconfig
 - .gitignore
 - .postcssrc.js
 - jsconfig.json
 - package.json
 - public/favicon.ico
 - src/App.vue
 - src/index.template.html
 - .vscode/extensions.json
 - .vscode/settings.json
 - public/icons/favicon-128x128.png
 - public/icons/favicon-16x16.png
 - public/icons/favicon-32x32.png
 - public/icons/favicon-96x96.png
 - src/assets/quasar-logo-vertical.svg
 - src/boot/.gitkeep
 - src/components/EssentialLink.vue
 - src/layouts/MainLayout.vue
 - src/pages/ErrorNotFound.vue
 - src/pages/IndexPage.vue
 - src/router/index.js
 - src/router/routes.js
 - src/css/app.scss
 - src/css/quasar.variables.scss
 - src/boot/axios.js
 - src/boot/i18n.js
 - src/i18n/index.js
 - src/i18n/en-US/index.js
 - .eslintignore
 - .eslintrc.js
 - src/stores/example-store.js
 - src/stores/index.js
 - src/stores/store-flag.d.ts

 Quasar •  SUCCESS  • The project has been scaffolded

√ Install project dependencies? (recommended) » Yes, use yarn

yarn install v1.22.4
info No lockfile found.
[1/5] Validating package.json...
[2/5] Resolving packages...
[3/5] Fetching packages...
info fsevents@2.3.2: The platform "win32" is incompatible with this module.
info "fsevents@2.3.2" is an optional dependency and failed compatibility check. Excluding it from installation.
[4/5] Linking dependencies...
warning " > @babel/eslint-parser@7.17.0" has unmet peer dependency "@babel/core@>=7.11.0".
warning " > eslint-webpack-plugin@3.1.1" has unmet peer dependency "webpack@^5.0.0".
[5/5] Building fresh packages...
success Saved lockfile.
Done in 49.17s.


yarn run v1.22.4
$ eslint --ext .js,.vue ./ --fix
Done in 1.84s.


To get started:

  cd try-quasar
  quasar dev # or: yarn quasar dev # or: npx quasar dev

Documentation can be found at: https://v2.quasar.dev

Quasar is relying on donations to evolve. We'd be very grateful if you can
read our manifest on "Why donations are important": https://v2.quasar.dev/why-donate
Donation campaign: https://donate.quasar.dev
Any amount is very welcomed.
If invoices are required, please first contact Razvan Stoenescu.

Please give us a star on Github if you appreciate our work:
  https://github.com/quasarframework/quasar

Enjoy! - Quasar Team

Done in 244.87s.
```

</details>

## Install the dependencies

```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

### Lint the files

```bash
yarn lint
# or
npm run lint
```

### Format the files

```bash
yarn format
# or
npm run format
```

### Build the app for production

```bash
quasar build
```

### Customize the configuration

See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).

## Usage

### Build Electron and Python backend .exe

```bash
quasar build -m electron
```

```bash
pyinstaller server.spec
```
