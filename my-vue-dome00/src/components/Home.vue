<template>
  <el-container>
      <el-header>
        <Header msg="Financial Management Systems Software" />
      </el-header>
    <el-container>
      <el-aside>
        <Asider msg="This is Asider!" />
      </el-aside>
      <el-main>
        <Main msg="This is Main!"/>
      </el-main>
    </el-container>
      <el-footer>
        <Footer msg="This is Footer!" />
      </el-footer>
  </el-container>
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

<style scoped>
#home{
  height: 100vh;
  /* width: 100%; */
}
/* .el-header{
  margin-top: 20px;
  margin-bottom: 20px;
} */
/* #app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
} */
</style>