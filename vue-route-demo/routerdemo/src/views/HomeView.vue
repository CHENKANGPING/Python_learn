<script setup>
import TheWelcome from '../components/TheWelcome.vue'
import {onBeforeRouteLeave, onBeforeRouteUpdate} from 'vue-router'

onBeforeRouteLeave((to,from) =>{
  const  answer = window.confirm("您当前页面没有保存，是否离开？")
 if (!answer){
   return false;
 }
})


</script>

<template>
  <main>
    <TheWelcome />
  </main>
</template>
