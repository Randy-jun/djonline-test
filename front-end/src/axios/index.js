import axios from 'axios'
import router from 'vue-router'

import Sstorage from '@/module/sstorage.js';

// axios 配置
axios.defaults.timeout = 5000
// axios.defaults.baseURL = 'http://127.0.0.1:9090'
axios.defaults.baseURL = 'http://60.205.204.124:8080';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (Sstorage.get('tonken')) {
    //   config.headers.authKey = Sstorage.get('username');
      config.headers.Authorization = Sstorage.get('username') + ':' + Sstorage.get('tonken');
        // config.headers.Authorization = {
        //     username:Sstorage.get('username'),
        //     tonken:Sstorage.get('tonken'),
        // }
    }
    return config
  },
  err => {
    return Promise.reject(err)
  },
)

// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 401 清除token信息并跳转到登录页面
          // 只有在当前路由不是登录页面才跳转
          router.currentRoute.path !== 'login' &&
            router.replace({
              path: 'login',
              query: { redirect: router.currentRoute.path },
            });
        case 403:
            console.log('您没有该操作权限');
        case 500:
            console.log('服务器错误');
      }
    }
    // console.log(JSON.stringify(error));//console : Error: Request failed with status code 402
    return Promise.reject(error.response.data)
  },
)

export default axios