<script setup>
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { onMounted } from 'vue'

// 1.route：主要是用于获取一些参数的，路由信息
// 2. router:主要用来做一些路由跳转
const route = useRoute()
const router = useRouter()

onMounted(() => {
  const query = route.query
  console.log(query)
})

const gotoNewsDetial = () => {
  // router.push('/news/detail/1')
  // router.push({ name: 'news-detail', params: { pk: 3 } })

  router.replace({ name: 'news-detail', params: { pk: 3 } })
}
</script>

<template>
  <ul>
    <li>
      <router-link to="/news/detail/1">新闻1</router-link>
    </li>
    <li>
      <router-link :to="{ name: 'news-detail', params: { pk: 2 } }">新闻2</router-link>
    </li>
    <li>
      <router-link :to="{ name: 'news-pub' }">发布</router-link>
    </li>
    <li>
      <button @click="gotoNewsDetial">新闻详情</button>
    </li>
  </ul>
  <RouterView></RouterView>
</template>

<style scoped></style>
