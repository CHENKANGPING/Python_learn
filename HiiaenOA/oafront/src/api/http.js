import axios from 'axios';
import { useAuthStore } from '@/stores/auth';

class Http {
    constructor() {
        this.instance = axios.create({
            baseURL: import.meta.env.VITE_BASE_URL,
            timeout: 10000,
        });
        this.instance.interceptors.request.use((config) => {
            const authStore = useAuthStore();
            const token = authStore.token;
            if(token){
                config.headers['Authorization'] = 'JWT ' + token;
            }
            return config;
        })
    }

    post(path, data) {
        // path: /auth/login
        // url: http://127.0.0.1:8000/auth/login
        // return this.instance.post(path, data);
        return new Promise(async (resolve, reject) => {
            // 网络请求发送出去后，线程会挂起这个等待
            // 等网络数据到达后，线程又会回到当前位置开始后执行
            // 如果在某个函数中使用了await，那么这个函数就必须要定义成async
            // axios底层也是使用promise对象，在响应的状态码不是200时，会调用reject
            // 调用reject的结果是，外层的函数会抛出异常
            try {
                let result = await this.instance.post(path, data)
                // 如果走到下面代码，说明上面await函数没有抛出异常，就肯定说明返回的状态码是200
                resolve(result.data);
            } catch (err) {
                let detial = err.response.data.detail;
                reject(detial)
            }
        })
    }

    get(path, params) {
        return this.instance.get(path, { params });
    }
}
export default new Http();