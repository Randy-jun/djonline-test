<template>
  <el-container>
    <el-header>
      <h1>Financial Management Systems Software</h1>
    </el-header>
    <el-main>
      <el-row id="loginInputs" type="flex" justify="space-around">
        <el-col :span="4">
          <el-input type="text" placeholder="用户名" suffix-icon="el-icon-edit" v-model="username"></el-input>
          <small>{{username}}</small>
          <el-input type="password" placeholder="密码" suffix-icon="el-icon-edit" v-model="password"></el-input>
          <small>{{password}}</small>
          <el-row :gutter="20">
            <el-button type="success" v-on:click="login($event)">登录</el-button>
            <el-button type="primary" v-on:click="reg()">注册</el-button>
          </el-row>
        </el-col>
      </el-row>      
    </el-main>
    <el-footer>
      <p>Powered by Vue.js and Bootstrap!</p>
    </el-footer>
  </el-container>
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
            this.$message({
              message: '登录成功！',
              type: 'success'
            });
            Sstorage.set('nickName', response.data.NickName);
            Sstorage.set('userID', response.data.userID);
            
            Sstorage.set('localName', response.data.DJName);
            Sstorage.set('localAgencyFk', response.data.local_agency_fk);
            
            Sstorage.set('tokenID', response.data.tokenID);
            //  console.log(response);
            setTimeout(()=>{
              this.$router.replace({ path: 'home' })
            },500)
            // var int=self.setInterval(this.$router.replace({ path: 'main' }),1000);
          }else{
            console.log(response);
            this.$message.error('登录失败！');
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
#loginInputs{
  margin-top: 16%;
}
#Login{
  /* width: 100vh;
  height: 100vh; */
}
</style>