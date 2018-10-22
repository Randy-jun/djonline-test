<template>
  <div class="col">
    <MainList msg="This is MainList!"/>

  </div>
</template>

<script>

import MainList from './MainList.vue'
import MainDetails from './MainDetails.vue'

export default {
  data() {
    return {
      msg: "Testing!",
    }
  },
  components: {
    MainList,
    MainDetails,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>