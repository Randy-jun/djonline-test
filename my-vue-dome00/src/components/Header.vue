<template>
  <div class="container-fluid">
    <div class="row justify-content-end">
       <div class="col-auto">
       {{nickname}} | {{djname}} | 设置
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-auto">
        <h1>DJ Online</h1>
      </div>
    </div>
  </div>
</template>

<script>
import Sstorage from '../module/sstorage.js';
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
  mounted() {
    this.nickname = Sstorage.get('nickname')
    this.djname = Sstorage.get('djname');
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