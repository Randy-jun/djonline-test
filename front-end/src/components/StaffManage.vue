<template>
  <div>
    <el-row>
      <el-col :span="2">
        <el-button type="primary" size="medium" plain style="width: 98.2%" icon="el-icon-circle-plus-outline" v-on:click="doAdd()">添加新职员</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-table v-if="0 !== table.countAll" :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip>
        <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
        <!-- <el-table :data="table.data" style="width: 100%" highlight-current-row v-on:current-change="handleCurrentChange" show-overflow-tooltip :default-sort = "{prop: 'id', order: 'ascending'}"> -->
        <el-table-column align='center' fixed type="index" width="100"></el-table-column>
        <!-- <el-table-column v-for="(v,i) in table.columns" :prop="v.field" :label="v.title" :sortable="v.sortable"> -->
        <el-table-column align='center' v-for="(value, key) in table.columns" :prop="value.field" :label="value.title" :sortable="value.sortable">
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
              <el-select size="mini" v-model="table.currentRow.statuscode" >
                <el-option v-for="item in statusList" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
            </span>
            <span v-else>
              <el-tag size="mini" :type="scope.row.statuscode?'success':'danger'">{{scope.row.statusflag}}</el-tag>
            </span>
          </template>
        </el-table-column>
        <el-table-column align='center' fixed="right" label="操作" width="150">
          <template slot-scope="scope">
            <span class="el-tag el-tag--info el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,false)">
                {{scope.row.isSet?'保存':"修改"}}
            </span>
            <span v-if="!scope.row.isSet" class="el-tag el-tag--danger el-tag--mini" v-on:click="doDel(scope.row,scope.$index)" style="cursor: pointer;">删除</span>
            <span v-else class="el-tag  el-tag--mini" style="cursor: pointer;" v-on:click="currentRowChange(scope.row,scope.$index,true)">取消</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <!-- <el-row>
      <el-pagination  
        v-on:size-change="handleSizeChange"
        v-on:current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="table.countAll">
      </el-pagination>
    </el-row> -->
  </div>
</template>

<script>
import Staff from '@/module/staff.js';
import InputCheck from '@/module/inputcheck.js';

export default {
  name: 'StaffManage',
  props: {
    msg: String
  },
  data() {
    return {
      statusList: [
          {value: true,label: '启用'},
          {value: false,label: '禁用'},
        ],
      table: {
        countAll: null,
        currentRow: null,//选中行   
        columns: [
          // { field: "id", title: "编号", width: 150, isEdit: false, sortable: true },
          { field: "e_username", title: "账号", width: 120, isEdit: true, sortable: false },
          { field: "nickname", title: "姓名", width: 120, isEdit: true, sortable: false },
          // { field: "ugroup", title: "归属组织", width: 220, isEdit: true, sortable: true },
          { field: "e_remark", title: "备注", width: 220, isEdit: true, sortable: false },
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
    choice(id){
      // console.log(zuid)
    },
    // statusChange(value){
    //   let obj = {};
    //   obj = this.statusList.find((item)=>{//这里的selectList就是上面遍历的数据源
    //       return item.value === value;//筛选出匹配数据
    //   });
    //   // console.log(obj)
    //   this.table.currentRow.statuscode = obj.value;
    //   this.table.currentRow.statusflag = obj.label;
    // },
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
        // rowContent.statuscode = this.table.currentRow.statuscode;
        return this.$set(this.table.data, index, rowContent)
      }

      if (rowContent.isSet) {
        // let tempData = JSON.parse(JSON.stringify(this.table.currentRow));

        if(InputCheck.namecheck(this.table.currentRow.name)) return this.$message.warning("组织名称不能为空或空格!");
        
        if(null !== rowContent.id){
          Staff.update(this.table.currentRow).then((response) => {
            this.$set(response, 'isSet', false);
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
          })
        }else{
          Staff.insert(this.table.currentRow).then((response) => {
            this.table.countAll+=1;
            this.$set(response, 'isSet', false);
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
          })
        }
      }else{
        this.table.currentRow = JSON.parse(JSON.stringify(rowContent));
        // this.table.currentRow = rowContent;
        rowContent.isSet = true;
        this.table.columns[0].isEdit = false;
        // this.$set(this.table.data, index, rowContent);
        this.table.data.splice(index, 1, rowContent)
      }
    },
    doAdd(){
      for (let item of this.table.data) {
        if (item.isSet) return this.$message.warning("请先保存当前编辑项!");
      }
      // let tempAddData = {id: null, "name": "", "remark": "", "isSet": true,};
      this.table.columns[0].isEdit = true;
      let tempAddData = {id: null, e_username: "", nickname: "", e_remark: "", statuscode: true, statusflag: "正常",isSet: true,};
      this.table.data.push(tempAddData);
      this.table.currentRow = JSON.parse(JSON.stringify(tempAddData));
      // console.log(this.table.data)
    },
    doDel(rowContent, index){
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(rowContent, index);
        Staff.delete(rowContent.id).then((response) => {
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
      }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除!'
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
    Staff.get().then((response) => {
      // this.table.countAll = JSON.parse(JSON.stringify(response.item_num));
      // this.table.data = JSON.parse(JSON.stringify(response.result));
      this.table.countAll = JSON.parse(JSON.stringify(response.item_num));
      // this.table.data = JSON.parse(JSON.stringify(response.result));
      this.table.data = response.data;
      this.table.data.forEach(item => {
        this.$set(item, 'isSet', false);
      });
      // console.log(typeof(this.table.data))
      // this.table.data = response.result;
    }).catch((error) => {
      // console.log(error);
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
