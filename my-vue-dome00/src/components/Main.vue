<template>
  <div class="container-fluid">
    <Header msg="Financial Management Systems Software" />
      <div class="row">
        <Asider msg="This is Asider!" />
        <Home msg="This is Home!"/>
      </div>
      <Footer msg="This is Footer!" />
  </div>
</template>

<script>

import Header from './Header.vue'
import Asider from './Asider.vue'
import Home from './Home.vue'
import Footer from './Footer.vue'

export default {
  name: 'app',
  data() {
    return {
      msg: "login!",
    }
  },
  components: {
    Header,
    Asider,
    Home,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>