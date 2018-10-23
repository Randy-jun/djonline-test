<template>
  <el-row>
    <el-row type="flex" align="bottom" justify="center">
      <el-col :span=20>
        <h1>DJonline</h1>
      </el-col>
      <el-col :span=4>
        {{nickname}} | {{djname}} | <a class="badge badge-second" v-on:click="setting()">设置</a>
      </el-col>
    </el-row>
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
      djname:'',
    }
  },
  methods: {
    setting(){
      // alert("setting")
      this.$router.replace({ path: 'setting' })
    },
  },
  mounted() {
    this.nickname = Sstorage.get('nickName')
    this.djname = Sstorage.get('localName');
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>