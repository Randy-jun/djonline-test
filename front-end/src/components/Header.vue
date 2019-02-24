<template>
  <el-row>
    <el-col :span=19>
      <h1>DJonline</h1>
    </el-col>
    <el-col :span=1>
      <small>{{nickname}}</small>
    </el-col>
    <el-col :span=2>
      <small :title=group>{{group}}</small>
    </el-col>
    <el-col :span=1>
      <small><a class="badge badge-second el-icon-setting" v-on:click="passwordChange()">修改密码</a></small>
    </el-col>
    <el-col :span=1>
      <small><a class="badge badge-second el-icon-setting" v-on:click="logout()">退出</a></small>
    </el-col>
    <el-dialog title="申诉" v-model="dialogVisible" :close-on-click-modal="false"> 
      <el-form :model="resetForm" status-icon :rules="resetFormRules" ref="resetForm" label-width="100px">
        <el-form-item label="新密码" prop="newpwd">
          <el-input type="password" v-model="resetForm.newpwd" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="renewpwd">
          <el-input type="password" v-model="resetForm.renewpwd" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
    </el-dialog>
  </el-row>
</template>

<script>
import Sstorage from '@/module/sstorage.js';
export default {
  name: 'Header',
  props: {
    msg: String
  },
  data() {
    var validatePass = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入新密码'));
      } else if (value.toString().length < 6 || value.toString().length > 18) {
        callback(new Error('密码长度为6 - 18个字符'))
      } else {
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.resetForm.newpwd) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      nickname:'',
      group:'',
      dialogVisible: false,
      resetForm: {
        newpwd: '',
        renewpwd: '',
      },
      resetFormRules: {
        newpwd: [
          { required: true, validator: validatePass, trigger: 'blur' }
        ],
        renewpwd: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ]
      },
    }
  },
  methods: {
    passwordChange(){
      this.dialogVisible = true;
      console.log(this.dialogVisible)
    },
    logout(){
      // alert("setting")
      Sstorage.clearAll();
      this.$router.replace({ path: '/login' })
    },
  },
  mounted() {
    this.nickname = Sstorage.get('nickName');
    this.group = Sstorage.get('group');
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>