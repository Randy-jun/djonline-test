<template>
<div>
  <el-row :gutter=20>
    <el-col :span=8>
      <el-card shadow="always" class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-tickets"></i>
        </div>
        <span><h4>组织管理</h4></span>
        <div class="bottom clearfix">
          <el-button class="button" type="text" plain>进入</el-button>
        </div>
      </el-card>
    </el-col>
    <el-col :span=8>
      <el-card shadow="always" class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-tickets"></i>
        </div>
        <span><h4>用户管理</h4></span>
        <div class="bottom clearfix">
          <el-button class="button" type="text" plain>进入</el-button>
        </div>
      </el-card>
    </el-col>
    <el-col :span=8>
      <el-card shadow="always" class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-tickets"></i>
        </div>
        <span><h4>订单管理</h4></span>
        <div class="bottom clearfix">
          <el-button class="button" type="text" plain>进入</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
  <el-row :gutter=20>
    <el-col :span=8>
      <el-card shadow="always" class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-tickets"></i>
        </div>
        <span><h4>更多应用，敬请期待。</h4></span>
        <div class="bottom clearfix">
          <el-button class="button" type="text" plain disabled>进入</el-button>
        </div>
      </el-card>
    </el-col>
  </el-row>
</div>
</template>

<script>
export default {
  name: 'MainHome',
  props: {
    msg: String
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
