import Layout from './components/Layout'

const routers = [
  {
    path: '/', // 去掉前面的点，用于前端调试
    component: Layout
  },
  {
      path: './Layout',
      name: 'Layout',
      component: Layout
  }, 
  // {
  //     path: './Stepper',
  //     component: () => import('./components/Stepper'),
  // },
]
export default routers
