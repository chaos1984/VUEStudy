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


Vue.use(VueRouter);
Vue.use(ElementUI);
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
