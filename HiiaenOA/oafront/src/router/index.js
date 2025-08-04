import {createRouter, createWebHashHistory} from 'vue-router'
import login from '../views/login/login.vue'
import frame from '../views/main/frame.vue'
import {useAuthStore} from '@/stores/auth';
import myabsent from '@/views/absent/my.vue'
import subabsent from '@/views/absent/sub.vue'

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'frame',
            component: frame,
            children: [
                {path: '/absent/my', name: 'myabsent', component: myabsent},
                {path: '/absent/sub', name: 'subabsent', component: subabsent}
            ]
        },
        {
            path: '/login',
            name: 'login',
            component: login
        }
    ]
})

router.beforeEach((to, from) => {
    const authStore = useAuthStore();
    if (!authStore.is_logined && to.name != 'login') {
        return {name: 'login'}
    }
})

export default router
