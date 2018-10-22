<template>
  <div class="col">
    <div class="row">
      <table class="table table-hover table-responsive-lg">
         <thead class="thead-lights">
            <tr>
               <th>AID</th>
               <th>标题</th>
               <th>Details/Edit/Del</th>
            </tr>
         </thead>
         <tbody v-for="(item,key) in data_list" v-bind:key='item.aid'>
            <!-- key 要写到后面才可以 -->
            <tr>
               <td>{{item.id}}</td>
               <td>{{item.name}}</td>
               <td>
                <div class="btn-group btn-group-sm">
                  <button type="button" class="btn btn-primary" v-bind:value="'#a'+key">Details</button>
                  <button type="button" class="btn btn-warnings">Edit</button>
                  <button type="button" class="btn btn-danger">Del</button>
                </div>
              </td>
            </tr>
         </tbody>
      </table>
      <div class="row">
        <div class="col-2"><button class="btn btn-default" v-on:click="doAdd($event)">添加</button></div>
      </div>
    </div>
    <div class="row">
        <div class="col"><button class="btn btn-success" v-on:click="postTest(true)">POST test</button></div>
        <div class="col"><button class="btn btn-danger" v-on:click="postTest(false)">POST test</button></div>
    </div>
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
.ho-pad{
  padding-top: 28px;
  padding-bottom: 28px;
}
</style>