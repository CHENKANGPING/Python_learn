<script setup>
import {useUserStore} from '@/stores/user.js'

const userStore = useUserStore();

const onSubmit = () => {
  setTimeout(() => {
    let user = {
      username: 'ckp',
      email: 'ckp@qq.com',
      is_active: true,
    }
    userStore.setUser(user)
  }, 1000)
}
</script>

<template>
  <button @click="onSubmit">登录</button>
</template>

<style scoped></style>