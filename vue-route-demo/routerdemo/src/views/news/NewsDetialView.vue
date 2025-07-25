<script setup>
import { onMounted, onUpdated } from 'vue';
import { onBeforeRouteUpdate, useRoute, onBeforeRouteLeave } from 'vue-router'

const route = useRoute();

onMounted(() => {
  const params = route.params
  console.log(params);
})

onUpdated(() => {
  const params = route.params
  console.log('updated:',params);
})

onBeforeRouteUpdate((to,from) =>{
  console.log(to);
  console.log(from);
})
</script>

<template>
  <h1>这是新闻详情页</h1>
</template>

<style scoped></style>
