<template>
  <div>
  <el-row :gutter=20 v-for="m in 3" :key="m">
    <el-col :span=6 v-for="n in 4" :key="n">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span><h4>应用 {{m}}-{{n}}</h4></span>
          <!-- <el-button style="float: right; padding: 3px 0" type="text">X</el-button> -->
        </div>
        <div class="el-icon-message">
          <span></span>
          <!-- <i class="el-icon-message"></i>           -->
        </div>
      </el-card>
    </el-col>
  </el-row>
</div>
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
  }
}
</script>

<style>

</style>