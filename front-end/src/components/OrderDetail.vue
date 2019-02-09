<template>
<div>
   <el-row :gutter="10">
    <el-col :span="5">
      <h2>
        <span>订单编号：</span>
        <span>2019-002-0202</span>
      </h2>
    </el-col>
    <!-- <el-col :span="4" :push="6">
      <el-button-group>
        <el-button type="success" style="cursor: pointer;">受理订单</el-button>
        <el-button type="warning" style="cursor: pointer;">打回订单</el-button>
      </el-button-group>
    </el-col> -->
    <el-col v-if="buttonShow" :span="4" :push="6">
      <el-button-group>
        <el-button type="success" style="cursor: pointer;">确认结算</el-button>
        <el-button type="danger" style="cursor: pointer;">取消结算</el-button>
      </el-button-group>
    </el-col>
    <el-col v-if="buttonShow" :span="4" :push="6">
      <el-button-group>
        <el-button type="primary" style="cursor: pointer;">修改订单</el-button>
        <el-button type="danger" style="cursor: pointer;">删除订单</el-button>
      </el-button-group>
    </el-col>
  </el-row>
  <el-row :gutter="10">
    <el-col :span="2" :push="1">
      <h4>
        <span>联系人:</span>
        <span>雷老虎</span>
      </h4>
    </el-col>
    <el-col :span="2" :push="2">
      <h4>
        <span>人数:</span>
        <span>12</span>
      </h4>
    </el-col>
    <el-col :span="5" :push="2">
      <h4>
        <span>联系电话:</span>
        <span>188-9888-8889</span>
      </h4>
    </el-col>
    <el-col :span="14" :push="2">
      <h4>
        <el-tag type="danger">备注:请务必提前一天联系客户，核对接送信息的准确性。</el-tag>
      </h4>
    </el-col>
  </el-row>
  <el-row :gutter="10">
    <el-col :span="6">
      <h4>
        <span>订单类型: </span>
        <el-radio v-model="type" label="1">接机</el-radio>
        <el-radio v-model="type" label="2">送机</el-radio>
      </h4>
    </el-col>
  </el-row>
  <el-row>
    <el-col :span="16">
      <el-card shadow="always" class="box-card">
      <el-row :gutter="10">
        <h4>
          <el-col :span="2" :push="0">接机日期:</el-col>
          <el-col :span="3" :push="0">2019-02-02</el-col>
          <el-col :span="2" :push="4">航班号:</el-col>
          <el-col :span="2" :push="4">T678</el-col>
        </h4>
      </el-row>
      <el-row :gutter="10">
        <h4>
          <el-col :span="2" :push="0">结算金额:</el-col>
          <el-col :span="2" :push="0">888</el-col>
          <el-col :span="2" :push="5">起止城市:</el-col>
          <el-col :span="2" :push="5">西安-北京</el-col>
        </h4>
      </el-row>
      <el-row :gutter="10">
        <h4>
          <el-col :span="2" :push="0">接送地址:</el-col>
          <el-col :span="2" :push="0">幸福中路</el-col>
          <el-col :span="2" :push="5">起飞时间:</el-col>
          <el-col :span="2" :push="5">08:08</el-col>
        </h4>
      </el-row>
      <el-row :gutter="10">
        <h4>
          <el-col :span="2" :push="0">航站楼:</el-col>
          <el-col :span="2" :push="0">T3</el-col>
          <el-col :span="2" :push="5">落地时间:</el-col>
          <el-col :span="2" :push="5">12:00</el-col>
        </h4>
      </el-row>
    </el-card>
    </el-col>
    <el-col :span="5">
      <el-row><h4>订单跟踪轨迹</h4></el-row>
      <el-row>猪八戒提交订单</el-row>
      <el-row>猪八戒小白龙受理订单</el-row>
      <el-row>唐僧更改为已确认结算订单</el-row>
    </el-col>
  </el-row>
    <el-row :gutter="10">
    <el-col :span="2" :push="1">
      <h4>
        <span>提交人:</span>
        <span>猪八戒</span>
      </h4>
    </el-col>
    <el-col :span="2" :push="2">
      <h4>
        <span>所属组织:</span>
        <span>中旅</span>
      </h4>
    </el-col>
  </el-row>
</div>
</template>

<script>
import Order from '@/module/order.js';
import InputCheck from '@/module/inputcheck.js';
import UserInfo from '@/module/userinfo.js';

export default {
  name: 'OrderDetail',
  props: {
    msg: String
  },
  data() {
    return {
      buttonShow: false,
      type:"1",
      order:{},
      isEdit:false,
    }
  },
  mounted() {
    Order.getOne().then((response) => {
      // console.log(response)
      this.order = JSON.parse(JSON.stringify(response));
      console.log(this.order)
    }).catch((error) => {
      // console.log(error);
    });
    UserInfo.getLevel().then((response) => {
      if('0' == response) this.buttonShow = true;
    }).catch((error) => {
      console.log(error);
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
</style>
