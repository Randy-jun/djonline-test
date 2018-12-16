<template>
  <div class="col-10">
    <h5>{{ msg }}</h5>
    <div class="col d-flex">
      <input class="form-control mr-3" type="text" placeholder="TODO..." v-model='todo' v-on:keyup.enter="doAdd($event)">
      <button class="btn btn-outline-success" v-on:click="doAdd($event)">添加</button>
    </div>
    <h2>Doing...</h2>
    <div v-for="(item,key) in list" v-if="!item.checked" v-bind:key='item.id'>
      <!-- key 要写到后面才可以 -->
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <input v-model="item.checked" v-on:change="saveList()" type="checkbox">
          </div>
        </div>
        <div class="form-control d-flex align-items-start">{{item.title}}</div>
        <div class="input-group-append">
          <button class="btn btn-sm btn-danger ml-2 mt-1 mb-1" v-on:click="doDel(key)">Delete</button>
        </div>
      </div>
    </div> 
    <h2>Done</h2>
    <div v-for="(item,key) in list" v-if="item.checked" v-bind:key='item.id'>
      <!-- key 要写到后面才可以 -->
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <input v-model="item.checked" v-on:change="saveList()" type="checkbox">
          </div>
        </div>
        <div class="form-control d-flex align-items-start">{{item.title}}</div>
        <div class="input-group-append">
          <button class="btn btn-sm  btn-danger ml-2 mt-1 mb-1" v-on:click="doDel(key)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import storage from '../module/lstorage.js';
export default {
  name: 'Home',
  props: {
    msg: String
  },
  data() {
    return {
      todo:'',
      list:[],
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
      storage.set('list', this.list);
      // localStorage.setItem('list', JSON.stringify(this.list));
    }
  },
  mounted(){
    // var list = JSON.parse(localStorage.getItem('list'));
    var list = storage.get('list');
    if (list) {
      this.list = list;
    }
  }
}
</script>

<style scoped>
</style>