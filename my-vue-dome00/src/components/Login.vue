<template>
  <div class="row">
    <div class="col-3 col-offset-1 login">
      <form>
        <div class="form-group">
          <label for="InputUsername">User name</label>
          <input type="texts" class="form-control" v-model='username' id="InputUsername" placeholder="User name">
          <small>{{username}}</small>
        </div>
        <div class="form-group">
          <label for="InputPassword">Password</label>
          <input type="password" class="form-control" v-model='password' id="InputPassword" placeholder="Password" v-on:keyup.enter="login($event)">
          <small>{{password}}</small>
        </div>
        <div class="row">
          <div class="col"><button type="button" class="btn btn-success" v-on:click="login($event)">登录</button></div>
          <div class="col"><button type="button" class="btn btn-primary" v-on:click="reg()">注册</button></div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';
export default {
  name: 'Login',
  props: {
    msg: String
  },
  data() {
    return {
      username:'',
      password:'',
      // post_data:{},
      test_list:[],
      tourist:[]
    }
  },
  methods: {
    login(e){
      // console.log(e)
      const api='http://127.0.0.1:9090/login/';
      if (e.type == 'click' || e.keyCode == 13) {
        // console.log(this.username,this.password);
        var params = new URLSearchParams();
        params.append("username",this.username);
        params.append("password",this.password); 
        Axios.post(api, params)
          .then(function (response) {
            alert(response.data.result);
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
            
          });
      }
    },
    reg(flag){
      
    }
  },
  mounted() {
    // var list = JSON.parse(localStorage.getItem('list'));
      
    // var api="http://127.0.0.1:9090/acct/request_form/6";
    var api='http://127.0.0.1:9090/acct/return_json/';
    // var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=2';
    Axios.get(api).then((response)=>{
        // console.log(response);
        // console.log(typeof(response.data.result));
        this.test_list=response.data.result;
      }).catch((error)=>{
        // console.log(error);
      })
  }
}
</script>

<style scoped>
.login{
  background-image: 'https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG/skin_zoom/5.jpg?2';
  margin-top: 25rem;
  margin-left: auto;
  margin-right: auto;
}
</style>