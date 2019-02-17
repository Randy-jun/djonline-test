<template>
  <el-row>
    <el-col :span=20>
      <h1>DJonline</h1>
    </el-col>
    <el-col :span=4>
      <small>{{nickname}} | {{group}} | <a class="badge badge-second el-icon-setting" v-on:click="logout()">退出</a></small>
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