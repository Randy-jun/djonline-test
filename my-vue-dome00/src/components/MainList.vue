<template>
<div>
  <el-row :gutter=20 v-for="m in 3" :key="m">
    <el-col :span=6 v-for="n in 4" :key="n">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span><h4>应用 {{m}}-{{n}}</h4></span>
          <!-- <el-button style="float: right; padding: 3px 0" type="text">X</el-button> -->
        </div>
        <div class="el-icon-message">
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
      // post_data:{},
      data_list:[],
      tourist:[]
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
    },
    postTest(flag){
      const api='http://127.0.0.1:9090/acct/get_json/';
      // var post_data={"id":123,"title":"this is 中文"};

      var params = new URLSearchParams();
      params.append('id', 1234325456); 
      if(flag){
        params.append('id', 156); 
      }
      params.append('title', 'this is 中文');
      Axios.post(api, params)
        .then(function (response) {
          alert(response.data.result);
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      // alert("POST test");
    }
  },
  mounted() {
    // var list = JSON.parse(localStorage.getItem('list'));
    
    const api='http://127.0.0.1:9090/acct/agencies/';
    Axios.get(api).then((response)=>{
        // console.log(response.data);
        this.data_list=response.data.result;
        // console.log(response.data.result);
        // console.log(typeof(response.data.result));
        // this.test_list=response.data.result;
      }).catch((error)=>{
        // console.log(error);
      })
  }
}
</script>

<style scoped>
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
.el-col {
  border-radius: 4px;
}
</style>