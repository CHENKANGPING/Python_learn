// import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
//
// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     {
//       path: '/about',
//       name: 'about',
//       // route level code-splitting
//       // this generates a separate chunk (About.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import('../views/AboutView.vue'),
//     },
//   ],
// })
//
// export default router

import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  // 路由history配置
  // 1.HTML5模式: createWebHistory 传统的url
  // 2.Hash模式: createWebHashHistory #/, #/about,
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        requireAuth: false
      }
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
      meta: {
        requireAuth: true
      }
      // beforeEnter: (to, from) => {
      //   return false
      // }
    },
    {
      path: '/news',
      name: 'news',
      component: () => import('../views/news/NewsView.vue'),
      children: [
        {
          path: 'detail/:pk',
          name: 'news-detail',
          component: () => import('../views/news/NewsDetialView.vue')
        },
        {
          path: 'pub',
          name: 'news-pub',
          component: () => import('../views/news/NewsPublicView.vue')
        },
        {
          path: '/login',
          name: 'login',
          component: () => import('../views/LoginView.vue')
        }
      ]
    }
  ]
})

// 全局导航守卫
// let isAuthenticated = true;
// router.beforeEach((to, from) => {
//   // 如果没有权限，就不能跳转，要转回登录页面
//   if (!isAuthenticated && to.name != 'login') {
//     return { name: 'login' }
//   }
// })
// router.afterEach((to,from) =>{
//   console.log(to);
//   console.log(from);
// })

let isAuthenticated = false;
router.beforeEach((to, from) => {
  // 如果没有权限，就不能跳转，要转回登录页面
  if(to.meta.requireAuth==true && !isAuthenticated && to.name != 'login'){
    return {
      name:'login'
    }
  }
})

export default router
