<template>
  <el-row>
    <el-row style="height:750px">
    <!-- <el-col :span=24> -->
      <el-scrollbar style="height:100%">
        <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <el-table-column type="index" width="100"></el-table-column>
          <!-- <el-table-column v-for="(v,i) in table.columns" :prop="v.field" :label="v.title" :sortable="v.sortable"> -->
          <el-table-column v-for="(value, key) in table.columns" :prop="value.field" :label="value.title" :sortable="value.sortable">
            <template slot-scope="scope">
              <span v-if="scope.row.isSet">
                <span v-if='value.isEdit'><el-input size="mini" placeholder="请输入内容" v-model="table.currentRow[value.field]"></el-input></span>
                <span v-else>{{scope.row[value.field]}}</span>
              </span>
              <span v-else>{{scope.row[value.field]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作" width="200">
            <template slot-scope="scope">
              <span v-if="!scope.row.isSet" class="el-tag el-tag el-tag--mini" style="cursor: pointer;" v-on:click="dialogData.tableVisible =true,currentRowModal(scope.row,scope.$index)">详细</span>
              <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,false)">
                  {{scope.row.isSet?'保存':"修改"}}
              </span>
              <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" v-on:click="doDel(scope.row,scope.$index)" style="cursor: pointer;">删除</span>
              <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,true)">取消</span>
            </template>
          </el-table-column>
        </el-table>
      </el-scrollbar>
    </el-row>
    <el-row>
      <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="dialogData.tableVisible =true,doAdd()">添加新的组织机构</el-button>
    </el-row>
    <el-row>
      <el-pagination  
        v-on:size-change="handleSizeChange"
        v-on:current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="table.countAll">
      </el-pagination>
    </el-row>
    <el-row>
    <el-dialog title="线路报价单" :visible.sync="dialogData.tableVisible">
      <el-row align="top">
        <el-col :span="8">
          <span v-if="!dialogData.isAdd" style="font-size: 24px;"> 线路报价单ID:{{dialogData._Content.id}}</span>
        </el-col>
        <el-col :span="4" :offset="12">
          <el-button type="primary" style="cursor: pointer;" v-on:click="contentChangeDialog(false)">
            {{dialogData.isEdit?'保存':"修改"}}
          </el-button>
          <el-button type="info" style="cursor: pointer;" v-on:click="contentChangeDialog(true)">
            {{dialogData.isEdit?'取消':"删除"}}
          </el-button>
        </el-col>
      </el-row>
      <el-row style="padding: 10px 10px">
        <el-col :gutter="20" :span="12">
          <span v-if='dialogData.isEdit'><el-input size="mini" placeholder="请输入内容" v-model="dialogData._Content.name"><template slot="prepend">线路名称:</template></el-input></span>
          <span v-else>线路名称:{{dialogData._Content.name}}</span>
        </el-col>
        <el-col :span="12">
          <span v-if='dialogData.isEdit'><el-input size="mini" placeholder="请输入内容" v-model="dialogData._Content.remark"><template slot="prepend">备注:</template></el-input></span>
          <span v-else>备注:{{dialogData._Content.remark}}</span>
        </el-col>
      </el-row>
      <el-table :data="dialogData.table.data">
        <el-table-column type="index" width="100"></el-table-column>
        <el-table-column v-for="(value, key) in dialogData.table.columns" :prop="value.field" :label="value.title" :sortable="value.sortable">
          <template slot-scope="scope">
            <span v-if="scope.row.isSet">
              <span v-if='value.isEdit'><el-input size="mini" placeholder="请输入内容" v-model="dialogData.table.currentRow[value.field]"></el-input></span>
              <span v-else>{{scope.row[value.field]}}</span>
            </span>
            <span v-else>{{scope.row[value.field]}}</span>
          </template>
        </el-table-column>
        <!-- <el-table-column property="id" label="编号" width="150"></el-table-column>
        <el-table-column property="kind" label="名称" width="200"></el-table-column>
        <el-table-column property="price" label="报价"></el-table-column> -->
        <el-table-column label="操作" width="200">
          <template slot-scope="scope">
            <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChangeDialog(scope.row,scope.$index,false)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini"  style="cursor: pointer;" v-on:click="doDelDialog(scope.row,scope.$index)">删除</span>
            <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChangeDialog(scope.row,scope.$index,true)">取消</span>
          </template>
        </el-table-column>
      </el-table>
      <el-row>
        <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAddDialog()">添加新的组织机构</el-button>
      </el-row>
       <el-row>
        <el-col :span="24">
          <span v-if='dialogData.isEdit'><el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入内容" v-model="dialogData._Content.detail"></el-input></span>
          <span v-else>{{dialogData._Content.detail}}</span>
        </el-col>
      </el-row>
    </el-dialog>
    </el-row>
  </el-row>
</template>

<script>

import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import InputCheck from '@/module/inputcheck.js';

export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      table: {
        countAll: null,
        currentRow: null,//选中行   
        columns: [
          { field: "id", title: "编号", width: 60, isEdit: false, sortable: true },
          { field: "name", title: "线路名称", width: 320, isEdit: true, sortable: true },
          { field: "top3_ref_data0", title: "1档位报价", width: 320, isEdit: false, sortable: false },
          { field: "top3_ref_data1", title: "2档位报价", width: 320, isEdit: false, sortable: false },
          { field: "top3_ref_data2", title: "3档位报价", width: 320, isEdit: false, sortable: false },
          { field: "remark", title: "备注", width: 320, isEdit: true, sortable: false },
        ],
        // tempData: [],
        data: [],
      },
      api:'http://127.0.0.1:9090/acct/lineprices/',
      currentPage4: 4,
      dialogData:{
        ContentId: "",
        tableVisible: false,
        isEdit: false,
        isAdd: false,
        _Content: {
          id: "",
          name: "",
          remark: "",
          detail: "",
        },
        Content: null,
        table: {
          countAll: null,
          currentRow: null,
          columns: [
            { field: "id", title: "档位", width: 60, isEdit: false, sortable: true },
            { field: "kind", title: "名称", width: 320, isEdit: true, sortable: true },
            { field: "price", title: "报价", width: 320, isEdit: true, sortable: true },
          ],
          data:[],
        }
      }
      
    }
  },
  components: {
    // CustomeAlert,
  },
  methods: {
    choice(){
      // console.log(zuid)
    },
    // handleCurrentChange(selectRow){
    //   this.table.currentRow = selectRow;
    //   console.log(this.table.currentRow);
    // },

    //TODO: to finish this page.
    currentRowModal(rowContent,index){
      for (let item of this.table.data) {
        if (item.isSet && (item.id != rowContent.id)) {
          this.$message.warning("请先保存当前编辑项!");
          return false;
        }
      }
      let localID = index;
      this.dialogData.isAdd = false;
      this.dialogData.isEdit = false;
      var params = new URLSearchParams();
      // params.append("req_method","GET_SINGLE");
      params.append("req_method","GETONE");
      
      params.append("pk",rowContent.id);
      
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("local_agency_fk",Sstorage.get('localAgencyFk'));

      Axios.post(this.api, params).then((response)=>{
        console.log(response)

        this.dialogData.Content = JSON.parse(JSON.stringify(response.data.result.line_price));
        // this.dialogData._Content = this.dialogData.Content;
        this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));

        this.dialogData.table.data = JSON.parse(JSON.stringify(response.data.result.ref_prices));
        this.dialogData.table.data.forEach(item => {
          this.$set(item, 'isSet', false);
        });
      }).catch((error)=>{
        console.log(error);
      })
    },
    currentRowChange(rowContent,index,isCancel){
      //点击修改、保存,判断是否已经保存所有操作
      // console.log(rowContent, index, isCancel)
      for (let item of this.table.data) {
        if (item.isSet && (item.id != rowContent.id)) return this.$message.warning("请先保存当前编辑项!");
      }
      //是否为取消操作
      if (isCancel) {
        if (null === this.table.currentRow.id) return this.table.data.splice(index, 1);
        rowContent.isSet = !rowContent.isSet;
        return this.$set(this.table.data, index, rowContent)
      }

      if (rowContent.isSet) {
        // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));

        if(InputCheck.namecheck(this.table.currentRow.name)) return this.$message.warning("线路名称不能为空或空格!");

        var params = new URLSearchParams();
        
        if(null !== this.table.currentRow.id){
          params.append("pk",this.table.currentRow.id);
          params.append("req_method",'UPDATE');
        }else{
          params.append("req_method",'ADD');
        }
        params.append("name",this.table.currentRow.name);
        params.append("remark",this.table.currentRow.remark);
        params.append("detail",this.table.currentRow.detail);
        
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));

        Axios.post(this.api, params).then((response)=>{
          if(response.data.status_flag){
            console.log(response);
            let tempData = response.data.result;
            console.log(tempData);
            this.$set(tempData, 'isSet', false);
            if(null !== this.table.currentRow.id){
              this.table.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "修改成功！"
              });
            }else{
              this.table.countAll+=1;
              this.table.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "添加成功！"
              });
            }
          }else{
            console.log(response);

            if(null !== this.table.currentRow.id){
              this.$message({
                type: 'error',
                message: "修改失败！"
              });
            }else{
              // this.table.data.splice(index, 1);
              this.$message({
                type: 'error',
                message: "添加失败！"
              });
            }
          }})
          .catch((error)=>{
            console.log(error);
            if(null !== this.table.currentRow.id) this.table.data.splice(index, 1);
            this.$message({
              type: 'error',
              message: "保存失败！"
            });
          });
        /*
        for (let k in tempData) rowContent[k] = tempData[k];
        console.log(this.table.data)
        return 0;
        */
        // this.$message({
        //     type: 'success',
        //     message: "保存成功!"
        // });
        //然后这边重新读取表格数据
        // app.readMasterUser();
      }else{
        this.table.currentRow = JSON.parse(JSON.stringify(rowContent));
        // this.table.currentRow = rowContent;
        rowContent.isSet = true;
        // this.$set(this.table.data, index, rowContent);
        this.table.data.splice(index, 1, rowContent);
        return true;
      }
    },
    doAdd(){
      for (let item of this.table.data) {
        if (item.isSet){
          this.$message.warning("请先保存当前编辑项!");
          return this.$set(this.dialogData, 'tableVisible', false);
        }
      }
      this.dialogData.isAdd = true;
      this.dialogData.isEdit = true;
      this.dialogData._Content = JSON.parse(JSON.stringify({id: null, "name": "", "remark": "", "detail": "",}));
      // this.dialogData.Content = JSON.parse(JSON.stringify(this.dialogData._Content));
      this.dialogData.table.data = [];
      this.dialogData.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      // console.log(this.table.data)
    },
    doDel(rowContent, index){
      this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(rowContent, index);
        var params = new URLSearchParams();
        params.append("req_method","DELETE");
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("pk",rowContent.id);

        Axios.post(this.api, params).then((response)=>{
          console.log(response);
          if(response.data.status_flag){
            this.table.countAll-=1;
            this.table.data.splice(index,1);
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
          }else{
            this.$message({
              type: 'error',
              message: '删除失败!'
            });
          }}).catch((error)=>{
            console.log(error);
            this.$message({
              type: 'error',
              message: '删除失败!'
            });
          });
      }).catch(() => {
        // this.$message({
        //   type: 'info',
        //   message: '已取消删除'
        // });          
      });
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
    contentChangeDialog(isCancel){
      console.log(this.dialogData.Content)
      // this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));
      if(isCancel){
        console.log(this.dialogData.isAdd)
        if(!this.dialogData.isEdit){
          console.log("dsadsa");
        }else{
          if (this.dialogData.isAdd){
            return this.$set(this.dialogData, 'tableVisible', false);
          } else {
            this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));;
            return this.$set(this.dialogData, 'isEdit', false);
          }
        }
      }else{
        return this.$set(this.dialogData, 'isEdit', true);
      }
    },
    currentRowChangeDialog(rowContent,index,isCancel){
      //点击修改、保存,判断是否已经保存所有操作
      for (let item of this.dialogData.table.data) {
        if (item.isSet && (item.id != rowContent.id)) return this.$message.warning("请先保存当前编辑项!");
      }
      //是否为取消操作
      if (isCancel) {
        if (null === this.dialogData.table.currentRow.id) return this.dialogData.table.data.splice(index, 1);
        rowContent.isSet = !rowContent.isSet;
        return this.$set(this.dialogData.table.data, index, rowContent)
      }

      if (rowContent.isSet) {
        // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));

        if(InputCheck.namecheck(this.dialogData.table.currentRow.name)) return this.$message.warning("报价名称不能为空或空格!");

        var params = new URLSearchParams();
        
        if(null !== this.table.currentRow.id){
          params.append("pk",this.dialogData.table.currentRow.id);
          params.append("req_method",'UPDATE');
        }else{
          params.append("req_method",'ADD');
        }
        params.append("name",this.dialogData.table.currentRow.name);
        params.append("remark",this.dialogData.table.currentRow.remark);
        
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));

        Axios.post(this.api, params).then((response)=>{
          if(response.data.status_flag){
            console.log(response);
            let tempData = response.data.result;
            console.log(tempData);
            this.$set(tempData, 'isSet', false);
            if(null !== this.dialogData.table.currentRow.id){
              this.dialogData.table.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "修改成功！"
              });
            }else{
              this.dialogData.table.countAll+=1;
              this.dialogData.table.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "添加成功！"
              });
            }
          }else{
            console.log(response);

            if(null !== this.dialogData.ble.currentRow.id){
              this.$message({
                type: 'error',
                message: "修改失败！"
              });
            }else{
              // this.table.data.splice(index, 1);
              this.$message({
                type: 'error',
                message: "添加失败！"
              });
            }
          }})
          .catch((error)=>{
            console.log(error);
            if(null !== this.dialogData.table.currentRow.id) this.dialogData.table.data.splice(index, 1);
            this.$message({
              type: 'error',
              message: "保存失败！"
            });
          });
        /*
        for (let k in tempData) rowContent[k] = tempData[k];
        console.log(this.table.data)
        return 0;
        */
        // this.$message({
        //     type: 'success',
        //     message: "保存成功!"
        // });
        //然后这边重新读取表格数据
        // app.readMasterUser();
      }else{
        this.dialogData.table.currentRow = JSON.parse(JSON.stringify(rowContent)); 
        rowContent.isSet = true;
        this.dialogData.table.data.splice(index, 1, rowContent);
        return true;
      }
    },
    doAddDialog(){
      for (let item of this.dialogData.table.data) {
        if (item.isSet) return this.$message.warning("请先保存当前编辑项!");
      }
      let tempAddData = {id: null, "kind": "", "price": "", "isSet": true,};
      this.dialogData.table.data.push(tempAddData);
      this.dialogData.table.currentRow = JSON.parse(JSON.stringify(tempAddData));
      // console.log(this.table.data)
    },
    doDelDialog(rowContent, index){
      this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(rowContent, index);
        var params = new URLSearchParams();
        params.append("req_method","DELETE");
        // params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("pk",rowContent.id);
        console.log(rowContent.id)

        Axios.post(this.api, params).then((response)=>{
          console.log(response);
          if(response.data.status_flag){
            this.table.countAll-=1;
            this.table.data.splice(index,1);
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
          }else{
            this.$message({
              type: 'error',
              message: '删除失败!'
            });
          }}).catch((error)=>{
            console.log(error);
            this.$message({
              type: 'error',
              message: '删除失败!'
            });
          });
      }).catch(() => {
        // this.$message({
        //   type: 'info',
        //   message: '已取消删除'
        // });          
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
      // console.log(response)
      this.table.countAll = response.data.item_num
      this.table.data = response.data.result;
      // this.table.countAll=response.data.item_num;
      this.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      this.table.data = JSON.parse(JSON.stringify(this.table.data));
      console.log(this.table.data);
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
.el-scrollbar__wrap {
  overflow-x: hidden;
}
</style>