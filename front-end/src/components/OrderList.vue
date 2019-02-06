<template>
<el-row :gutter=20>
  <el-row v-if="0 !== table.countAll">
    <el-col>
      <el-card shadow="hover" class="box-card">
        <div slot="header" class="clearfix">
          <span><h4>订单记录毛都没有，来不及解释了，赶快上车！</h4></span>
        </div>
        <div>
          <el-button v-on:click="doAdd()" >
            <i class="el-icon-plus"></i>
            <span>新增订单</span>
          </el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <el-row v-else>
    <!-- <el-row style="height:750px"> -->
      <el-row type="flex">
        <span>出团时间：不限|今天|本周|本月</span>
        <el-date-picker
          v-model="dateValue"
          type="daterange"
          align="right"
          unlink-panels
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期">
        </el-date-picker>
      </el-row>
      <el-row type="flex">
        <span>单据状态：不限|无|已审核|已结算</span>
      </el-row>
      <el-row>
    <!-- <el-col :span=24> -->
      <!-- <el-scrollbar style="height:100%"> -->
        <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <el-table-column fixed type="index" width="100"></el-table-column>
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
          <el-table-column fixed="right" label="操作" width="150">
            <template slot-scope="scope">
              <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,false)">
                  {{scope.row.isSet?'保存':"修改"}}
              </span>
              <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" v-on:click="doDel(scope.row,scope.$index)" style="cursor: pointer;">删除</span>
              <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,true)">取消</span>
            </template>
          </el-table-column>
        </el-table>
      <!-- </el-scrollbar> -->
    </el-row>
    <el-row>
      <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAdd()">新增出团记录</el-button>
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
  </el-row>
</el-row>
</template>

<script>

import Order from '@/module/order.js';
import InputCheck from '@/module/inputcheck.js';
// import CustomeAlert from  '@/components/sysinfo/CustomAlert.vue';

export default {
  name: 'OrderList',
  props: {
    msg: String
  },
  data() {
    return {
      dateValue:null,
      value:true,
      table: {
        countAll: 0,
        currentRow: null,//选中行   
        columns: [
          { field: "id", title: "编号", width: 150, isEdit: false, sortable: true },
          { field: "group", title: "组织名称", width: 320, isEdit: true, sortable: true },
          { field: "product", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "date", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "count", title: "备注", width: 320, isEdit: true, sortable: false },
          { field: "status", title: "备注", width: 320, isEdit: true, sortable: false },
        ],
        // tempData: [],
        data: [
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
      api:'http://127.0.0.1:9090/acct/agencies/',
      currentPage4: 4,
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
    //   this.table.currentRow = selectRow;
    //   console.log(this.table.currentRow);
    // },
    currentRowChange(rowContent,index,isCancel){
      //点击修改、保存,判断是否已经保存所有操作
      // console.log(rowContent, index, isCancel)
      for (let item of this.table.data) {
        if (item.isSet && (item.id != rowContent.id)) {
          this.$message.warning("请先保存当前编辑项!");
          return false;
        }
      }
      //是否为取消操作
      if (isCancel) {
        if (null === this.table.currentRow.id) return this.table.data.splice(index, 1);
        rowContent.isSet = !rowContent.isSet;
        return this.$set(this.table.data, index, rowContent)
      }

      if (rowContent.isSet) {
        // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));

        if(InputCheck.namecheck(this.table.currentRow.name)) return this.$message.warning("组织名称不能为空或空格!");

        var params = new URLSearchParams();
        
        if(null !== this.table.currentRow.id){
          params.append("pk",this.table.currentRow.id);
          params.append("req_method",'UPDATE');
        }else{
          params.append("req_method",'ADD');
        }
        params.append("name",this.table.currentRow.name);
        params.append("remark",this.table.currentRow.remark);
        
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
        this.table.data.splice(index, 1, rowContent)
      }
    },
    doAdd(){
      var goadd = "/home/addorder";
      // console.log(goadd)
      this.$router.replace({ path: goadd })
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
    }
  },
  mounted() {
    // var list = JSON.parse(localStorage.getItem('list'));
    
    // const api='http://127.0.0.1:9090/acct/agencies/';
    
    Order.get().then((response) => {
      console.log(response)
      this.table.countAll = response.data.item_num;
      // this.table.countAll = 0;
      // this.table.data = response.data.result;
      // this.table.countAll=response.data.item_num;
      this.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      // this.table.data = JSON.parse(JSON.stringify(this.table.data));
      // console.log(this.table.data);s
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

<style>
.el-scrollbar__wrap {
  overflow-x: hidden;
}
</style>