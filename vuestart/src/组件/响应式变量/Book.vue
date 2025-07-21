<script setup>
import {onUpdated, reactive} from "vue";

// reactve:不能用来定义基本数据类型的相应式变量
// let username = reactive("ckp")
// reactive：可以用来定义复合类型的响应式变量（数组 对象）
let author = reactive({
  username: "ckp",
  age: 22
})

let books = reactive([
  {name: '水浒传', author: '施耐庵'},
  {name: '三国演义', author: '罗贯中'},
])

const onUpdateAuther = () => {
  // author.username = 'zj';
  Object.assign(author, {'username': 'hyf', age: 24})
}

const onUpdateBook = () => {
  // books[0].name = '金瓶梅'
  Object.assign(books, [
    {name: '三国演义', author: '罗贯中'},
    {name: '水浒传', author: '施耐庵'},
  ])
}

</script>

<template>
  <div>
    <h1>作者名:{{ author.username }}.年龄:{{ author.age }}</h1>
    <button @click="onUpdateAuther">更新作者</button>
  </div>

  <div>
    <p>图书名：{{ books[0].name }}, 作者：{{ books[0].author }}</p>
    <button @click="onUpdateBook">更新图书</button>
  </div>

</template>

<style scoped>

</style>