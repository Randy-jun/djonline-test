<template>
  <div class="col">
    <div class="row jumbotron ho-pad">
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">地接社名称：</h5><a class="card-text">{{order.dj_name}}</a></div></div>
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">组团社名称：</h5><a class="card-text">{{order.zt_name}}</a></div></div>
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">单据编号：</h5><a class="card-text">{{order.dd_number}}</a></div></div>
      <div class="w-100"></div>
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">线路名称：</h5><a class="card-text">{{order.xl_name}}</a></div></div>
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">默认报价：</h5><a class="card-text">{{order.def_price}}</a></div></div>
      <div class="col card text-center"><div class="card-body"><h5 class="card-title">出团日期：</h5><a class="card-text">{{order.dd_date}}</a></div></div>
    </div>
    <div>
      <ul class="nav nav-pills nav-justified">
        <li><a href="#">基础业务</a></li>
        <li><a href="#">调拨业务</a></li>
        <li><a href="#">代收业务</a></li>
      </ul>
    </div>
    <div class="row">
      <table class="table table-hover table-responsive-lg">
         <thead class="thead-lights">
            <tr>
               <th>ID</th>
               <th>姓名</th>
               <th>人数</th>
               <th>参考报价</th>
               <th>修正金额</th>
               <th>最终报价</th>
               <th>报价修正备注</th>
               <th>Details/Edit/Del</th>
            </tr>
         </thead>
         <tbody v-for="(item,key) in tourist" v-if="!item.checked" v-bind:key='item.id'>
            <!-- key 要写到后面才可以 -->
            <tr>
               <td>{{key+1}}</td>
               <td>{{item.name}}</td>
               <td>{{item.count}}</td>
               <td>{{item.refer_price.rp_name}}:{{item.refer_price.rp_price}}</td>
               <td>{{item.modify_price}}</td>
               <td>{{item.final_price}}</td>
               <td>{{item.modify_price_remark}}</td>
               <td>
                <div class="btn-group btn-group-sm">
                  <button type="button" class="btn btn-primary" data-toggle="collapse" v-bind:data-target="'#a'+key">Details</button>
                  <button type="button" class="btn btn-warnings">Edit</button>
                  <button type="button" class="btn btn-danger">Del</button>
                </div>
              </td>
            </tr>
            <tr v-bind:id="'a'+key" class="collapse in">
              <td colspan="8">
                fdsfds
              </td>
            </tr>
         </tbody>
      </table>
      <div class="row">
        <div class="col-2"><button class="btn btn-default" v-on:click="doAdd($event)">添加</button></div>
      </div>
    </div>
    <ul class="pagination pagination-sm">
      <li><a href="#">&laquo;</a></li>
      <li><a href="#">1</a></li>
      <li><a href="#">2</a></li>
      <li><a href="#">3</a></li>
      <li><a href="#">4</a></li>
      <li><a href="#">5</a></li>
      <li><a href="#">&raquo;</a></li>
    </ul>
  </div>
</template>

<script>
import Axios from 'axios';
import Storage from '../module/storage.js';
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