<template>
  <div>
    <el-row :gutter=20 v-for="m in 3" :key="m">
      <el-col :span=6 v-for="n in 4" :key="n">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span><h4>管理首页 {{m}}-{{n}}</h4></span>
            <!-- <el-button style="float: right; padding: 3px 0" type="text">X</el-button> -->
          </div>
          <div class="el-icon-setting">
            <span></span>
            <!-- <i class="el-icon-message"></i>           -->
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
    // var list = JSON.parse(localStorage.getItem('list'));
      
    // var api="http://127.0.0.1:9090/acct/request_form/6";
    var api='http://www.phonegap100.com/appapi.php?a=getPortalList&catid=20&page=2';
    Axios.get(api).then((response)=>{
      // console.log(response);
      this.test_list=response.data.result;
    }).catch((error)=>{
      console.log(error);
    })
  }
}
</script>

<style scoped>
.ho-pad{
  padding-top: 28px;
  padding-bottom: 28px;
}
</style>