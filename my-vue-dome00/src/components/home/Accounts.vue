<template>
  <el-row>
    <!-- <el-row style="height:750px"> -->
    <el-row type="flex">
      <span><h4>往来查询：百恒国际旅行社<i class="el-icon-refresh"></i>光大旅行社</h4></span>
    </el-row>
    <el-row type="flex">
      <span>出团时间：不限|今天|本周|本月</span>
      <el-date-picker
        v-model="dateValue"
        type="daterange"
        align="right"
        unlink-panels
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
        :picker-options="pickerOptions2">
      </el-date-picker>
    </el-row>
    <el-row type="flex">
      <span>单据状态：不限|无|已审核|已结算</span>
    </el-row>
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
              <span class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="flashTable.isShow = !flashTable.isShow">联查相关单据</span>
            </template>
          </el-table-column>
        </el-table>
      </el-scrollbar>
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
      <el-collapse-transition>
        <el-row v-show="flashTable.isShow">
          <el-table :data="flashTable.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
            <el-table-column fixed type="index" width="150"></el-table-column>
            <el-table-column v-for="(value, key) in flashTable.columns" :prop="value.field" :label="value.title" :sortable="value.sortable">
              <template slot-scope="scope">
                <span v-if="scope.row.isSet">
                  <span v-if='value.isEdit'><el-input size="mini" placeholder="请输入内容" v-model="table.currentRow[value.field]"></el-input></span>
                  <span v-else>{{scope.row[value.field]}}</span>
                </span>
                <span v-else>{{scope.row[value.field]}}</span>
              </template>
            </el-table-column>
          </el-table>
        </el-row>
      </el-collapse-transition>
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
      dateValue:null,
      table: {
        countAll: null,
        currentRow: null,//选中行   
        columns:[
          { field: "payee", title: "收款方", width: 200, isEdit: true, sortable: true },
          { field: "payer", title: "付款方", width: 200, isEdit: true, sortable: true },
          { field: "product", title: "线路名称", width: 200, isEdit: true, sortable: true },
          { field: "amount", title: "结算金额", width: 200, isEdit: true, sortable: true },
          { field: "business_type", title: "业务类型", width: 200, isEdit: true, sortable: true },
        ],
        // tempData: [],
        data: [
          {
              payee:"百恒国际旅行社",
              payer:"光大旅行社",
              product:"西安北线三日游（旺季）",
              amount:4420,
              business_type:"基础业务",
          },
          {
              payee:"百恒国际旅行社",
              payer:"光大旅行社",
              product:"西安东线二日游（旺季）",
              amount:2000,
              business_type:"基础业务",
          },
          {
              payee:"百恒国际旅行社",
              payer:"光大旅行社",
              product:"西安华山一日游（旺季）",
              amount:2080,
              business_type:"基础业务",
          },
          {
              payee:"光大旅行社",
              payer:"百恒国际旅行社",
              product:"西安市内二日游（旺季）",
              amount:900,
              business_type:"调拨业务",
          },
          {
              payee:"光大旅行社",
              payer:"百恒国际旅行社",
              product:"西安华山一日游（旺季）",
              amount:200,
              business_type:"调拨业务",
          },
          {
              payee:"光大旅行社",
              payer:"百恒国际旅行社",
              product:"西安兵马俑一日游（旺季）",
              amount:100,
              business_type:"调拨业务",
          },
        ],
      },
      api:'http://127.0.0.1:9090/acct/lineprices/',
      refApi:'http://127.0.0.1:9090/acct/refprices/',
      currentPage4: 4,
      flashTable:{
        isShow:false,
        columns:[
          { field: "id", title: "编号", width: 150, isEdit: false, sortable: true },
          { field: "group", title: "组织名称", width: 320, isEdit: true, sortable: true },
          { field: "product", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "date", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "count", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "status", title: "备注", width: 320, isEdit: true, sortable: false },
        ],
        data:[
          {
            id:"2019-0922-0001",
            group:"光大旅行社",
            product:"西安北线二日游（旺季）",
            date:"2019-09-22",
            count:18,
            status:"",
          },
          {
            id:"2019-0921-0001",
            group:"光大旅行社",
            product:"西安北线二日游（旺季）",
            date:"2019-09-21",
            count:20,
            status:"",
          },
          {
            id:"2019-0922-0021",
            group:"光大旅行社",
            product:"西安北线二日游（旺季）",
            date:"2019-06-22",
            count:16,
            status:"已结算",
          },
          {
            id:"2019-0922-0201",
            group:"西安康辉旅行社",
            product:"西安东线三日游",
            date:"2019-04-24",
            count:23,
            status:"已结算",
          },
          {
            id:"2019-0612-0001",
            group:"中国青年旅行社",
            product:"西安市内一日游",
            date:"2019-07-12",
            count:9,
            status:"",
          },
        ],
      },
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
      this.dialogData.ContentId = rowContent.id;
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
      this.dialogData.ContentId = null;
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

        Axios.post(this.refApi, params).then((response)=>{
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
            this.$message({
              type: 'warning',
              message: "每条线路至少有一个默认报价！"
            });
            return 0;
          }
        }

        params.append("name",this.dialogData._Content.name);
        params.append("remark",this.dialogData._Content.remark);
        params.append("detail",this.dialogData._Content.detail);
        
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));
        
        console.log(params.getAll("pk"))
        Axios.post(this.api, params).then((response)=>{
          console.log(response);
          if(response.data.status_flag){
            
            let tempData = response.data.result;
            this.$set(tempData, 'isSet', false);
            
            if(null !== this.dialogData.ContentId){
              this.table.data.splice(this.dialogData.localID,1,tempData);
              this.$message({
                type: 'success',
                message: "修改成功！"
              });
            }else{
              this.table.countAll+=1;
              this.table.data.splice(this.dialogData.localID,1,tempData);
              this.dialogData.ContentId = tempData.id;

              let data2Add = {};
              this.dialogData.table.data.forEach((item,index) => {
                this.$set(item, 'user_id',Sstorage.get('userID'));
                this.$set(item, 'token',Sstorage.get('tokenID'));
                this.$set(item, 'local_agency_fk',Sstorage.get('localAgencyFk'));
                this.$set(item, 'line_price_fk', this.dialogData.ContentId);
                data2Add[index] = JSON.stringify(item);
              });

              var paramsData = new URLSearchParams();
              paramsData.append("req_method",'ADD');
              // paramsData.append("data_to_add",JSON.stringify(this.dialogData.table.data));
              paramsData.append("data_to_add",JSON.stringify(data2Add));
              // console.log(paramsData.getAll("data_to_add"));
              Axios.post(this.refApi , paramsData).then((response)=>{
                console.log(response);
                if(0 == response.data.failed_num){
                  this.$message({
                    type: 'success',
                    message: "添加成功！"
                  });
                  //this.$set(this.dialogData, 'tableVisible', false);
                  this.dialogData.isAdd = false;
                  this.dialogData.isEdit = false;
                  // this.dialogData.ContentId = rowContent.id;
                  // this.dialogData.localID = index;
                  var getOneParams = new URLSearchParams();
                  // params.append("req_method","GET_SINGLE");
                  getOneParams.append("req_method","GETONE");
                  
                  getOneParams.append("pk",this.dialogData.ContentId);
                  
                  getOneParams.append("tokenID",Sstorage.get('tokenID'));
                  getOneParams.append("local_agency_fk",Sstorage.get('localAgencyFk'));

                  Axios.post(this.api, getOneParams).then((response)=>{
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
                }else{
                  this.$message({
                    type: 'error',
                    message: "添加失败！"
                  });
                }
              })
              .catch((error)=>{
                this.$message({
                  type: 'error',
                  message: "保存失败！"
                });
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
        console.log("else-out")
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
          console.log("else")
          var params = new URLSearchParams();
          // if(null !== this.table.currentRow.id){
          //   params.append("pk",this.dialogData.table.currentRow.id);
          //   params.append("req_method",'UPDATE');
          // }else{
          //   params.append("req_method",'ADD');
          // }
          let data2Add = {0: JSON.stringify({
            "line_price_fk": this.dialogData.ContentId,
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
          Axios.post(this.refApi, params).then((response)=>{
            console.log(response);
            return 0;
            ```
            在单条线路报价新增成功后，希望获得新的返回值形式，例如之前的组织机构新增后返回的结构，以便添加后在前台及时更新显示。
            ```
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
      // this.table.countAll = response.data.item_num
      // this.table.data = response.data.result;
      // // this.table.countAll=response.data.item_num;
      // this.table.data.forEach(item => {
      //   this.$set(item, 'isSet', false);
      // });
      // this.table.data = JSON.parse(JSON.stringify(this.table.data));
      // console.log(this.table.data);
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