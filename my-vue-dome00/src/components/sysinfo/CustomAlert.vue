<template>
<div class="col">
  <!-- <div class="alert" v-bind:class='alertmsg.stateFlag' role="alert">{{alertmsg.msgConten}}</div>
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button> -->
  <div class="alert alert-dismissible fade show" v-bind:class='alertmsg.stateFlag' role="alert">
    {{alertmsg.msgConten}}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</div>
</template>

<script>
import Sstorage from '@/module/sstorage.js';
export default {
  name: 'CustomAlert',
  props: [
    'alertmsg',
  ],
  data() {
    return {
    }
  },
  methods: {

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