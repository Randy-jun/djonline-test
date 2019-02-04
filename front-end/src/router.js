import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      name: 'home',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Home" */ '@/views/Home.vue'),
      children: [{
        path: 'managegroup',
        component: () => import(/* webpackChunkName: "home/managegroup" */ '@/components/GroupManage.vue'),
      },{
        path: 'manageuser',
        component: () => import(/* webpackChunkName: "home/manageuser" */ '@/components/UserManage.vue'),
      },{
        path: 'records',
        component: () => import(/* webpackChunkName: "home/records" */ '@/components/RecordList.vue'),
      },{
        path: 'record',
        component: () => import(/* webpackChunkName: "home/record" */ '@/components/RecordDetail.vue'),
      },{
        path: '/*',
        component: () => import(/* webpackChunkName: "home/*" */ '@/components/MainHome.vue'),
      }],
    },
  ]
})
