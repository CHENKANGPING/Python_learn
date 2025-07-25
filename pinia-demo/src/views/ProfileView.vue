<script setup>
import { ref , onMounted} from 'vue'
import { useUserStore } from '@/stores/user.js'
let username = ref(" ");

const userStore = useUserStore();

onMounted(() =>{
  username.value = userStore.user.username;
})

</script>

<template>
<h1>用户名:{{username}}</h1>
</template>

<style scoped>

</style>