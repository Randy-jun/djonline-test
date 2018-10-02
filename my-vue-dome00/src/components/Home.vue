<template>
  <div class="col">
    <HomeList msg="This is Home!"/>
    <!-- <HomeDetails msg="This is Home!"/> -->
  </div>
</template>

<script>

import HomeList from './HomeList.vue'
import HomeDetails from './HomeDetails.vue'

export default {
  data() {
    return {
      msg: "Testing!",
    }
  },
  components: {
    HomeList,
    HomeDetails,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>