<template>
  <el-row>
    <el-col :span=24>
      <el-table :data="group.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
        <!-- <el-table :data="group.data" style="width: 100%" highlight-current-row show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
        <!-- <el-table :data="group.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
        <el-table-column type="index" width="100"></el-table-column>
        <!-- <el-table-column v-for="(v,i) in group.columns" :prop="v.field" :label="v.title" :sortable="v.sortable"> -->
        <el-table-column v-for="(value, key) in group.columns" :prop="value.field" :label="value.title" :sortable="value.sortable">
          <template slot-scope="scope">
            <span v-if="scope.row.isSet">
              <span v-if='value.field != "id"'><el-input size="mini" placeholder="请输入内容" v-model="group.currentRow[value.field]"></el-input></span>
              <span v-else>{{scope.row[value.field]}}</span>
            </span>
            <span v-else>{{scope.row[value.field]}}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150">
          <template slot-scope="scope">
            <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" @click="currentRowChange(scope.row,scope.$index,false)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" style="cursor: pointer;">删除</span>
            <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" @click="currentRowChange(scope.row,scope.$index,true)">取消</span>
          </template>
        </el-table-column>
      </el-table>
    </el-col>
    <el-col :span=24>
      <div class="el-table-add-row" style="width: 99.2%;" @click="doAdd()"><span class="el-icon-circle-plus-outline">添加新的组织机构</span></div>
    </el-col>
  </el-row>
</template>

<script>

import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import InputCheck from '@/module/inputcheck.js';
// import CustomeAlert from  '@/components/sysinfo/CustomAlert.vue';

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
          { field: "id", title: "编号", width: 150, sortable: true },
          { field: "name", title: "组织名称", width: 320, sortable: true },
          { field: "remark", title: "备注", width: 320, sortable: false },
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
    // CustomeAlert,
  },
  methods: {
    choice(id){
      // console.log(zuid)
    },
    // handleCurrentChange(selectRow){
    //   this.group.currentRow = selectRow;
    //   console.log(this.group.currentRow);
    // },
    currentRowChange(rowContent,index,isCancel){
      console.log(rowContent,index,isCancel);
      console.log(this.group.data)
      //点击修改、保存,判断是否已经保存所有操作
      for (let item of this.group.data) {
        if (item.isSet && (item.id != rowContent.id)) {
          this.$message.warning("请先保存当前编辑项!");
          return false;
        }
      }
      //是否是取消操作
      if (isCancel) {
        if (null === this.group.currentRow.id) {
          console.log(this.group.currentRow.id)
          this.group.data.splice(index, 1);
        }
        return rowContent.isSet = !rowContent.isSet;
      }
      if (rowContent.isSet) {
        (function () {
            let tempData = JSON.parse(JSON.stringify(this.group.currentRow));
            for (let k in tempData) rowContent[k] = tempData[k];
            this.$message({
                type: 'success',
                message: "保存成功!"
            });
            //然后这边重新读取表格数据
            // app.readMasterUser();
            rowContent.isSet = false;
        })();
      }else{
        // this.group.currentRow = JSON.parse(JSON.stringify(rowContent));
        this.group.currentRow = JSON.parse(JSON.stringify(rowContent));
        // console.log(this.group.currentRow)
        rowContent.isSet = true;
      }
    },
    doAdd(){
      for (let item of this.group.data) {
        if (item.isSet) return this.$message.warning("请先保存当前编辑项!");
      }
      let tempAddData = {id: null, "name": "", "remark": "", "isSet": true,};
      this.group.data.push(tempAddData);
      this.group.currentRow = JSON.parse(JSON.stringify(tempAddData));
      // console.log(this.group.data)
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