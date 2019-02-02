<template>
  <el-container>
    <el-header>
      <h1>Financial Management Systems Software</h1>
    </el-header>
    <el-main>
      <div class="login-box">
        <el-row>
          <el-col :span="8">
            <el-input id="username"  v-model="username" placeholder="请输入帐号">
              <template slot="prepend">帐号</template>
            </el-input> 
            <small>{{username}}</small>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-input id="password" v-model="password" type="password" placeholder="请输入密码">
              <template slot="prepend">密码</template>
            </el-input>
            <small>{{password}}</small>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-button id="login" v-on:click="login($event)" style="width:98%" type="success">登录</el-button>
          </el-col>
        </el-row>
      </div>
    </el-main>
    <el-footer>
        <p>Powered by Vue.js and Element-ui!</p>
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
      status:{
        userCheck:false,
        passCheck:false,
      }
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