<template>
  <div class="col">
    <small>总共: <span class="font-italic font-weight-bold">{{count_all}}</span> 条记录</small>
    <div class="row">
      <table class="table table-hover table-responsive-lg">
         <thead class="thead-lights">
            <tr>
               <!-- <th>
                 <div class="custom-control custom-checkbox">
                  <input type="checkbox" class="custom-control-input" v-on:change="choiceall()" id="allCheck">
                  <label class="custom-control-label" for="allCheck">全选</label>
                </div>
               </th> -->
               <th>序号</th>
               <th>组团社ID</th>
               <th>组团社名称</th>
               <th>备注</th>
               <th>操作</th>
            </tr>
         </thead>
         <tbody>
            <!-- key 要写到后面才可以 -->
            <tr v-for="(item, index) in data_list">
              <!-- <td>
                 <div class="custom-control custom-checkbox">
                  <input type="checkbox" class="custom-control-input" v-on:change="choiceall()" v-bind:id="item.id">
                  <label class="custom-control-label" v-bind:for="item.id"></label>
                </div>
               </td> -->
               <td>{{index + 1}}</td>
               <td v-bind:id="item.id" >{{item.id}}</td>
               <td v-bind:id="item.id">{{item.name}}</td>
               <td v-bind:id="item.id">{{item.remark}}</td>
               <td>
                <div class="btn-group btn-group-sm">
                  <button type="button" class="btn btn-second">编辑</button>
                  <button type="button" class="btn btn-danger" data-toggle="modal" v-bind:data-target='"#deleteConfirm"+item.id'>删除</button>
                </div>
                <div class="modal fade" role="dialog" v-bind:id='"deleteConfirm"+item.id'>
                  <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">确认删除吗？</h5>
                        <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button> -->
                      </div>
                      <!-- <div class="modal-body">
                        <p>Modal body text goes here.</p>
                      </div> -->
                      <div class="modal-footer">
                        <button class="btn btn-danger btn-sm" data-dismiss="modal" v-on:click="delete_group(item.id)">确认</button>
                        <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
                      </div>
                    </div>
                  </div>
                </div>
              </td>
            </tr>
         </tbody>
      </table>
    </div>
    <div class="row">
      <div class="col-2"><button class="btn btn-default" v-on:click="doAdd($event)">添加</button></div>
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
      count_all:0,
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
    choice(groupid){
      // console.log(zuid)
    },
    delete_group(groupid){
      
      console.log(groupid)
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
        this.data_list=response.data.result;
        this.count_all=response.data.result.length;
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