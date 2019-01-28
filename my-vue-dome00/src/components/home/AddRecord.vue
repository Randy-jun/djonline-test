<template>
  <el-row>
    <el-row :gutter=20 type="flex" justify="space-between">
      <el-col :span=8>
        <span >出团记录ID：{{content.data.id}}</span>
      </el-col>
      <el-col :span=8>
        <span>单据状态：{{content.data.status}}</span>
      </el-col>
      <el-col :span=4>
        <el-button type="primary" @click="flashTable.isShow = !flashTable.isShow">查看结算信息</el-button>
      </el-col>
      <el-col :span=2>
        <el-button>保存</el-button>
      </el-col>
      <el-col :span=2>
        <el-button>取消</el-button>
      </el-col>
    </el-row>
    <el-row :gutter=20 type="flex" justify="space-between">
      <el-col :span=6>
        <span >地接社名称：{{content.data.djName}}</span>
      </el-col>
      <el-col :span=6>
        <span>组团社名称：{{content.data.ztName}}</span>
      </el-col>
      <el-col :span=6>
        <span>线路名称：{{content.data.product}}</span>
      </el-col>
      <el-col :span=6>
        <span>出团日期：{{content.data.date}}</span>
      </el-col>
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
    <el-row>
      <el-tabs type="card" v-model="table.activeTableName" @tab-click="handleClick">
        <el-tab-pane label="基础业务" name="first">
          <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
            <el-table-column fixed type="index" width="100"></el-table-column>
            <el-table-column v-for="(value, key) in table.columns1" :prop="value.field" :label="value.title" :sortable="value.sortable">
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
          <el-row>
            <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAdd()">添加游客</el-button>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="调拨业务" name="second">
          <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
            <el-table-column fixed type="index" width="100"></el-table-column>
            <el-table-column v-for="(value, key) in table.columns2" :prop="value.field" :label="value.title" :sortable="value.sortable">
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
        </el-tab-pane>
        <el-tab-pane label="代收业务" name="third">
          <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
            <el-table-column fixed type="index" width="100"></el-table-column>
            <el-table-column v-for="(value, key) in table.columns3" :prop="value.field" :label="value.title" :sortable="value.sortable">
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
        </el-tab-pane>
      </el-tabs>
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
      content:{
        data:{
            id:"6868-2219-SQ85-6988",
            status:"已审核",
            djName:"百恒国际旅行社",
            ztName:"光大旅行社",
            product:"西安北线二日游（旺季）",
            date:"2019年01月01日",
          },
        },
      table: {
        activeTableName:'first',
        countAll: null,
        currentRow: null,//选中行  
        columns1:[
          { field: "name", title: "姓名", width: 150, isEdit: true, sortable: true },
          { field: "count", title: "人数", width: 150, isEdit: true, sortable: true },
          { field: "refer_price", title: "参考报价", width: 320, isEdit: true, sortable: true },
          { field: "final_price", title: "最终报价", width: 320, isEdit: true, sortable: true },
          { field: "modify_price", title: "修正金额", width: 320, isEdit: true, sortable: true },
          { field: "modify_price_remark", title: "修正报价", width: 320, isEdit: true, sortable: true },
        ], 
        columns2:[
          { field: "name", title: "姓名", width: 150, isEdit: true, sortable: true },
          { field: "count", title: "人数", width: 150, isEdit: true, sortable: true },
          { field: "final_price", title: "最终报价", width: 320, isEdit: true, sortable: true },
          { field: "allocate_price", title: "调拨金额", width: 320, isEdit: true, sortable: true },
          { field: "allocate_group", title: "调拨单位", width: 320, isEdit: true, sortable: true },
          { field: "allocate_remark", title: "调拨备注", width: 320, isEdit: true, sortable: true },
        ], 
        columns3:[
          { field: "name", title: "姓名", width: 150, isEdit: true, sortable: true },
          { field: "count", title: "人数", width: 150, isEdit: true, sortable: true },
          { field: "final_price", title: "最终报价", width: 320, isEdit: true, sortable: true },
          { field: "deputy_price", title: "代收金额", width: 320, isEdit: true, sortable: true },
          { field: "deputy_group", title: "代收单位", width: 320, isEdit: true, sortable: true },
          { field: "deputy_remark", title: "代收备注", width: 320, isEdit: true, sortable: true },
        ], 
        data: [
           {
            name:"甲",
            count:1,
            refer_price:"成人:270",
            final_price:280,
            modify_price:+10,
            modify_price_remark:"含餐",
            allocate_price:null,
            allocate_group:null,
            allocate_remark:null,
            deputy_price:null,
            deputy_group:null,
            deputy_remark:null,
          },
          {
            name:"乙",
            count:1,
            refer_price:"车住:160",
            final_price:190,
            modify_price:+30,
            modify_price_remark:"法门寺电瓶车",
            allocate_price:null,
            allocate_group:null,
            allocate_remark:null,
            deputy_price:20,
            deputy_group:"百恒国际旅行社",
            deputy_remark:"车费",
          },
          {
            name:"丙",
            count:1,
            refer_price:"车费:130",
            final_price:140,
            modify_price:+10,
            modify_price_remark:"含餐",
            allocate_price:100,
            allocate_group:"大唐旅行社",
            allocate_remark:null,
            deputy_price:20,
            deputy_group:"大唐旅行社",
            deputy_remark:"车费",
          },
          {
            name:"丁",
            count:10,
            refer_price:"成人:270",
            final_price:2800,
            modify_price:+100,
            modify_price_remark:"含餐",
            allocate_price:2000,
            allocate_group:"大唐旅行社",
            allocate_remark:null,
            deputy_price:null,
            deputy_group:null,
            deputy_remark:null,
          },
          {
            name:"戊",
            count:5,
            refer_price:"成人:270",
            final_price:1150,
            modify_price:-200,
            modify_price_remark:"优惠",
            allocate_price:1000,
            allocate_group:"中国青年旅行社",
            allocate_remark:null,
            deputy_price:100,
            deputy_group:"中国青年旅行社",
            deputy_remark:"车费",
          },
        ],
      },
      api:'http://127.0.0.1:9090/acct/agencies/',
      currentPage4: 4,
      flashTable:{
        isShow:false,
        columns:[
          { field: "payee", title: "收款方", width: 200, isEdit: true, sortable: true },
          { field: "payer", title: "付款方", width: 200, isEdit: true, sortable: true },
          { field: "amount", title: "结算金额", width: 200, isEdit: true, sortable: true },
          { field: "business_type", title: "业务类型", width: 200, isEdit: true, sortable: true },
        ],
        data:[
          {
            payee:"百恒国际旅行社",
            payer:"光大旅行社",
            amount:4420,
            business_type:"基础业务",
          },
          {
            payee:"百恒国际旅行社",
            payer:"游客",
            amount:20,
            business_type:"代收业务",
          },
          {
            payee:"大唐旅行社",
            payer:"百恒国际旅行社",
            amount:2080,
            business_type:"调拨业务",
          },
          {
            payee:"中国青年旅行社",
            payer:"百恒国际旅行社",
            amount:900,
            business_type:"调拨业务",
          },
          {
            payee:"大唐旅行社",
            payer:"游客",
            amount:20,
            business_type:"第三方代收业务",
          },
          {
            payee:"中国青年旅行社",
            payer:"游客",
            amount:100,
            business_type:"第三方代收业务",
          },
        ],
      },
    }
  },
  components: {
    // CustomeAlert,
  },
  methods: {
    handleClick(tab, event) {
        console.log(tab, event);
    },
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
      for (let item of this.table.data) {
        if (item.isSet) return this.$message.warning("请先保存当前编辑项!");
      }
      let tempAddData = {id: null, "name": "", "remark": "", "isSet": true,};
      this.table.data.push(tempAddData);
      this.table.currentRow = JSON.parse(JSON.stringify(tempAddData));
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
    }
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
      console.log(response)
      this.table.countAll = response.data.item_num;
      this.table.countAll = 0;
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
.el-row {
  margin-top: 5px;
  margin-bottom: 15px;
}
</style>