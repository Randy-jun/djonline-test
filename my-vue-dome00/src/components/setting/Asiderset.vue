<template>
  <el-menu class="el-menu-vertical" default-active="1">
    <el-menu-item index="1" v-on:click="navgo('')">
      <i class="el-icon-menu"></i>
      <span slot="title" >管理首页</span>
    </el-menu-item>
    <el-menu-item index="2" v-on:click="navgo('groups')">
      <i class="el-icon-menu"></i>
      <span slot="title">组团社管理</span>
    </el-menu-item>
    <el-menu-item index="3" v-on:click="navgo('products')">
      <i class="el-icon-menu"></i>
      <span slot="title">线路报价管理</span>
    </el-menu-item>
  </el-menu>
<!-- <div class="col-2 ">
  <nav class="nav nav-pills nav-fill flex-column">
    <a class="nav-item nav-link active" v-on:click="navgo('')">管理首页</a>
    <a class="nav-item nav-link" v-on:click="navgo('groups')">组团社管理</a>
    <a class="nav-item nav-link" v-on:click="navgo('products')">线路报价管理</a>
  </nav>
</div> -->
</template>

<script>
export default {
  name: 'Asiderset',
  data() {
    return {
    }
  },
  props: {
    msg: String,
  },
  methods: {
    navgo(addgo){
      var goadd = "/setting/" + addgo
      // console.log(goadd)
      this.$router.replace({ path: goadd })
    },
  },
  mounted() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
