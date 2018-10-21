<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-3 col-offset-1 login">
        <el-input type="text" placeholder="用户名" suffix-icon="el-icon-edit" v-model="username"></el-input>
        <small>{{username}}</small>
        <el-input type="password" placeholder="密码" suffix-icon="el-icon-edit" v-model="password"></el-input>
        <small>{{password}}</small>
        <div v-show="show_S" class="alert alert-success" role="alert">
          登录成功!
        </div>
        <div v-show="show_F" class="alert alert-danger" role="alert">
          登录失败!
        </div>
        <div class="row">
          <el-button type="success" v-on:click="login($event)">登录</el-button>
          <el-button type="primary" v-on:click="reg()">注册</el-button>
        </div>
      </div>
  </div>
  </div>
</template>

<script>
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
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
          if(response.data.isLogin){
            console.log(response);
            this.show_F=false;
            this.show_S=true;
            Sstorage.set('nickName', response.data.NickName);
            Sstorage.set('userID', response.data.userID);
            
            Sstorage.set('localName', response.data.DJName);
            Sstorage.set('localAgencyFk', response.data.local_agency_fk);
            
            Sstorage.set('tokenID', response.data.tokenID);
            //  console.log(response);
            setTimeout(()=>{
              this.$router.replace({ path: 'main' })
            },1000)
            // var int=self.setInterval(this.$router.replace({ path: 'main' }),1000);
          }else{
            console.log(response);
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