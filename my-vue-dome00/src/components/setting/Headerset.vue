<template>
  <el-row>
    <el-row>
      <el-col :span=20>
        <h1>DJonline</h1>
      </el-col>
      <el-col :span=4>
        <small>{{nickname}} | {{djname}} | <a class="el-icon-back" v-on:click="goback()">返回</a></small>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
import Sstorage from '@/module/sstorage.js';
export default {
  name: 'Headerset',
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
    goback(){
      this.$router.replace({ path: '/home' })
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
.hp{
    padding-top: 30px;
    padding-bottom: 18px;
}
</style>