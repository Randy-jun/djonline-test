<template>
  <div class="container-fluid">
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
          <template>

          </template>
          <div v-show="show_S" class="alert alert-success" role="alert">
            登录成功!
          </div>
          <div v-show="show_F" class="alert alert-danger" role="alert">
            登录失败!
          </div>
          <div class="row">
            <div class="col"><button type="button" class="btn btn-success" v-on:click="login($event)">登录</button></div>
            <div class="col"><button type="button" class="btn btn-primary" v-on:click="reg()">注册</button></div>
          </div>
        </form>
      </div>
  </div>
  </div>
</template>

<script>
import Axios from 'axios';
import Sstorage from '../module/sstorage.js';
export default {
  name: 'Login',
  props: {
    msg: String
  },
  data() {
    return {
      username:'',
      password:'',
      show_S:false,
      show_F:false,
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
        Axios.post(api, params).then((response)=>{
          if(response.data.is_login){
            this.show_F=false;
            this.show_S=true;
            Sstorage.set('nickname', response.data.NickName);
            Sstorage.set('djname', response.data.DJName);
            //  console.log(response);
            setTimeout(()=>{
              this.$router.replace({ path: 'main' })
            },1000)
            // var int=self.setInterval(this.$router.replace({ path: 'main' }),1000);
            // console.log(response.data.is_login);
            // console.log(response.data.login_result_string)
            // console.log(response.data.NickName)
            // console.log(response.data.DJName)
          }else{
            // alert("登录失败");
            this.show_S=false;
            this.show_F=true;
          }
        })
        .catch((error)=>{
          console.log(error);
        });
      }
    },
    reg(){
    }
  },
  mounted() {
  },
}
</script>

<style scoped>
.login{
  margin: 20rem auto auto auto;
}
</style>