<script setup>
import { onMounted, onUpdated } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

onMounted(() => {
  const params = route.params
  console.log(params);
})

onUpdated(() => {
  const params = route.params
  console.log('updated:',params);
})
</script>

<template>
  <h1>这是新闻详情页</h1>
</template>

<style scoped></style>
