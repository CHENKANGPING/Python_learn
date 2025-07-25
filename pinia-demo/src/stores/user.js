import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  let user = ref({
    username: '',
    email: '',
    is_active: false,
  })

  const setUser = (user_obj) =>{
    user.value = user_obj;
    // 存储在本地
    localStorage.setItem('user',JSON.stringify(user_obj));
  }

  return{
    user,
    setUser
  }
})
