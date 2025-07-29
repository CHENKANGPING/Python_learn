import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const USER_KEY = "OA_USER_KEY";
const TOKEN_KEY = "OA_TOKEN_KEY";

export const useAuthStore = defineStore('auth', () => {
    let _user = ref({});
    let _token = ref({});

    function setUerToken(user, token) {
        // 保存到对象上(内存中)
        _user.value = user;
        _token.value = token;

        // 存储到浏览器的localStorge(硬盘上)
        localStorage.setItem(USER_KEY, JSON.stringify(user));
        localStorage.setItem(TOKEN_KEY, token);
    }

    // 计算属性
    let user = computed(() => {
        // 如果_user是一个空对象，那么就视图从localStorge中获取
        if(!_user.value){
            _user.value = localStorage.getItem(USER_KEY);
        }
        return _user.value;
    });
    // 计算属性
    let token = computed(() => {
        // 如果_token是一个空对象，那么就视图从localStorge中获取
        if(!_token.value){
            _token.value = localStorage.getItem(TOKEN_KEY);
        }
        return _token.value;
    });
    // 想要让外面访问，就必须要返回
    return {setUerToken,user,token}
})
