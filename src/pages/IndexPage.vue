<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    />
    <q-btn label="select a directory" @click="openDirectory" />
    <span id="directoryPath"></span>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'IndexPage',
  setup() {
    async function openDirectory() {
      if (process.env.MODE === 'electron') {
        const directoryPath = await window.electronAPI.dialogOpenDirectory()
        console.log(directoryPath)
        document.getElementById('directoryPath').innerHTML = directoryPath
      }
    }
    return { openDirectory }
  },
})
</script>
