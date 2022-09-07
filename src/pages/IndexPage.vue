<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    />
    <img id="image" />
    <span id="t"></span>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { io } from 'socket.io-client'

export default defineComponent({
  name: 'IndexPage',
  setup() {
    const socket = io('http://localhost:3000')
    socket.on('connect', () => {
      console.log('connected')
    })
    socket.on('disconnect', () => {
      console.log('disconnected')
    })
    socket.on('message', (data) => {
      console.log(data)
    })
    socket.on('image_server2client', (data) => {
      const image = document.getElementById('image')
      image.src = `data:image/jpeg;base64,${data}`
    })
    socket.on('t_server2client', (data) => {
      const t = document.getElementById('t')
      t.textContent = data
    })
  },
})
</script>
