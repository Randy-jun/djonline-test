<template>
  <div class="jumbotron text-center" style="margin-bottom:0">
    <p class="text-monospace">{{ footer }}</p>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
        footer:"Powered by Vue.js and Bootstrap!",
    }
  },
  props: {
    msg: String
  }
}
</script>

<style scoped>
</style>