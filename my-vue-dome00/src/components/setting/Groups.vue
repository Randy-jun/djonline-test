<template>
  <div class="col" id="groups">
    <CustomeAlert v-if="alertState" v-bind:alertmsg="alertMsg" />
    <!-- <div class="alert alert-success" role="alert">
      A simple success alert—check it out!
    </div> -->
    <small>总共: <span class="font-italic font-weight-bold">{{count_all}}</span> 条记录</small>
    <div class="row">
      <table class="table table-hover table-responsive-lg">
         <thead class="thead-lights">
            <tr>
               <!-- <th>
                 <div class="custom-control custom-checkbox">
                  <input type="checkbox" class="custom-control-input" v-on:change="choiceall()" id="allCheck">
                  <label class="custom-control-label" for="allCheck">全选</label>
                </div>
               </th> -->
               <th>序号</th>
               <th>组团社ID</th>
               <th>组团社名称</th>
               <th>备注</th>
               <th>操作</th>
            </tr>
         </thead>
         <tbody>
            <!-- key 要写到后面才可以 -->
            <tr v-for="(item, index) in data_list">
              <!-- <td>
                 <div class="custom-control custom-checkbox">
                  <input type="checkbox" class="custom-control-input" v-on:change="choiceall()" v-bind:id="item.id">
                  <label class="custom-control-label" v-bind:for="item.id"></label>
                </div>
               </td> -->
               <td>{{index + 1}}</td>
               <td v-bind:id="item.id" >{{item.id}}</td>
               <td v-bind:id="item.id">{{item.name}} </td>
               <td v-bind:id="item.id">{{item.remark}}</td>
               <td>
                <div class="btn-group btn-group-sm">
                  <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#editPage" v-on:click="update(index, item)">编辑</button>
                  <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#deleteConfirm" v-on:click="del(index, item.id)">删除</button>
                </div>
              </td>
            </tr>
         </tbody>
      </table>
    </div>
    <div class="row align-items-end">
      <div class="col"><button type="button" class="btn btn-success btn-sm" data-toggle="modal" data-target="#editPage" v-on:click="add()">新增组团社</button></div>
    </div>
    <div class="modal fade" role="dialog" id="editPage">
      <div class="modal-dialog modal-md modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{editPage.title}}</h5>
            <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button> -->
          </div>
          <div class="modal-body">
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text" id="name">组团社名称</span>
              </div>
              <input type="text" class="form-control" id="nameInput" aria-describedby="name" v-model="group.name">
            </div>
            <small>{{group.name}}</small>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text">备注</span>
              </div>
              <textarea class="form-control" aria-label="备注" placeholder="备注内容请保持在120字以内..." v-model="group.remark"></textarea>
            </div>
            <small>{{group.remark}}</small>
          </div>
          <div class="modal-footer">
            <button class="btn btn-success btn-sm" data-dismiss="modal" v-on:click="doSave()">保存</button>
            <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" role="dialog" id="deleteConfirm">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">确认删除吗？</h5>
          </div>
          <div class="modal-footer">
            <button class="btn btn-danger btn-sm" data-dismiss="modal" v-on:click="doDel()">确认</button>
            <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import InputCheck from '@/module/inputcheck.js';
import CustomeAlert from  '@/components/sysinfo/CustomAlert.vue';

export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      count_all:null,
      alertState:false,
      alertMsg:{
        stateFlag:null,
        msgConten:null,
      },
      group:{
        name:null,
        remark:null,
      },
      editPage:{
        title:null,
        methods:null,
        id:null,
        localId:null,
      },
      delete:{
        id:null,
        localId:null,
      },
      api:'http://127.0.0.1:9090/acct/agencies/',
      data_list:[],
    }
  },
  components: {
    CustomeAlert,
  },
  methods: {
    choice(id){
      // console.log(zuid)
    },
    del(localId, id){
      this.delete.localId=localId;
      this.delete.id=id;
    },
    doDel(){
      // var api='http://127.0.0.1:9090/acct/agencies/';
      var params = new URLSearchParams();
      params.append("req_method","DELETE");
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("pk",this.delete.id);
      Axios.post(this.api, params).then((response)=>{
        console.log(response);
        if(response.data.status_flag){
          console.log(response);

          this.alertMsg.stateFlag="alert-success";
          this.alertMsg.msgConten="删除成功！";

          this.alertState=true;
          this.count_all-=1;
          this.data_list.splice(this.delete.localId,1)
          setTimeout(()=>{
            this.alertState=false;
          },2000);
        }else{
          console.log(response);

          this.alertMsg.stateFlag="alert-danger";
          this.alertMsg.msgConten="删除失败！";

          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
          },2000);
        }})
        .catch((error)=>{
          console.log(error);
        });
    },
    update(localId, groupContent){
      this.group.name=groupContent.name;
      this.group.remark=groupContent.remark;
      this.editPage.title="修改组团社";
      this.editPage.methods="UPDATE";
      this.editPage.id=groupContent.id;
      this.editPage.localId=localId;
    },
    add(){
      this.group.name="";
      this.group.remark="";
      this.editPage.title="新增组团社";
      this.editPage.methods="ADD";
      this.editPage.localId=null;
    },
    doSave(){
      // const api='http://127.0.0.1:9090/acct/agencies/';
      if(InputCheck.namecheck(this.group.name)){
        this.alertMsg={
            'stateFlag':'alert-danger',
            'msgConten':'组织名称不能为空或空格',
        }
        this.alertState=true;
        setTimeout(()=>{
          this.alertState=false;
        },2000);
        return 1;
      }
      var params = new URLSearchParams();
      params.append("req_method",this.editPage.methods);
      
      if(null !== this.editPage.localId){
        params.append("pk",this.editPage.id);
      }

      params.append("name",this.group.name);
      params.append("remark",this.group.remark);
      
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("local_agency_fk",Sstorage.get('localAgencyFk'));

      Axios.post(this.api, params).then((response)=>{
        if(response.data.status_flag){
          console.log(response);
          this.alertMsg.stateFlag="alert-success";

          // console.log(response.data.result)
          console.log(this.editPage.localId)
          if(null !== this.editPage.localId){
            this.data_list.splice(this.editPage.localId,1,response.data.result);
            this.alertMsg.msgConten="修改成功！";
          }else{
            this.count_all+=1;
            this.data_list.push(response.data.result)
            this.alertMsg.msgConten="添加成功！";
          }
          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
            // this
          },2000);
        }else{
          console.log(response);
          this.alertMsg={
            'stateFlag':'alert-danger',
            'msgConten':'修改失败！',
          }
          if(this.editPage.localId){
            this.alertMsg.msgConten="修改失败！";
          }else{
            this.alertMsg.msgConten="添加失败！";
          }
          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
            // this
          },2000);
        }})
        .catch((error)=>{
          console.log(error);
        });
    },
  },
  mounted() {
    // var list = JSON.parse(localStorage.getItem('list'));
    
    // const api='http://127.0.0.1:9090/acct/agencies/';
    var params = new URLSearchParams();
    params.append("req_method","GET");
    params.append("userID",Sstorage.get('userID'));
    params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
    params.append("tokenID",Sstorage.get('tokenID'));
    Axios.post(this.api, params).then((response)=>{
        this.data_list=response.data.result;
        this.count_all=response.data.result.length;
        console.log(this.data_list)
        // setTimeout(()=>{
        //   this.data_list.splice(0,1)
        //   console.log(this.data_list)
        // },5000);
        
        // console.log(typeof(response.data.result));
        // this.test_list=response.data.result;
      }).catch((error)=>{
        // console.log(error);
      })
  }
}
</script>

<style scoped>
.ho-pad{
  padding-top: 28px;
  padding-bottom: 28px;
}
#groups{
  margin-bottom: 2%;
}
</style>