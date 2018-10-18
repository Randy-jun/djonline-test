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
               <th>编号</th>
               <th>名称</th>
               <th>1档位报价</th>
               <th>2档位报价</th>
               <th>3档位报价</th>
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
               <td v-bind:id="item.id">{{item.name}} </td>
               <td v-bind:id="item.id">{{item.top3_ref_data0}} </td>
               <td v-bind:id="item.id">{{item.top3_ref_data1}} </td>
               <td v-bind:id="item.id">{{item.top3_ref_data2}} </td>
               <td v-bind:id="item.id">{{item.remark}}</td>
               <td>
                <div class="btn-group btn-group-sm">
                  <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#editPage" v-on:click="update(index, item)">编辑</button>
                  <button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#deleteConfirm" v-on:click="del(index, item.id)">删除</button>
                </div>
                
              </td>
            </tr>
         </tbody>
      </table>
    </div>
    <div class="row align-items-end">
      <div class="col"><button type="button" class="btn btn-success btn-sm" data-toggle="modal" data-target="#editPage" v-on:click="add()">新增组团社</button></div>
    </div>
    <!-- TODO:还没有做成线路报价单的样式 -->
    <div class="modal fade" role="dialog" id="editPage">
      <div class="modal-dialog modal-md modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{editPage.title}}</h5>
            <div>
              <button class="btn btn-success btn-sm" style="margin-right:10px" data-dismiss="modal" v-on:click="doSave()">保存</button>
              <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
            </div>
            <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button> -->
          </div>
          <div class="modal-body">
            <div>{{product.id}}</div>
            <div>{{product.name}}</div>
            <div>{{product.remark}}</div>
            <div>{{product.detail}}</div>
            <div v-for="(item, index) in product.prices">
              {{index+1}} : {{item.id}} : {{item.kind}} : {{item.line_price_fk}} : {{item.price}}
            </div>
          </div>
          <!-- <div class="modal-footer">
            <button class="btn btn-success btn-sm" data-dismiss="modal" v-on:click="doSave()">保存</button>
            <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
          </div> -->
        </div>
      </div>
    </div>
    <!-- TODO:还没有做成线路报价单的样式 -->
    <div class="modal fade" role="dialog" id="deleteConfirm">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">确认删除吗？</h5>
          </div>
          <div class="modal-footer">
            <button class="btn btn-danger btn-sm" data-dismiss="modal" v-on:click="doDel()">确认</button>
            <button class="btn btn-primary btn-sm" data-dismiss="modal">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import InputCheck from '@/module/inputcheck.js';
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
      alertMsg:{
        stateFlag:null,
        msgConten:null,
      },
      product:{
        id:null,
        name:null,
        remark:null,
        prices:[],
        detail:null,
      },
      editPage:{
        title:null,
        methods:null,
        id:null,
        localId:null,
      },
      delete:{
        id:null,
        localId:null,
      },
      api:'http://127.0.0.1:9090/acct/lineprices/',
      data_list:[],
    }
  },
  components: {
    CustomeAlert,
  },
  methods: {
    choice(id){
      // console.log(zuid)
    },
    del(localId, id){
      this.delete.id=id;
      this.delete.localId=localId;
    },
    doDel(){
      var params = new URLSearchParams();
      params.append("req_method","DELETE");
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("pk",this.delete.id);
      Axios.post(this.api, params).then((response)=>{
        console.log(response);
        if(response.data.status_flag){
          console.log(response);

          this.alertMsg.stateFlag="alert-success";
          this.alertMsg.msgConten="删除成功！";

          this.alertState=true;
          this.count_all-=1;
          this.data_list.splice(this.delete.localId ,1);
          setTimeout(()=>{
            this.alertState=false;
          },2000);
        }else{
          console.log(response);

          this.alertMsg.stateFlag="alert-danger";
          this.alertMsg.msgConten="删除失败！";

          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
          },2000);
        }})
        .catch((error)=>{
          console.log(error);
        });
    },
    update(localId, productContent){
      this.editPage.id=productContent.id;
      this.editPage.localId=localId;

      var params = new URLSearchParams();
      // params.append("req_method","GET_SINGLE");
      params.append("req_method","GETONE");
      
      params.append("pk",productContent.id);
      
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("local_name",Sstorage.get('localname'));

      Axios.post(this.api, params).then((response)=>{
        console.log(response)
        // this.product.id=response.data.result.line_price.id;
        // this.product.name=response.data.result.line_price.name;
        // this.product.remark=response.data.result.line_price.remark;
        this.product.detail=response.data.result.line_price.detail;

        this.product.prices=response.data.result.ref_prices;
        this.count_all=response.data.result.length;

      }).catch((error)=>{
        // console.log(error);
      })
      this.product.id=productContent.id;
      this.product.name=productContent.name;
      this.product.remark=productContent.remark;

      this.editPage.title="修改线路报价单";
      this.editPage.methods="UPDATE";
    },
    add(){
      this.group.name="";
      this.group.remark="";
      this.editPage.title="新增线路报价单";
      this.editPage.methods="ADD";
      this.editPage.localId=null;
    },
    doSave(){
      if(InputCheck.namecheck(this.group.name)){
        this.alertMsg={
            'stateFlag':'alert-danger',
            'msgConten':'线路报价单名称不能为空或空格',
        }
        this.alertState=true;
        setTimeout(()=>{
          this.alertState=false;
        },2000);
        return 1;
      }
      var params = new URLSearchParams();
      params.append("req_method",this.editPage.methods);
      
      if(null !== this.editPage.localId){
        params.append("pk",this.editPage.id);
      }

      params.append("name",this.group.name);
      params.append("remark",this.group.remark);
      
      params.append("tokenID",Sstorage.get('tokenID'));
      params.append("local_name",Sstorage.get('localname'));

      Axios.post(this.api, params).then((response)=>{
        if(response.data.status_flag){
          console.log(response);
          this.alertMsg.stateFlag="alert-success";

          // console.log(response.data.result)
          console.log(this.editPage.localId)
          if(null !== this.editPage.localId){
            this.data_list.splice(this.editPage.localId,1,response.data.result);
            this.alertMsg.msgConten="修改成功！";
          }else{
            this.count_all+=1;
            this.data_list.push(response.data.result)
            this.alertMsg.msgConten="添加成功！";
          }
          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
            // this
          },2000);
        }else{
          console.log(response);
          this.alertMsg={
            'stateFlag':'alert-danger',
            'msgConten':'修改失败！',
          }
          if(this.editPage.localId){
            this.alertMsg.msgConten="修改失败！";
          }else{
            this.alertMsg.msgConten="添加失败！";
          }
          this.alertState=true;
          setTimeout(()=>{
            this.alertState=false;
            // this
          },2000);
        }})
        .catch((error)=>{
          console.log(error);
        });
    },
  },
  mounted() {

    var params = new URLSearchParams();
    params.append("req_method","GET");
    params.append("userID",Sstorage.get('userID'));
    params.append("local_name",Sstorage.get('localname'));
    params.append("tokenID",Sstorage.get('tokenID'));
    Axios.post(this.api, params).then((response)=>{
        this.data_list=response.data.result;
        this.count_all=response.data.result.length;
        console.log(this.data_list)
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