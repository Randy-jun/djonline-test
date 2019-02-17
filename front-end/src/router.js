import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
import Sstorage from '@/module/sstorage.js';

Vue.use(Router)

// export default new Router({
const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: Login
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      name: 'home',
      meta: {
        requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
      },
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Home" */ '@/views/Home.vue'),
      children: [{
        path: 'group',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/managegroup" */ '@/components/GroupManage.vue'),
      },{
        path: 'staff',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/manageuser" */ '@/components/StaffManage.vue'),
      },{
        path: 'clerk',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/manageuser" */ '@/components/ClerkManage.vue'),
      },{
        path: 'orderlist',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/orrderlist" */ '@/components/OrderList.vue'),
      },{
        path: 'order',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/order" */ '@/components/OrderDetail.vue'),
      },{
        path: '',
        meta: {
          requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
        },
        component: () => import(/* webpackChunkName: "home/*" */ '@/components/MainHome.vue'),
      }],
    },
  ]
})

router.beforeResolve((to, from, next) => {
  if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
    // console.log(null !== Sstorage.get('tonken'))
    if (Sstorage.get('tonken')) {  // 通过vuex state获取当前的token是否存在
      next();
    }
    else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
      });
    }
  }
  else {
      next();
  }
})

export default router;