import Layout from './components/Layout'
import Echart from './components/Echart/Echart'

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
  {
    path: './Echart',
    name: 'Echart',
    component: Echart
}, 
]
export default routers
