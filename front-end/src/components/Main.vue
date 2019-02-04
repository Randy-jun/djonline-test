<template>
  <router-view/>
  <!-- <HomeList msg="This is Home!"/> -->
  <!-- <HomeDetails msg="This is Home!"/> -->
</template>

<script>
import MainHome from '@/components/MainHome.vue'

export default {
  data() {
    return {
      msg: "Main!",
    }
  },
  components: {
    MainHome,
  }
}
</script>

<style>

</style>