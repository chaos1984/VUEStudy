import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import routers from './routers'
import store from './store'
import axios from "axios"


Vue.use(VueRouter)
Vue.prototype.$axios = axios

Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  routes: routers
  })

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
