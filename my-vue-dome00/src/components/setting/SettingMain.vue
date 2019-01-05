<template>
<div>
  <el-row :gutter=20>
    <el-col :span=8>
      <el-card shadow="always" class="box-card">
        <div slot="header" class="clearfix">
          <i class="el-icon-tickets"></i>
        </div>
        <span><h4>组团社管理</h4></span>
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
          <span><h4>线路报价管理</h4></span>
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
import Axios from 'axios';
import Storage from '@/module/lstorage.js';
export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      order:{
        dj_name:"百恒国际旅行社",
        zt_name:"光大旅行社",
        dd_number:"CTSQD-0001",
        xl_name:"西安北线二日游（淡季）",
        def_price: 8888,
        dd_date:"2018-8.31"
      },
      test_list:[],
      tourist:[  
        {
          name:"甲",
          count:1,
          refer_price:{rp_name:"成人",rp_price:270},
          modify_price:10,
          final_price:280,
          modify_price_remark:"含餐",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"乙",
          count:1,
          refer_price:{rp_name:"车住",rp_price:160},
          modify_price:30,
          final_price:190,
          modify_price_remark:"法门寺电瓶车",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丙",
          count:1,
          refer_price:{rp_name:"车费",rp_price:130},
          modify_price:10,
          final_price:140,
          modify_price_remark:"含餐",
          tran_price:100,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丁",
          count:10,
          refer_price:{rp_name:"成人",rp_price:2700},
          modify_price:100,
          final_price:2800,
          modify_price_remark:"含餐",
          tran_price:2000,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"戊",
          count:5,
          refer_price:{rp_name:"成人",rp_price:1350},
          modify_price:-200,
          final_price:1150,
          modify_price_remark:"优惠",
          tran_price:1000,
          tran_org:"中国青年旅行社",
          tran_remark:null,
          delivery:100,
          delivery_remark:"车费",
        },
        {
          name:"甲",
          count:1,
          refer_price:{rp_name:"成人",rp_price:270},
          modify_price:10,
          final_price:280,
          modify_price_remark:"含餐",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"乙",
          count:1,
          refer_price:{rp_name:"车住",rp_price:160},
          modify_price:30,
          final_price:190,
          modify_price_remark:"法门寺电瓶车",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丙",
          count:1,
          refer_price:{rp_name:"车费",rp_price:130},
          modify_price:10,
          final_price:140,
          modify_price_remark:"含餐",
          tran_price:100,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丁",
          count:10,
          refer_price:{rp_name:"成人",rp_price:2700},
          modify_price:100,
          final_price:2800,
          modify_price_remark:"含餐",
          tran_price:2000,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"戊",
          count:5,
          refer_price:{rp_name:"成人",rp_price:1350},
          modify_price:-200,
          final_price:1150,
          modify_price_remark:"优惠",
          tran_price:1000,
          tran_org:"中国青年旅行社",
          tran_remark:null,
          delivery:100,
          delivery_remark:"车费",
        },
        {
          name:"甲",
          count:1,
          refer_price:{rp_name:"成人",rp_price:270},
          modify_price:10,
          final_price:280,
          modify_price_remark:"含餐",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"乙",
          count:1,
          refer_price:{rp_name:"车住",rp_price:160},
          modify_price:30,
          final_price:190,
          modify_price_remark:"法门寺电瓶车",
          tran_price:null,
          tran_org:null,
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丙",
          count:1,
          refer_price:{rp_name:"车费",rp_price:130},
          modify_price:10,
          final_price:140,
          modify_price_remark:"含餐",
          tran_price:100,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:20,
          delivery_remark:"车费",
        },
        {
          name:"丁",
          count:10,
          refer_price:{rp_name:"成人",rp_price:2700},
          modify_price:100,
          final_price:2800,
          modify_price_remark:"含餐",
          tran_price:2000,
          tran_org:"大唐旅行社",
          tran_remark:null,
          delivery:null,
          delivery_remark:null,
        },
        {
          name:"戊",
          count:5,
          refer_price:{rp_name:"成人",rp_price:1350},
          modify_price:-200,
          final_price:1150,
          modify_price_remark:"优惠",
          tran_price:1000,
          tran_org:"中国青年旅行社",
          tran_remark:null,
          delivery:100,
          delivery_remark:"车费",
        },
      ],
    }
  },
  methods: {
    doAdd(e){
      // console.log(e)
      if (e.type == 'click' || e.keyCode == 13) {
        this.list.push(
          {
            title:this.todo,
            checked:false,
          }
        );
      this.todo='';
      }
      this.saveList();
    },
    doDel(delKey){
      this.list.splice(delKey,1 );
      this.saveList();
    },
    saveList(){
      Storage.set('list', this.list);
      // localStorage.setItem('list', JSON.stringify(this.list));
    }
  },
  mounted() {

  }
}
</script>

<style scoped>
.ho-pad{
  padding-top: 28px;
  padding-bottom: 28px;
}

.bottom {
  margin-top: 8px;
  line-height: 12px;
}
.button {
  padding:2px;
  float: right;
}
.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}
</style>