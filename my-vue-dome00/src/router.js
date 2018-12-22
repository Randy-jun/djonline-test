import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/home',
      name: 'Home',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Home" */ '@/components/Home.vue'),
      children: [{
        path: 'records',
        component: () => import(/* webpackChunkName: "home/records" */ '@/components/home/Records.vue'),
      }, {
        path: 'addrecord',
        component: () => import(/* webpackChunkName: "home/addrecord" */ '@/components/home/AddRecord.vue'),
      }, {
        path: 'accounts',
        component: () => import(/* webpackChunkName: "home/accounts" */ '@/components/home/Accounts.vue'),
      },{
        path: '/',
        component: () => import(/* webpackChunkName: "home/main" */ '@/components/HomeMain.vue'),
      }],
    },
    {
      path: '/setting',
      // name: 'setting',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "setting" */ '@/components/setting/Setting.vue'),
      children: [{
        path: 'groups',
        component: () => import(/* webpackChunkName: "setting/groups" */ '@/components/setting/Groups.vue'),
      }, {
        path: 'products',
        component: () => import(/* webpackChunkName: "setting/products" */ '@/components/setting/Products.vue'),
      },{
        path: '/',
        component: () => import(/* webpackChunkName: "setting/settingMain" */ '@/components/setting/SettingMain.vue'),
      }],
    }
  ]
})
