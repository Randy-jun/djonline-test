<template>
<div class="col-2 ">
  <nav class="nav nav-pills nav-fill flex-column">
    <a class="nav-item nav-link active" v-on:click="navgo('groups')">组团社管理</a>
    <a class="nav-item nav-link" v-on:click="navgo('products')">线路报价管理</a>
  </nav>
</div>
</template>

<script>
export default {
  name: 'Asiderset',
  data() {
    return {
        menu_name: "MENU",
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
