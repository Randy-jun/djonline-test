<template>
  <div class="container-fluid">
    <Headerset msg="Financial Management Systems Software Headerset" />
      <div class="row">
        <Asiderset msg="This is Asiderset!" />
        <Homeset msg="This is Homeset!"/>
      </div>
      <Footerset msg="This is Footerset!" />
  </div>
</template>

<script>

import Headerset from './Headerset.vue'
import Asiderset from './Asiderset.vue'
import Homeset from './Homeset.vue'
import Footerset from './Footerset.vue'

export default {
  name: 'app',
  data() {
    return {
      msg: "login!",
    }
  },
  components: {
    Headerset,
    Asiderset,
    Homeset,
    Footerset,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>