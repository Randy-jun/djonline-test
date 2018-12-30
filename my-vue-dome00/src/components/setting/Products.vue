<template>
  <el-row>
    <!-- <el-row style="height:750px"> -->
    <el-row>
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
              <!-- <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,false)">
                  {{scope.row.isSet?'保存':"修改"}}
              </span> -->
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
          <el-button v-if="dialogData.isEdit" type="info" style="cursor: pointer;" v-on:click="contentChangeDialog(true)">取消</el-button>
          <el-button v-else type="info" style="cursor: pointer;" v-on:click="doDel(dialogData._Content,dialogData.localID)">删除</el-button>
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
        <el-table-column type="index" width="100">档位</el-table-column>
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
            <span v-if="dialogData.isAdd || scope.row.isNew" class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChangeDialog(scope.row,scope.$index,false)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <!-- <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini"  style="cursor: pointer;" v-on:click="doDelDialog(scope.row,scope.$index)">删除</span> -->
            <span v-if="dialogData.isAdd || scope.row.isNew" class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChangeDialog(scope.row,scope.$index,true)">取消</span>
          </template>
        </el-table-column>
      </el-table>
      <el-row>
        <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAddDialog()">添加新的线路报价单</el-button>
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
import Product from '@/module/setting/product.js';

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
      refApi:'http://127.0.0.1:9090/acct/refprices/',
      currentPage4: 4,
      dialogData:{
        localID:"",
        contentId: "",
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
            //{ field: "id", title: "编号", width: 60, isEdit: false, sortable: true },
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
      // let localID = index;
      this.dialogData.isAdd = false;
      this.dialogData.isEdit = false;
      this.dialogData.contentId = rowContent.id;
      this.dialogData.localID = index;

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
            // console.log(response);
            let tempData = response.data.result;
            // console.log(tempData);
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
      this.dialogData.contentId = null;
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
        console.log(rowContent.id, index);
        var params = new URLSearchParams();
        params.append("req_method","DELETE");
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("pk",rowContent.id);
        // console.log(params.getAll("pk","req_method"));
        Axios.post(this.api, params).then((response)=>{
          if(response.data.status_flag){
            this.table.countAll-=1;
            if (this.dialogData.tableVisible) this.$set(this.dialogData, 'tableVisible', false)
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
      // console.log(this.dialogData.Content)
      // this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));
      if(isCancel){
        console.log(this.dialogData.isAdd)
        if(!this.dialogData.isEdit){
          console.log("isCancel,isEdit");
        }else{
          if (this.dialogData.isAdd){
            return this.$set(this.dialogData, 'tableVisible', false);
          } else {
            this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));
            return this.$set(this.dialogData, 'isEdit', false);
          }
        }
      }
      // console.log(dialogData.isSet)
      if (this.dialogData.isEdit) {
        // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));

        if(InputCheck.namecheck(this.dialogData._Content.name)) return this.$message.warning("线路名称不能为空或空格!");
        var params = new URLSearchParams();
        
        // console.log(this.dialogData._Content.id)
        if(null !== this.dialogData._Content.id){
          params.append("pk",this.dialogData._Content.id);
          params.append("req_method",'UPDATE');
          console.log("UPDATE")
        }else{
          params.append("req_method",'ADD');
          console.log("ADD")
          if(0 == this.dialogData.table.data.length){
            return this.$message({
              type: 'warning',
              message: "每条线路至少有一个默认报价！"
            });
          }
        }

        params.append("name",this.dialogData._Content.name);
        params.append("remark",this.dialogData._Content.remark);
        params.append("detail",this.dialogData._Content.detail);
        
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        
        console.log(params.getAll("pk"))
        Axios.post(this.api, params).then((response)=>{
          // console.log(response,"0000000");
          if(response.data.status_flag){
            // let tempData = response.data.result;
            if(null === this.dialogData.contentId){
              // this.table.countAll+=1;
              // this.table.data.splice(this.dialogData.localID,1,tempData);
              this.dialogData.contentId = response.data.result.id;

              let data2Add = {};
              this.dialogData.table.data.forEach((item,index) => {
                this.$set(item, 'user_id',Sstorage.get('userID'));
                this.$set(item, 'token',Sstorage.get('tokenID'));
                this.$set(item, 'local_agency_fk',Sstorage.get('localAgencyFk'));
                this.$set(item, 'line_price_fk', this.dialogData.contentId);
                data2Add[index] = JSON.stringify(item);
              });

              var paramsData = new URLSearchParams();
              paramsData.append("req_method",'ADD');
              // paramsData.append("data_to_add",JSON.stringify(this.dialogData.table.data));
              paramsData.append("data_to_add",JSON.stringify(data2Add));
              // console.log(paramsData.getAll("data_to_add"));
              Axios.post(this.refApi , paramsData).then((response)=>{
                // console.log(response);
                if(0 == response.data.failed_num){
                  this.$message({
                    type: 'success',
                    message: "添加成功！"
                  });
                  //this.$set(this.dialogData, 'tableVisible', false);
                }else{
                  return this.$message({
                            type: 'error',
                            message: "添加失败！"
                          });
                }
              })
              .catch((error)=>{
                return this.$message({
                        type: 'error',
                        message: "保存失败！"
                      });
              });
            }
            this.dialogData.isEdit = false;
            Product.getOne(this.dialogData.contentId).then((resp) => {
              let tempData = {
                'id': resp.result.line_price.id,
                'name': resp.result.line_price.name,
                'remark': resp.result.line_price.remark,
                'local_agency_fk': resp.result.line_price.local_agency_fk,
                'detail': resp.result.line_price.detail,
                'isSet': false,
              }
              resp.result.ref_prices.forEach((item, tempIndex) => {
                let tempContent = item.kind + ':' + item.price;
                tempData['top3_ref_data' + tempIndex] = tempContent;
              });
              // console.log(resp, this.dialogData.localID, "++++++++++", this.table.data)
              // this.table.data.splice(this.dialogData.localID,1,tempLine);
              
              if(this.dialogData.isAdd){
                //===========反写对话框内容==========
                this.dialogData.Content = JSON.parse(JSON.stringify(resp.result.line_price));
                // this.dialogData._Content = this.dialogData.Content;
                this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));

                this.dialogData.table.data = JSON.parse(JSON.stringify(resp.result.ref_prices));
                this.dialogData.table.data.forEach(item => {
                  this.$set(item, 'isSet', false);
                });
                //===========反写外部表单内容==========
                this.table.data.push(tempData);
                return this.$message({
                type: 'success',
                message: "新增成功！"
              });
              }else{
                this.table.data.splice(this.dialogData.localID,1,tempData);
                return this.$message({
                type: 'success',
                message: "修改成功！"
              });
              }
            }).catch((err) => {
              console.log(err);
            });
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
            console.log(this.dialogData.localID,error);
            if(null !== this.table.currentRow.id) this.table.data.splice(this.dialogData.localID, 1);
            this.$message({
              type: 'error',
              message: "保存失败！"
            });
          });
      }else{
        return this.$set(this.dialogData, 'isEdit', true);
      }
    },
    currentRowChangeDialog(rowContent,index,isCancel){
      //点击修改、保存,判断是否已经保存所有操作
      // console.log(rowContent,index)
      for (let item of this.dialogData.table.data) {
        // console.log(item.isNew , rowContent.isNew)
        if ((item.isSet && (item.id != rowContent.id)) || ((item.isSet && this.dialogData.isAdd && (item.isNew != rowContent.isNew)))) return this.$message.warning("请先保存当前编辑项!");
        if (item.isSet && (item.id != rowContent.id) && (item.kind === rowContent.kind)) return this.$message.warning("该档名称价已经存在!");
        // console.log(this.dialogData.isAdd, item.isNew, this.dialogData.table.currentRow.isNew, item.kind, this.dialogData.table.currentRow.kind)
        if (this.dialogData.isAdd) {
          // console.log(item.isSet)
          console.log(item.isNew ,this.dialogData.table.currentRow.isNew ,item.kind , this.dialogData.table.currentRow.kind)
          if (item.isSet && (item.isNew !=rowContent.isNew) && (item.isNew != this.dialogData.table.currentRow.isNew)) {
            return this.$message.warning("请先保存当前编辑项!");
          } else if (!isCancel && (item.isNew != this.dialogData.table.currentRow.isNew) && (item.kind === this.dialogData.table.currentRow.kind)) {
            return this.$message.warning("该档名称价已经存在!");
          } 
        }
      }
      //是否为取消操作
      if (isCancel) {
        if (this.dialogData.table.currentRow.isSet && (null === this.dialogData.table.currentRow.id)) return this.dialogData.table.data.splice(index, 1);
        rowContent.isSet = !rowContent.isSet;
        return this.$set(this.dialogData.table.data, index, rowContent)
      }
      if (rowContent.isSet) {
        
        if (this.dialogData.isAdd){
          // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));
          if(InputCheck.namecheck(this.dialogData.table.currentRow.name)) return this.$message.warning("报价名称不能为空或空格!");
          if(this.dialogData.isAdd){
            let tempData = JSON.parse(JSON.stringify({"id": null, "kind": this.dialogData.table.currentRow.kind, "price": this.dialogData.table.currentRow.price, "isSet": false, "isNew": this.dialogData.table.currentRow.isNew,}));
            console.log(tempData)
            this.dialogData.table.countAll+=1;
            this.dialogData.table.data.splice(index,1,tempData)
            return 0;
          }
        }else{
          
          var params = new URLSearchParams();
          // if(null !== this.table.currentRow.id){
          //   params.append("pk",this.dialogData.table.currentRow.id);
          //   params.append("req_method",'UPDATE');
          // }else{
          //   params.append("req_method",'ADD');
          // }
          let data2Add = {0: JSON.stringify({
            "line_price_fk": this.dialogData.contentId,
            "local_agency_fk": Sstorage.get('localAgencyFk'),
            "token": Sstorage.get('tokenID'),
            "user_id":Sstorage.get('userID'),
            "id": null,
            "kind": this.dialogData.table.currentRow.kind,
            "price": this.dialogData.table.currentRow.price,
            }),};

          params.append("req_method",'ADD');
          // paramsData.append("data_to_add",JSON.stringify(this.dialogData.table.data));
          params.append("data_to_add",JSON.stringify(data2Add));
          console.log(params.getAll("req_method"));
          console.log(params.getAll("data_to_add"));
          Axios.post(this.refApi, params).then((response) => {
            // console.log(response.data.added_data[0])
            if(1 == response.data.added_num && 0 == response.data.failed_num){
              let tempData = JSON.parse(JSON.stringify(response.data.added_data[0]));
              this.$set(tempData, 'isSet', false);
              if(3 > this.dialogData.table.countAll) {
                // console.log(this.dialogData.table.countAll);
                Product.getOne(this.dialogData.contentId).then((resp) => {
                  console.log(resp);
                  let tempLine = {
                    'id': resp.result.line_price.id,
                    'name': resp.result.line_price.name,
                    'remark': resp.result.line_price.remark,
                    'local_agency_fk': resp.result.line_price.local_agency_fk,
                    'detail': resp.result.line_price.detail,
                    'isSet': false,
                  }
                  resp.result.ref_prices.forEach((item, tempIndex) => {
                    let tempContent = item.kind + ':' + item.price;
                    tempLine['top3_ref_data' + tempIndex] = tempContent;
                  });
                  console.log(this.dialogData.localID, "++++++++*********")
                  this.table.data.splice(this.dialogData.localID,1,tempLine);
                  //TODO:继续完成。
                }).catch((err) => {
                  console.log(err);
                });
              }
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
        }
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
      let tempAddData = {"id": null, "kind": "", "price": "", "isSet": true, "isNew":new Date().getTime(),};
      this.dialogData.table.data.push(JSON.parse(JSON.stringify(tempAddData)));
      this.dialogData.table.currentRow = JSON.parse(JSON.stringify(tempAddData));
      // console.log(this.table.data)
    },
    //目前可能不需要删除功能？？？
    doDelDialog(rowContent, index){
      this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(rowContent, index);
        // if (this.dialogData.isAdd) {
        if (null === rowContent.id) {
          this.dialogData.table.data.splice(index, 1);
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          return 0;
        } 
        var params = new URLSearchParams();
        params.append("req_method","DELETE");
        // params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        params.append("pk",rowContent.id);
        params.append("user_id",Sstorage.get('tokenID'));
        params.append("token",Sstorage.get('tokenID'));
        
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
    updateOne(contentID, localID, isAdd){

      console.log(contentID,localID);
      Axios.post(this.api, params).then((response)=>{
        console.log(response,contentID,localID);
        if (response.data.status_flag){
          console.log("--------")
          let tempData = {"id": response.data.result.line_price.id, 
                        "name": response.data.result.line_price.name,
                        "remark": response.data.result.line_price.remark,
                        "local_agency_fk": response.data.result.line_price.local_agency_fk,
                        "isSet": false,
                        };
          console.log(tempData)
          response.data.result.ref_prices.forEach(item=>{
            console.log("item:", item, "index:", index);
          })
          console.log("--------")
          // top3_ref_data0: "gtrgt:543.0"
          // top3_ref_data1: "g3gg3:4545.0"
          // top3_ref_data2: "456gfgdg:56655.0"
          return 0;
          this.table.countAll += 1;
          if(isAdd){
            this.table.data.append(tempData);
          } else {
            this.table.data.splice(localID, 1, tempData);
          }
        }

        // this.dialogData.Content = JSON.parse(JSON.stringify(response.data.result.line_price));
        // // this.dialogData._Content = this.dialogData.Content;
        // this.dialogData._Content = JSON.parse(JSON.stringify(this.dialogData.Content));

        // this.dialogData.table.data = JSON.parse(JSON.stringify(response.data.result.ref_prices));
        // this.dialogData.table.data.forEach(item => {
        //   this.$set(item, 'isSet', false);
        // });
      }).catch((error)=>{
        console.log(error);
      })
    }
  },
  mounted() {
    // var list = JSON.parse(localStorage.getItem('list'));
    
    // const api='http://127.0.0.1:9090/acct/agencies/';
    Product.get().then((data) => {
      this.table.countAll = data.item_num
      this.table.data = data.result;
      this.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      this.table.data = JSON.parse(JSON.stringify(this.table.data));
      // console.log(this.table.data)
    }).catch((error) => {
      console.log(error);
    });
  }
}
</script>

<style scoped>
.el-scrollbar__wrap {
  overflow-x: hidden;
}
</style>