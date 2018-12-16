<template>
<router-view/>
  <!-- <HomeList msg="This is Home!"/> -->
  <!-- <HomeDetails msg="This is Home!"/> -->
</template>

<script>
import Records from './home/Records.vue'
import Accounts from './home/Accounts.vue'

export default {
  data() {
    return {
      msg: "Main!",
    }
  },
  components: {
    Records,
    Accounts,
  }
}
</script>

<style>

</style>