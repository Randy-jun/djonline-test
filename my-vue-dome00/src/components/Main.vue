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

</style>