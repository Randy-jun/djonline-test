<template>
  <el-row>
    <el-col :span=19>
      <h1>DJonline</h1>
    </el-col>
    <el-col :span=1>
      <small>{{nickname}}</small>
    </el-col>
    <el-col :span=2>
      <small :title=group>{{group}}</small>
    </el-col>
    <el-col :span=1>
      <small><a class="badge badge-second el-icon-setting" v-on:click="passwordChange()">修改密码</a></small>
    </el-col>
    <el-col :span=1>
      <small><a class="badge badge-second el-icon-setting" v-on:click="logout()">退出</a></small>
    </el-col>
  </el-row>
</template>

<script>
import Sstorage from '@/module/sstorage.js';
export default {
  name: 'Header',
  props: {
    msg: String
  },
  data() {
    return {
      nickname:'',
      group:'',
    }
  },
  methods: {
    passwordChange(){
      
    },
    logout(){
      // alert("setting")
      Sstorage.clearAll();
      this.$router.replace({ path: '/login' })
    },
  },
  mounted() {
    this.nickname = Sstorage.get('nickName');
    this.group = Sstorage.get('group');
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>