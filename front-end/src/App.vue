<template>
  <div id="app">
    <!-- <Login msg="Welcome to Your Vue.js App"/> -->
    <router-view/>
  </div>
</template>

<script>
// import Login from './views/Login.vue'

export default {
  name: 'app',
  components: {
    // Login
  }
}
</script>

<style>
*{
margin: 0;
padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
