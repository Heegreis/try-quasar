<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    />
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
  },
})
</script>
