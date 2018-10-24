<template>
    <p>{{ footer }}</p>
</template>

<script>
export default {
  name: 'Footerset',
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