import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import routers from './routers'
import store from './store'
import axios from "axios"

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import './assets/icon/iconfont.css'

import uploadfile from './components/UploadFile/index.js'
import stepperbtn from './components/StepperBtn/index.js'
import pdfviewer from './components/PDFViewer/index.js'
// import { config } from 'vue/types/umd';

Vue.use(VueRouter);
Vue.use(ElementUI);
Vue.use(uploadfile);
Vue.use(stepperbtn);
Vue.use(pdfviewer);


Vue.prototype.$axios = axios

Vue.config.productionTip = false

const router = new VueRouter({
  // mode: 'history',
  routes: routers
  })

new Vue({
  vuetify,
  router,
  store,
  ElementUI,
  el: '#app',
  render: h => h(App)
}).$mount('#app')

axios.interceptors.request.use(
    config=> {
      let token =sessionStorage.getItem('token')
      if (token){
        config.headers.Authorization = token
      }
      return config
    },
    (error) =>{
      return Promise.reject(error)
    }
  
)

axios.interceptors.response.use((response) => {
  if (response.config.url !== ''){
    console.log(response)
    if (response.data.status ===-6){
      alert('ID IS WRONG')
      window.location = '/login'
    }
  }
  return response
},(error)=>{
  return Promise.reject(error)
}
)