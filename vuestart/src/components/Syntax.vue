<script setup>
import {reactive, ref} from "vue";

let username = ref("ckp")
let code = ref("<h1 style='background-color: pink;'>欢迎</h1>")
let classname = ref('box')
let age = 20
let weather = 'rain'
const books = reactive([
    {'name': '三国演义','author': '罗贯中'},
    {'name': '水浒传','author': '施耐庵'},
    {'name': '西游记','author': '吴承恩'},
    {'name': '红楼梦','author': '曹雪芹'}
  ])

let person = reactive({
  username:"ckp",
  age :100
})

let book_names = ref(["红楼梦", "水浒传", "三国演义", "西游记"])

const onUpdateUsername = () => {
  username.value = "zj"
}

const  onUpdateBooks = () =>{
  books.sort((x,y) => {
    let a = Math.random()
    let b = Math.random()
    return a-b
  })
}

const onSplice = () =>{
    // 1.添加元素
    books.splice(1,0,{name:"ckp",author:"ckp"})
    // 2.删除元素
    books.splice(1,2)
    // 3.替换元素
    books.splice(1,1,{name:"ckp",author:"ckp"})
}

const  onReplaceBooks = () =>{
  book_names.value = ['ckp','zj','hyf']
}
</script>

<template>

  <p v-once>{{ username }}</p>
  <div>
    <button @click="onUpdateUsername">修改username</button>
  </div>

  <div v-html="code"></div>

  <div v-bind:class="classname">蓝色生死恋</div>

  <div>{{ age > 18 ? '你可以进网吧' : '你不可以进入网吧' }}</div>

  <div v-if="weather == 'sun'">今天去公园</div>
  <div v-else-if="weather == 'rain'">今天去看电影</div>
  <div v-else>今天哪也不去</div>

  <div v-show="true">这是show的div</div>

  <table>
    <thead>
        <tr>
          <th>序号</th>
          <th>书名</th>
          <th>作者</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(book,index) in books">
            <td>{{index + 1}}</td>
            <td>{{ book.name }}</td>
            <td>{{ book.author }}</td>
        </tr>
    </tbody>
  </table>

  <div>
    <p v-for="(value,key) in person">键:{{key}}, 值:{{value}}</p>
  </div>

  <div v-for="book in books" :key="book.name">
    <label>{{book.name}}</label>
    <input type="text" v-bind:placeholder="book.name">
  </div>
  <button @click="onUpdateBooks">更新</button>
  <button @click="onSplice">splice</button>

  <div>
    <span v-for="book in book_names">{{book}},</span>
  </div>
  <button @click="onReplaceBooks">替换数组</button>

</template>

<style scoped>
.box {
  background-color: aqua;
}

</style>