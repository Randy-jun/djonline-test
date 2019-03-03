<template>
<div>
   <el-row type="flex" align="middle" justify="space-between">
    <el-col :span="8">
      <h2 v-if="!isAdd">
        <span>订单编号：</span>
        <span>{{order.id}}</span>
      </h2>
    </el-col>
    <el-col :span="10">
      <el-steps :active="order.statusCode" finish-status="success" simple>
        <el-step title="暂存"></el-step>
        <el-step title="提交"></el-step>
        <el-step title="受理"></el-step>
        <el-step title="结算"></el-step>
      </el-steps>
    </el-col>
    <el-col :span="4">
      <el-button-group v-if="!isAdd || !isEdit">
        <el-button type="primary" @click="orderChange" style="cursor: pointer;">{{isEdit?"取消修改":"修改订单"}}</el-button>
        <el-button type="danger" @click="doDel" style="cursor: pointer;">删除订单</el-button>
      </el-button-group>
      <el-button v-else type="primary" @click="goBack" style="cursor: pointer;">返回</el-button>
    </el-col>
  </el-row>
  <el-row :gutter="10" type="flex" justify="center">
    <el-col :span="23">
      <el-tabs @tab-click="orderTypeChange" v-model="order.typeCode" type="border-card">
        <el-tab-pane v-if="isEdit || '0' == order.typeCode" label="接机" name="0">
          <el-row v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-input v-model="order.linkMan">
                <template slot="prepend">联系人</template>
              </el-input>
            </el-col>
             <el-col :span="5">
              <el-input v-model="order.phoneNumber">
                <template slot="prepend">联系电话</template>
              </el-input>
            </el-col>
            <el-col :span="5">
              <span>人数：</span>
              <el-input-number v-model="order.count" :min="1" :max="100"></el-input-number>
            </el-col>
            <el-col :span="5">
              <span>订单金额：</span>
              <el-input-number v-model="order.charge" :min="0" :max="9999999"></el-input-number>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>联系人:{{order.linkMan}}</span>
            <span>联系电话:{{order.phoneNumber}}</span>
            <span>人数:{{order.count}}</span>
            <span>订单金额：{{order.charge}}</span>
          </el-row>
          <el-row  v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-date-picker
                v-model="order.date"
                type="date"
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="接机日期">
              </el-date-picker>
            </el-col>
            <el-col :span="5">
              <el-time-picker
                v-model="order.arriveTime"
                type="time"
                align="center"
                format="hh 时 mm 分"
                value-format="hh:mm"
                placeholder="接机时间">
              </el-time-picker>      
            </el-col>
            <el-col :span="5">
              <el-input v-model="order.lineNumber">
                <template slot="prepend">航班号</template>
              </el-input>     
            </el-col>
            <el-col :span="5">
              <el-input v-model="order.terminal">
                <template slot="prepend">航站楼</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>起飞日期:{{order.date}}</span>
            <span>接机时间:{{order.arriveTime}}</span>
            <span>航班号:{{order.lineNumber}}</span>
            <span>航站楼:{{order.terminal}}</span>
          </el-row>
          <el-row v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-input v-model="order.leaveCity">
                <template slot="prepend">起飞城市</template>
              </el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="order.address">
                <template slot="prepend">送客地址</template>
              </el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="order.remark">
                <template slot="prepend">备注</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>起飞城市:{{order.leaveCity}}</span>
            <span>送客地址:{{order.address}}</span>
            <span>备注:{{order.remark}}</span>
          </el-row>
        </el-tab-pane>
        <el-tab-pane  v-if="isEdit || '1' == order.typeCode" label="送机" name="1">
          <el-row v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-input v-model="order.linkMan">
                <template slot="prepend">联系人</template>
              </el-input>
            </el-col>
             <el-col :span="5">
              <el-input v-model="order.phoneNumber">
                <template slot="prepend">联系电话</template>
              </el-input>
            </el-col>
            <el-col :span="5">
              <span>人数：</span>
              <el-input-number v-model="order.count" :min="1" :max="100"></el-input-number>
            </el-col>
            <el-col :span="5">
              <span>订单金额：</span>
              <el-input-number v-model="order.charge" :min="0" :max="9999999"></el-input-number>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>联系人:{{order.linkMan}}</span>
            <span>联系电话:{{order.phoneNumber}}</span>
            <span>人数:{{order.count}}</span>
            <span>订单金额：{{order.charge}}</span>
          </el-row>
          <el-row  v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-date-picker
                v-model="order.date"
                type="date"
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="送机日期">
              </el-date-picker>
            </el-col>
            <el-col :span="5">
              <el-time-picker
                v-model="order.leaveTime"
                type="time"
                align="center"
                format="hh 时 mm 分"
                value-format="hh:mm"
                placeholder="送机时间">
              </el-time-picker>      
            </el-col>
            <el-col :span="5">
              <el-input v-model="order.lineNumber">
                <template slot="prepend">航班号</template>
              </el-input>     
            </el-col>
            <el-col :span="5">
              <el-input v-model="order.terminal">
                <template slot="prepend">航站楼</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>起飞日期:{{order.date}}</span>
            <span>送机时间:{{order.leaveTime}}</span>
            <span>航班号:{{order.lineNumber}}</span>
            <span>航站楼:{{order.terminal}}</span>
          </el-row>
          <el-row v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-input v-model="order.arriveCity">
                <template slot="prepend">到达城市</template>
              </el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="order.address">
                <template slot="prepend">接客地址</template>
              </el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="order.remark">
                <template slot="prepend">备注</template>
              </el-input>
            </el-col>
          </el-row>
          <el-row v-else :gutter="10" type="flex" justify="space-between">
            <span>到达城市:{{order.arriveCity}}</span>
            <span>接客地址:{{order.address}}</span>
            <span>备注:{{order.remark}}</span>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="5">
      <span v-if="!isAdd" >所属组织:{{order.group}}</span>
    </el-col>
    <el-col :span="5">
      <span v-if="!isAdd" 制单人：{{order.user}}</span>
    </el-col>
    <el-col :span="5">
      <span v-if="!isAdd" 提交人：{{order.Submit}}</span>
    </el-col>
    <el-col :span="4">
      <el-button-group v-if="isEdit">
        <el-button v-if="isAdd" type="primary" @click="onSave(false)" style="cursor: pointer;">临时保存</el-button>
        <el-button type="success" @click="onSave(true)" style="cursor: pointer;">保存提交</el-button>
      </el-button-group>
    </el-col>
  </el-row>
</div>
</template>

<script>
import Order from '@/module/order.js';
import InputCheck from '@/module/inputcheck.js';
// import UserInfo from '@/module/userinfo.js';
import Sstorage from '@/module/sstorage.js';

export default {
  name: 'OrderDetail',
  props: {
    msg: String
  },
  data() {
    return {
      order:{},
      orderTemp:null,
      isEdit:false,
      isAdd:false,
      orderId:null,
      userLevel:null,
    }
  },
  methods: {
    goBack() {
      var orderlist = "/home/orderlist";
      // console.log(goadd)
      this.$router.replace({ path: orderlist })
    },
    orderTypeChange(value) {
      // console.log(value.paneName);
      this.order.typeCode = value.paneName;
    },
    orderChange() {
      if (this.isEdit) {
        this.isEdit = false;
        return this.order = this.orderTemp;
      } else {
        this.orderTemp = JSON.parse(JSON.stringify(this.order));;
        return this.isEdit = true;
      }
      
    },
    onSave(isSave) {
      // this.isEdit = false;
      if (isSave) {
        this.order.statusCode = 2;
      } else {
        this.order.statusCode = 1;
      }
      Order.change(this.order).then((response) => {
        // console.log(response)
        this.order = JSON.parse(JSON.stringify(response));
        // console.log(this.order)
        this.isEdit = false;
        this.isAdd = false;
      }).catch((error) => {
        // console.log(error);
      });
    },
    doDel(){
      this.$confirm('此操作将永久删除该组织, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
       Order.delete(this.order.id).then((response) => {
          this.$message({
            type: 'success',
            message: "删除成功！"
          });
          this.goBack();
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
  },
  mounted() {
    this.userLevel = Sstorage.get('userLevel');
    this.isAdd = Sstorage.get('orderAdd');
    console.log(this.isAdd)
    if (this.isAdd) {
      this.isEdit = true;
      this.order = {
        id:null,
        address: "",
        arriveCity: "",
        arriveTime: "",
        charge: 0,
        count: 1,
        date: "",
        leaveTime: "",
        leaveCity: "",
        lineNumber: "",
        linkMan: "",
        phoneNumber: "",
        remark: "",
        statusCode: 0,
        terminal: "",
        typeCode: "0",
      };
    } else {
      console.log("57638920847839")
      this.isEdit = false;
      this.orderId = Sstorage.get('orderID');
      Order.getOne(this.orderId).then((response) => {
        // console.log(response)
        this.order = JSON.parse(JSON.stringify(response));
        console.log(this.order)
      }).catch((error) => {
        // console.log(error);
      });
    }
    console.log(this.isEdit, this.isAdd)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
</style>
