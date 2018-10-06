<template>
  <nav class="navbar navbar-light bg-light">
    <span class="navbar-brand"><h1>DJonline</h1></span>
      <div class="col-auto">
      <small>{{nickname}} | {{djname}} | <a class="badge badge-second" v-on:click="setting()">设置</a></small>
      </div>
  </nav>
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
    this.nickname = Sstorage.get('nickname')
    this.djname = Sstorage.get('localname');
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