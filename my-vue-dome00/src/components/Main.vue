<template>
<router-view/>
  <!-- <HomeList msg="This is Home!"/> -->
  <!-- <HomeDetails msg="This is Home!"/> -->
</template>

<script>
import Records from './home/Records.vue'
import AddRecord from './home/AddRecord.vue'
import Accounts from './home/Accounts.vue'

export default {
  data() {
    return {
      msg: "Main!",
    }
  },
  components: {
    Records,
    AddRecord,
    Accounts,
  }
}
</script>

<style>

</style>