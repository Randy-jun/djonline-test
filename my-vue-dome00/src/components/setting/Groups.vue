<template>
  <el-row>
    <el-row>
    <!-- <el-col :span=24> -->
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
            <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,false)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" v-on:click="del(scope.row,scope.$index)" style="cursor: pointer;">删除</span>
            <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,true)">取消</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <el-row>
      <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAdd()">添加新的组织机构</el-button>
    </el-row>
    <el-row>
      <el-pagination  
        v-on:size-change="handleSizeChange"
        v-on:current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="400">
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
    //   this.group.currentRow = selectRow;
    //   console.log(this.group.currentRow);
    // },
    currentRowChange(rowContent,index,isCancel){
      //点击修改、保存,判断是否已经保存所有操作
      // console.log(rowContent, index, isCancel)
      for (let item of this.group.data) {
        if (item.isSet && (item.id != rowContent.id)) {
          this.$message.warning("请先保存当前编辑项!");
          return false;
        }
      }
      //是否为取消操作
      if (isCancel) {
        if (null === this.group.currentRow.id) return this.group.data.splice(index, 1);
        rowContent.isSet = !rowContent.isSet;
        return this.$set(this.group.data, index, rowContent)
      }

      if (rowContent.isSet) {
        // let tempData = JSON.parse(JSON.stringify(this.group.currentRow));

        if(InputCheck.namecheck(this.group.currentRow.name)) return this.$message.warning("组织名称不能为空或空格!");

        var params = new URLSearchParams();
        
        if(null !== this.group.currentRow.id){
          params.append("pk",this.group.currentRow.id);
          params.append("req_method",'UPDATE');
        }else{
          params.append("req_method",'ADD');
        }
        params.append("name",this.group.currentRow.name);
        params.append("remark",this.group.currentRow.remark);
        
        params.append("tokenID",Sstorage.get('tokenID'));
        params.append("local_agency_fk",Sstorage.get('localAgencyFk'));

        Axios.post(this.api, params).then((response)=>{
          if(response.data.status_flag){
            console.log(response);
            let tempData = response.data.result;
            console.log(tempData);
            this.$set(tempData, 'isSet', false);
            if(null !== this.group.currentRow.id){
              this.group.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "修改成功！"
              });
            }else{
              this.count_all+=1;
              this.group.data.splice(index,1,tempData);
              this.$message({
                type: 'success',
                message: "添加成功！"
              });
            }
          }else{
            console.log(response);

            if(null !== this.group.currentRow.id){
              this.$message({
                type: 'error',
                message: "修改失败！"
              });
            }else{
              // this.group.data.splice(index, 1);
              this.$message({
                type: 'error',
                message: "添加失败！"
              });
            }
          }})
          .catch((error)=>{
            console.log(error);
            if(null !== this.group.currentRow.id) this.group.data.splice(index, 1);
            this.$message({
              type: 'error',
              message: "保存失败！"
            });
          });
        /*
        for (let k in tempData) rowContent[k] = tempData[k];
        console.log(this.group.data)
        return 0;
        */
        // this.$message({
        //     type: 'success',
        //     message: "保存成功!"
        // });
        //然后这边重新读取表格数据
        // app.readMasterUser();
      }else{
        this.group.currentRow = JSON.parse(JSON.stringify(rowContent));
        // this.group.currentRow = rowContent;
        rowContent.isSet = true;
        this.$set(this.group.data, index, rowContent);
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
    del(rowContent, index){
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
            this.count_all-=1;
            this.group.data.splice(index,1);
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
        this.$message({
          type: 'info',
          message: '已取消删除'
        });          
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
      this.count_all = response.data.item_num
      this.group.data = response.data.result;
      // this.count_all=response.data.item_num;
      this.group.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      // this.group.data = JSON.parse(JSON.stringify(this.group.data));
      // console.log(this.group.data);s
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