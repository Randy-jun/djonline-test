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
  </el-container>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Asider from '@/components/Asider.vue'
import Main from '@/components/Main.vue'

export default {
  name: 'home',
  components: {
    Header,
    Asider,
    Main,
  }
}
</script>
<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0px;
  }
}
.login-box {
  margin-top:15%;
  margin-left:40%;
}
.el-header {
  background-color: rgb(91, 202, 156);
  line-height: 60px;
}
.el-aside, el-menu {
  background-color: rgb(214, 252, 236);
}
.el-main {
  background-color: rgb(214, 252, 236);
  height: 948px;
}
</style>