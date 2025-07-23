<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router';
import { onMounted } from 'vue';

const route = useRoute();

onMounted(() =>{
  const query = route.query;
  console.log(query);
})

</script>

<template>
  <ul>
    <li>
      <router-link to="/news/detail/1">新闻1</router-link>
    </li>
    <li>
      <router-link :to="{ name: 'news-detail', params:{pk:2}}">新闻2</router-link>
    </li>
    <li>
      <router-link :to="{ name: 'news-pub' }">发布</router-link>
    </li>
  </ul>
  <RouterView></RouterView>
</template>

<style scoped></style>
