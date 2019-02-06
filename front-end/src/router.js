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
        path: 'group',
        component: () => import(/* webpackChunkName: "home/managegroup" */ '@/components/GroupManage.vue'),
      },{
        path: 'staff',
        component: () => import(/* webpackChunkName: "home/manageuser" */ '@/components/StaffManage.vue'),
      },{
        path: 'clerk',
        component: () => import(/* webpackChunkName: "home/manageuser" */ '@/components/ClerkManage.vue'),
      },{
        path: 'orderlist',
        component: () => import(/* webpackChunkName: "home/orrderlist" */ '@/components/OrderList.vue'),
      },{
        path: 'order',
        component: () => import(/* webpackChunkName: "home/order" */ '@/components/OrderDetail.vue'),
      },{
        path: '/*',
        component: () => import(/* webpackChunkName: "home/*" */ '@/components/MainHome.vue'),
      }],
    },
  ]
})
