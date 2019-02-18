<template>
  <el-row>
    <!-- <el-radio-group v-model="isCollapse">
      <el-radio :border="true" :label="false" size="mini" >展开</el-radio>
      <el-radio :border="true" :label="true" size="mini" >收起</el-radio>
    </el-radio-group> -->
    <!-- <el-menu default-active="1-4-1" class="el-menu-vertical" @open="handleOpen" @close="handleClose" :collapse="isCollapse"> -->
    <el-menu class="el-menu-vertical" default-active="1" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-menu-item index="1" v-on:click="navgo('')">
        <i class="el-icon-menu"></i>
        <span slot="title" >首页</span>
      </el-menu-item>
      <el-menu-item v-if="menu[0]" index="2" v-on:click="navgo('group')">
        <i class="el-icon-menu"></i>
        <span slot="title">组织管理</span>
      </el-menu-item>
      <el-menu-item v-if="menu[2]" index="4" v-on:click="navgo('partner')">
        <i class="el-icon-menu"></i>
        <span slot="title">用户管理</span>
      </el-menu-item>
      <el-menu-item v-if="menu[1]" index="3" v-on:click="navgo('staff')">
        <i class="el-icon-menu"></i>
        <span slot="title">职员管理</span>
      </el-menu-item>
      <el-menu-item v-if="menu[3]" index="5" v-on:click="navgo('orderlist')">
        <i class="el-icon-menu"></i>
        <span slot="title">订单管理</span>
      </el-menu-item>
      <el-menu-item v-if="menu[4]" index="6" v-on:click="navgo('order')">
        <i class="el-icon-menu"></i>
        <span slot="title">订单详情</span>
      </el-menu-item>
        <!-- <el-menu-item-group>
          <span slot="title">分组一</span>
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <span slot="title">选项4</span>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">导航二</span>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <i class="el-icon-document"></i>
        <span slot="title">导航三</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item> -->
    </el-menu>
  </el-row>
</template>

<script>
import Sstorage from '@/module/sstorage.js';

export default {
  data() {
    return {
      isCollapse: false,
      menu:[false, false, false, false, false]
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    navgo(addgo){
      var goadd = "/home/" + addgo
      // console.log(goadd)
      this.$router.replace({ path: goadd })
    },
  },
  mounted() {
    let userLevel = Sstorage.get('userLevel');
    console.log(userLevel);
    if (0 == userLevel) {
     this.menu = [true, true, true, true, true]; 
    }else if (1 == userLevel) {
      this.menu = [false, false, false, true, true];
    }else if (2 == userLevel) {
      this.menu = [false, false, true, true, true];
    }else if (3 == userLevel) {
      this.menu = [false, false, false, true, true];
    }
  },
}
  
// export default {
//   name: 'Asider',
//   data() {
//     return {
//         menu_name: "MENU",
//     }
//   },
//   props: {
//     msg: String,
//   },
//   mounted() {

//   }
// }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-row{
  
}
.el-menu-vertical:not(.el-menu--collapse) {
  /* width: 200px; */
  min-height: 400px;
}
</style>
