<template>
<el-row :gutter=20>
  <el-row v-if="0 == table.countAll">
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
      <el-row :gutter="10" class="filter">
        <el-col :span="2"><span>接送时间</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">不限</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">今天</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">明天</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">本周</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">本月</span></el-col>
        <el-col :span="3">
          <el-date-picker
            v-model="dateValue"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期">
          </el-date-picker>
        </el-col>
      </el-row>
      <el-row :gutter="10" class="filter">
        <el-col :span="2"><span>订单类型</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">不限</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">接机</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">送机</span></el-col>
      </el-row>
      <el-row :gutter="10" class="filter">
        <el-col :span="2"><span>订单状态</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">不限</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">暂存</span></el-col>
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">已提交</span></el-col>
        <!-- <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">受理中</span></el-col> -->
        <el-col :span="1"><span class="el-tag el-tag--mini" style="cursor: pointer;">已结算</span></el-col>
      </el-row>
      <el-row :gutter="10" class="filter">
        <el-col :span="4">
          <el-button-group>
            <el-button type="primary" style="cursor: pointer;" v-on:click="doAdd()">新增订单</el-button>
            <el-button v-if="buttonShow" type="danger" style="cursor: pointer;">删除订单</el-button>
          </el-button-group>
        </el-col>
        <!-- <el-col :span="4">
          <el-button-group>
            <el-button type="success" style="cursor: pointer;">受理订单</el-button>
            <el-button type="warning" style="cursor: pointer;">打回订单</el-button>
          </el-button-group>
        </el-col> -->
        <el-col :span="4" v-if="buttonShow">
          <el-button-group>
            <el-button type="success" style="cursor: pointer;">确认结算</el-button>
            <el-button type="danger" style="cursor: pointer;">取消结算</el-button>
          </el-button-group>
        </el-col>
        <el-col :span="2" :push="12" v-if="buttonShow">
          <el-button type="primary" style="cursor: pointer;" v-on:click="exportOrder()">导出订单</el-button>
        </el-col>
      </el-row>
      <el-row>
    <!-- <el-col :span=24> -->
      <!-- <el-scrollbar style="height:100%"> -->
        <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
          <el-table-column type="selection" width="55" @selection-change="handleSelectionChange"></el-table-column>
          <el-table-column fixed type="index" width="20"></el-table-column>
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
          <el-table-column align='center' width="100" label="状态">
            <template slot-scope="scope">
              <span v-if="scope.row.isSet">
                <el-select size="mini" @change="statusChange" v-model="scope.row.statuscode" >
                  <el-option v-for="item in statusList" :key="item.value" :label="item.label" :value="item.value">
                  </el-option>
                </el-select>
              </span>
              <span v-else class="el-tag el-tag--mini">{{scope.row.statusflag}}</span>
            </template>
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="150">
            <template slot-scope="scope">
              <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="showOrder(scope.row,scope.$index)">详细</span>
              <span class="el-tag el-tag--danger el-tag--mini" v-on:click="doDel(scope.row,scope.$index)" style="cursor: pointer;">删除</span>
            </template>
          </el-table-column>
        </el-table>
      <!-- </el-scrollbar> -->
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
import UserInfo from '@/module/userinfo.js';
import Sstorage from '@/module/sstorage.js';

export default {
  name: 'OrderList',
  props: {
    msg: String
  },
  data() {
    return {
      checkedList:[],
      statusList: [
            {value: 0,label: '暂存'},
            {value: 1,label: '已提交'},
            {value: 2,label: '已结算'},
          ],
      buttonShow:false,
      dateValue:null,
      value:true,
      table: {
        countAll: null,
        currentRow: null,//选中行   
        columns: [
          // { field: "id", title: "编号", width: 160, isEdit: true, sortable: false },
          { field: "user", title: "提交人员", width: 800, isEdit: true, sortable: false },
          { field: "linkman", title: "联系人", width: 80, isEdit: true, sortable: false },
          { field: "phone", title: "联系电话", width: 330, isEdit: true, sortable: false },
          { field: "count", title: "人数", width: 10, isEdit: true, sortable: false },
          { field: "charge", title: "收费金额", width: 15, isEdit: true, sortable: false },
          { field: "address", title: "接送地址", width: 200, isEdit: true, sortable: false },
          { field: "group", title: "组织", width: 200, isEdit: true, sortable: false },
          { field: "name", title: "订单类型", width: 200, isEdit: true, sortable: false },
          { field: "number", title: "航班时间", width: 200, isEdit: true, sortable: false },
          { field: "leavetime", title: "上机时间", width: 200, isEdit: true, sortable: false },
          { field: "arrivetime", title: "下机时间", width: 200, isEdit: true, sortable: false },
          { field: "terminal", title: "航站楼", width: 200, isEdit: true, sortable: false },
          { field: "remark", title: "备注", width: 220, isEdit: true, sortable: false },
        ],
        // tempData: [],
        data: [],
      },
      currentPage4: 4,
    }
  },
  components: {
    // CustomeAlert,
  },
  methods: {
    handleSelectionChange(){
      console.log(value)
    },
    statusChange(value){
      let obj = {};
      obj = this.statusList.find((item)=>{//这里的selectList就是上面遍历的数据源
          return item.value === value;//筛选出匹配数据
      });
      // console.log(obj)
      this.table.currentRow.statuscode = obj.value;
      this.table.currentRow.statusflag = obj.label;
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
          Order.update(this.table.currentRow).then((response) => {
            this.table.data.splice(index,1,response);
            this.$message({
              type: 'success',
              message: "修改成功！"
            });
          }).catch((error) => {
            console.log(error);
            this.$message({
              type: 'error',
              message: "修改失败！"
            });
          });
        }else{
          Order.insert(this.table.currentRow).then((response) => {
            this.table.countAll+=1;
            this.table.data.splice(index,1,response);
            this.$message({
              type: 'success',
              message: "添加成功！"
            });
          }).catch((error) => {
            console.log(error);
            this.$message({
              type: 'error',
              message: "添加失败！"
            });
          });
        }
      }else{
        this.table.currentRow = JSON.parse(JSON.stringify(rowContent));
        // this.table.currentRow = rowContent;
        rowContent.isSet = true;
        // this.$set(this.table.data, index, rowContent);
        this.table.data.splice(index, 1, rowContent)
      }
    },
    doAdd() {
      Sstorage.set('orderAdd', true);
      var orderdetail = "/home/order";
      // console.log(goadd)
      this.$router.replace({ path: orderdetail })
    },
    showOrder(rowContent, index){
      console.log("detail")
      Sstorage.set('orderAdd', false);
      Sstorage.set('orderID', 1);
      // Sstorage.set('orderID', rowContent.id);
      var orderdetail = "/home/order";
      // console.log(goadd)
      this.$router.replace({ path: orderdetail })
    },
    doDel(rowContent, index){
      this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(rowContent, index);
       Order.delete(rowContent.id).then((response) => {
          this.table.countAll-=1;
          this.table.data.splice(index,1);
          this.$message({
            type: 'success',
            message: "删除成功！"
          });
        }).catch((error) => {
          console.log(error);
          this.$message({
            type: 'error',
            message: "删除失败！"
          });
        });
      }).catch((error) => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
    },
    exportOrder(){
      window.open("http://60.205.204.124:8080/order/export/")
      // Order.exportOrder((response) => {
      //   console.log("exportOrder");
      // }).catch((error) => {
      //   console.log(error);
      // })
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    }
  },
  mounted() {
    Sstorage.remove('orderID');
    Sstorage.remove('orderAdd');
    
    Order.get().then((response) => {
      console.log(response)
      // this.table.countAll = response.data.item_num;
      // this.table.countAll = 0;
      // this.table.data = response.data.result;
      this.table.countAll=JSON.parse(JSON.stringify(response.item_num));
      this.table.data=JSON.parse(JSON.stringify(response.data));
      this.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      console.log(this.table.countAll);
      console.log(this.table.data);
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
    });
    UserInfo.getLevel().then((response) => {
      console.log(response.data);
      if('0' == response) this.buttonShow = true;
    }).catch((error) => {
      console.log(error);
    })
  }
}
</script>

<style>
.el-scrollbar__wrap {
  overflow-x: hidden;
}
.filter {
  line-height: 20px;
  align-self: auto;
}
</style>