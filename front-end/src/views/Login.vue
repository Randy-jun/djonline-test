<template>
  <el-container>
    <el-header>
      <h1>Financial Management Systems Software</h1>
    </el-header>
    <el-main>
      <div class="login-box">
        <form id="jsLoginForm" autocomplete="off">
          <input type="hidden" name="csrfmiddlewaretoken" value="YgezAZugvEEiADKS1yFQFwW75jez80R9dEVXbaVLSrilwzeZ2cnsTWvXGmXPyVE1">
          <el-row>
            <el-col :span="8">
              <el-input id="username"  v-model="userInfo.userName" placeholder="请输入帐号">
                <template slot="prepend">帐号</template>
              </el-input> 
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">
              <el-input id="password" v-model="userInfo.passWord" v-on:keyup.enter.native="login($event)" type="password" placeholder="请输入密码">
                <template slot="prepend">密码</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8">
              <el-button id="login" v-on:click="login($event)" style="width:98%" type="success" v-bind:disabled="isWorking">立即登录</el-button>
            </el-col>
          </el-row>
        </form>
      </div>
    </el-main>
    <el-footer>
        <p>Powered by Vue.js and Element-ui!</p>
    </el-footer>
  </el-container>
</template>

<script>

import { login } from '@/api/api'
import Sstorage from '@/module/sstorage.js';
import Axios from 'axios'

export default {
  name: 'Login',
  props: {
    msg: String
  },
  data() {
    return {
      userInfo:{
        userName:'',
        passWord:'',
      },
      isWorking:false,
      status:{
        userCheck:false,
        passCheck:false,
      },
    }
  },
  methods: {
    // login(e){
    login : function(event){
      console.log(event)
      const api='http://127.0.0.1:9090/login/';
      if (event.type == 'click' || event.keyCode == 13) {
        // var params = new URLSearchParams();
        // params.append("username",this.userInfo.userName);
        // params.append("password",this.userInfo.passWord); 
        // Axios.post(api, params).then((response) => {
        //   console.log(response);
        // }).catch(error => {
        //   console.log(error);
        // });
        this.isWorking = true;
        login({
            username:this.userInfo.userName,
            password:this.userInfo.passWord,
        }).then((response) => {
          console.log(response);    
          setTimeout(()=>{
              this.$router.replace({ path: 'home' })
          },500)
          this.$message({
            message: '登录成功！',
            type: 'success'
          });
        }).catch((error) => {
          console.log(error);
          this.$message.error('登录失败！');
          this.isWorking = false;
        })
      }
    },
  },
  mounted() {
  },
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0px;
  }
}
.login-box {
  margin-top:15%;
  margin-left:40%;
}
.el-header {
  background-color: rgb(91, 202, 156);
  line-height: 60px;
}
.el-footer {
  background-color: rgb(214, 252, 236);
}
.el-main {
  background-color: rgb(214, 252, 236);
  height: 888px;
}
</style>