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
      <el-steps :active="order.statuscode" finish-status="success" simple>
        <el-step title="暂存"></el-step>
        <el-step title="提交"></el-step>
        <el-step title="结算"></el-step>
      </el-steps>
    </el-col>
    <el-col :span="4">
      <el-button-group v-if="!isAdd || !isEdit">
        <el-button type="primary" @click="orderChange" style="cursor: pointer;">{{isEdit?"取消修改":"修改订单"}}</el-button>
        <el-button type="danger" style="cursor: pointer;">删除订单</el-button>
      </el-button-group>
    </el-col>
  </el-row>
  <el-row :gutter="10" type="flex" justify="center">
    <el-col :span="23">
      <el-tabs type="border-card">
        <el-tab-pane label="接机">
          <el-row v-if="isEdit" :gutter="10" type="flex" justify="space-between">
            <el-col :span="5">
              <el-input v-model="order.linkman">
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
            <span>联系人:{{order.linkman}}</span>
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
              <el-input v-model="order.levaeCity">
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
            <span>起飞城市:{{order.levaeCity}}</span>
            <span>送客地址:{{order.address}}</span>
            <span>备注:{{order.remark}}</span>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="送机">送机</el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="5">
      <span v-if="!isAdd" >所属组织:{{order.group}}</span>
    </el-col>
    <el-col :span="5">
      <span v-if="!isAdd" >提交人：{{order.user}}</span>
    </el-col>
    <el-col :span="4" :push="6">
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
import UserInfo from '@/module/userinfo.js';
import Sstorage from '@/module/sstorage.js';

export default {
  name: 'OrderDetail',
  props: {
    msg: String
  },
  data() {
    return {
      order:{
        id:1,
        remark:"",
        typeCode:2,
        statusCode:2,
        phoneNumber:"1231321123",
        from:"beijing",
        date:"2015-01-02",
        time:"12:55",
        zhidan:"adam",
        tijiao:"adam",
        shouli:"bill",
        fukuan:"Sam",
        shoukuan:"Tom",
        jiesuan_type:"2",
        dahui_msg:"default",
        status:"已付款",
      },
      orderTemp:null,
      isEdit:false,
      isAdd:true,
      orderId:null,
      userLevel:null,
    }
  },
  methods: {
    onSubmit() {
      console.log('submit!');
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
      this.isEdit = false;
    },
  },
  mounted() {
    this.userLevel = Sstorage.get('userLevel');
    this.isAdd = Sstorage.get('orderAdd');
    if (this.Add) {

    } else {
      this.orderId = Sstorage.get('orderID');
      Order.getOne(this.orderId).then((response) => {
        // console.log(response)
        this.order = JSON.parse(JSON.stringify(response));
        console.log(this.order)
      }).catch((error) => {
        // console.log(error);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
</style>
