<template>
  <div>
    <el-header>
      <Header msg="Financial Management Systems Software" />
    </el-header>
    <el-aside>
      <Asider msg="This is Asider!" />
    </el-aside>
    <el-main>
      <Main msg="This is Main!"/>
    </el-main>
    <el-footer>
      <Footer msg="This is Footer!" />
    </el-footer>
  </div>
</template>

<script>

import Header from './Header.vue'
import Asider from './Asider.vue'
import Main from './Main.vue'
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
    Main,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>