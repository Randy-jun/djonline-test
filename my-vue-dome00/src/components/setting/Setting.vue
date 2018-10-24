<template>
  <el-container>
    <el-header>
      <Headerset msg="Financial Management Systems Software Headerset" />
    </el-header>
    <el-container>
      <el-aside>
        <Asiderset msg="This is Asiderset!" />
      </el-aside>
      <el-main>
        <Mainset msg="This is Mainset!"/>
      </el-main>
    </el-container>
    <el-footer>
      <Footerset msg="This is Footerset!" />
    </el-footer>
  </el-container>
</template>

<script>

import Headerset from './Headerset.vue'
import Asiderset from './Asiderset.vue'
import Mainset from './Mainset.vue'
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
    Mainset,
    Footerset,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>