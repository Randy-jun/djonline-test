<template>
  <div class="col">
    <router-view/>
    <!-- <HomeList msg="This is Home!"/> -->
    <!-- <HomeDetails msg="This is Home!"/> -->
  </div>
</template>

<script>

import Groups from './Groups.vue'
import Products from './Products.vue'

export default {
  data() {
    return {
      msg: "Testing!",
    }
  },
  components: {
    Groups,
    Products,
  }
}
</script>

<style>
#app {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
</style>