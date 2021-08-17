// import VueRouter from 'vue-router'
import Layout from './components/Layout'
import UserLogin from './components/UserLogin'
import Register from './components/UserLogin/Register'
// import Echart from './components/Echart/Echart'

const routers = [
  {
    path: '/', // 去掉前面的点，用于前端调试
    redirect: '/UserLogin',

  },
  {
    path: '/UserLogin',
    name: 'UserLogin',
    component: UserLogin
  }, 
  {
    path: '/Register',
    name: 'Register',
    component: Register
  }, 
  {
    path: '/Layout',
    name: 'Layout',
    component: Layout,
    beforeEach:(to , from ,next)=>{
      next(false)
    }
  }, 
  {
    path: '**',   // 错误路由
    redirect: '/UserLogin'   //重定向
  },
]
// const router = new VueRouter({
//   mode:'history',
//   routers
// })

// //挂载路由导航守卫
// //如果没有登录，就跳转到登陆页面
// router.beforeEach((to,from,next)=>{
//     //to将要访问的页面
//     //from从哪个路径跳转而来
//     //next是一个函数，表示放行
//     //next() 放行  next('/login')强制跳转
//     console.log('navigation-guards');
//     const nextRoute = ['Layout'];
    
//     if (to.path==='/UserLogin'){
//         return next(false);
//     }
//     //获取token
//     const tokenStr = window.sessionStorage.getItem('token');
//     console.log("tokenStr")
//     console.log(tokenStr)
//     if (nextRoute.indexOf(to.name)){
//       if(!tokenStr){
//           return next('/UserLogin');
//       }else{
//           next('/Layout');
//       }
//     }
// })
export default routers
