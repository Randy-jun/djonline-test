<template>
  <div class="col" id="groups">
    <CustomeAlert v-if="alertState" v-bind:alertmsg="alertMsg" />
    <!-- <div class="alert alert-success" role="alert">
      A simple success alert—check it out!
    </div> -->
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
                  <button type="button" class="btn btn-primary btn-sm">编辑</button>
                  <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" v-bind:data-target='"#deleteConfirm"+item.id'>删除</button>
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
                        <button class="btn btn-danger btn-sm" data-dismiss="modal" v-on:click="doDeleGroup(index, item.id)">确认</button>
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
    <div class="row align-items-end">
      <div class="col"><button type="button" class="btn btn-success btn-sm" data-toggle="modal" data-target="#addGroup">新增组团社</button></div>
      <div class="modal fade" role="dialog" id="addGroup">
        <div class="modal-dialog modal-md modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">新增组团社</h5>
              <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button> -->
            </div>
            <div class="modal-body">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="groupName">组团社名称</span>
                </div>
                <input type="text" class="form-control" id="groupNameInput" aria-describedby="groupName" v-model="AddGroup.groupName">
              </div>
              <small>{{AddGroup.groupName}}</small>
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text">备注</span>
                </div>
                <textarea class="form-control" aria-label="备注" placeholder="备注内容请保持在120字以内..." v-model="AddGroup.groupRemark"></textarea>
              </div>
              <small>{{AddGroup.groupRemark}}</small>
            </div>
            <div class="modal-footer">
              <button class="btn btn-success btn-sm" data-dismiss="modal" v-on:click="doAddGroup($event)">保存</button>
              <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Axios from 'axios';
import Storage from '@/module/lstorage.js';
import CustomeAlert from  '@/components/sysinfo/CustomAlert.vue';

export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      count_all:null,
      alertState:false,
      alertMsg:null,
      AddGroup:{
        groupName:null,
        groupRemark:null,
      },
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
  components: {
    CustomeAlert,
  },
  methods: {
    choice(groupid){
      // console.log(zuid)
    },
    doDeleGroup(localId, groupid){
      var api='http://127.0.0.1:9090/acct/agency/' + groupid;
      console.log(api);
      Axios.delete(api).then((response)=>{
        console.log(response);
        this.alertMsg={
          'stateFlag':'alert-success',
          'msgConten':'删除成功！',
        }
        this.alertState=true;
        this.data_list.splice(localId,1)
        setTimeout(()=>{
          this.alertState=false;
          // this
        },2000);
      }).catch((error)=>{
        // console.log(error);
      })
      // console.log(groupid);
      
    },
    doAddGroup(e){
      const api='http://127.0.0.1:9090/acct/agencies/';
      if (e.type == 'click' || e.keyCode == 13) {
        // console.log(this.username,this.password);
        var params = new URLSearchParams();
        params.append("AddGroup",this.AddGroup);
        Axios.post(api, params).then((response)=>{
          console.log(response);
          this.alertMsg={
            'stateFlag':'alert-success',
            'msgConten':'添加成功！',
          }
          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
            // this
          },2000);
        })
        .catch((error)=>{
          console.log(error);
        });
      }
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
        console.log(this.data_list)
        // setTimeout(()=>{
        //   this.data_list.splice(0,1)
        //   console.log(this.data_list)
        // },5000);
        
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
#groups{
  margin-bottom: 2%;
}
</style>