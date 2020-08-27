import Layout from './components/Layout'

const routers = [
  {
    path: '/',
    component: Layout
  },
  {
      path: './Layout',
      name: 'Layout',
      component: Layout
  },
  {
    path: './Upload',
    component: () => import('./components/UploadFile'),
  },  
  {
      path: './Stepper',
      component: () => import('./components/Stepper'),
  },
]
export default routers
