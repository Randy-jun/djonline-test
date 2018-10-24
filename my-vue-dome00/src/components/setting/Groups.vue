<template>
  <el-row>
    <el-col :span=24>
      <el-table :data="group.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}">
        <el-table-column type="index"></el-table-column>
        <!-- <el-table-column v-for="(v,i) in group.columns" :prop="v.field" :label="v.title" :sortable="v.sortable"> -->
        <el-table-column v-for="(value, key) in group.columns" :prop="value.field" :label="value.title">
          <template slot-scope="scope">
            <span v-if="scope.row.isSet">
              <el-input size="mini" placeholder="请输入内容" v-model="group.currentRow[value.field]">
              </el-input>
            </span>
            <span v-else>{{scope.row[value.field]}}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="100">
          <template slot-scope="scope">
            <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" @click="currentRowChange(scope.row,scope.$index,true)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" style="cursor: pointer;">删除</span>
            <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" @click="currentRowChange(scope.row,scope.$index,false)">取消</span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>   
  </el-row>
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
      group: {
        currentRow: null,//选中行   
        columns: [
          { field: "id", title: "编号", width: 150 },
          { field: "name", title: "组织名称", width: 120 },
          { field: "remark", title: "备注", width: 220 },
        ],
        // tempData: [],
        data: [],
      },
      count_all:null,
      alertState:false,
      alertMsg:{
        stateFlag:null,
        msgConten:null,
      },
      group1:{
        name:null,
        remark:null,
      },
      editPage:{
        isUpdate:true,
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
    handleCurrentChange(val){
      this.group.currentRow = val;
      console.log(this.group.currentRow);
    },
    currentRowChange(rowContent,index,isset){
      console.log(rowContent,index,isset);
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
      this.group1.name=groupContent.name;
      this.group1.remark=groupContent.remark;

      this.$set(this.data_list[localId], "isEdite", this.data_list[localId].isEdite = true)
      this.data_list[localId].isEdite = true
      // console.log(this.data_list[localId]);
      console.log(this.data_list);
      // console.log(groupContent)

      this.editPage.isUpdate=true;
      this.editPage.title="修改组团社";
      this.editPage.methods="UPDATE";
      this.editPage.id=groupContent.id;
      this.editPage.localId=localId;
    },
    add(){
      this.editPage.isUpdate=false;
      this.group1.name="";
      this.group1.remark="";
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
    Axios.post(this.api, params).then((response) => {
      this.group.data=response.data.result;
      // this.count_all=response.data.item_num;
      this.group.data.forEach(item => {
        item.isSet=false;
        // this.group.data.push(item)
      });
      console.log(this.group.data);
      // setTimeout(()=>{
      //   this.data_list.splice(0,1)
      //   console.log(this.data_list)
      // },5000);
      
      // console.log(typeof(response.data.result));
      // this.test_list=response.data.result;
    }).catch((error) => {
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