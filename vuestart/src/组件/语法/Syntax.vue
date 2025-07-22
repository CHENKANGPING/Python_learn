<script setup>
import {reactive, ref, watch} from "vue";

let username = ref("ckp")
let code = ref("<h1 style='background-color: pink;'>欢迎</h1>")
let classname = ref('box')
let age = 20
let weather = 'rain'
const books = reactive([
  {'name': '三国演义', 'author': '罗贯中'},
  {'name': '水浒传', 'author': '施耐庵'},
  {'name': '西游记', 'author': '吴承恩'},
  {'name': '红楼梦', 'author': '曹雪芹'}
])

let person = reactive({
  username: "ckp",
  age: 100
})

let book_names = ref(["红楼梦", "水浒传", "三国演义", "西游记"])

let count = ref(0);

let usernameInput = ref();

let university = ref("");
let category = ref(0);

const onUpdateUsername = () => {
  username.value = "zj"
}

const onUpdateBooks = () => {
  books.sort((x, y) => {
    let a = Math.random()
    let b = Math.random()
    return a - b
  })
}

const onSplice = () => {
  // 1.添加元素
  books.splice(1, 0, {name: "ckp", author: "ckp"})
  // 2.删除元素
  books.splice(1, 2)
  // 3.替换元素
  books.splice(1, 1, {name: "ckp", author: "ckp"})
}

const onReplaceBooks = () => {
  book_names.value = ['ckp', 'zj', 'hyf']
}

const onUpdateCount = (step, event) => {
  count.value += step;
  console.log(event);
}

const gotoWebsite = (event) => {
  // 阻止默认行为
  // event.preventDefault();
  window.location = "https://www.360.com"
}

const onShowUsername = () => {
  console.log(usernameInput.value.value);
}

const onLogUniversity = () => {
  console.log(university.value);
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
      <td>{{ index + 1 }}</td>
      <td>{{ book.name }}</td>
      <td>{{ book.author }}</td>
    </tr>
    </tbody>
  </table>

  <div>
    <p v-for="(value,key) in person">键:{{ key }}, 值:{{ value }}</p>
  </div>

  <div v-for="book in books" :key="book.name">
    <label>{{ book.name }}</label>
    <input type="text" v-bind:placeholder="book.name">
  </div>
  <button @click="onUpdateBooks">更新</button>
  <button @click="onSplice">splice</button>

  <div>
    <span v-for="book in book_names">{{ book }},</span>
  </div>
  <button @click="onReplaceBooks">替换数组</button>

  <div>
    <p>count:{{ count }}</p>
    <button @click="onUpdateCount(8,$event)">更新count</button>
  </div>

  <div>
    <a href="https://www.baidu.com" @click.prevent="gotoWebsite($event)">百度</a>
  </div>

  <div>
    <input ref="usernameInput" type="text"/>
    <button @click="onShowUsername">获取用户名</button>
  </div>

  <div>
    <input type="text" v-model="university">
    <button @click="onLogUniversity">输出大学</button>
  </div>

  <div>
    <select v-model="category">
      <option value="1">python</option>
      <option value="2">JS</option>
    </select>
    <p>分类为{{ category }}</p>
  </div>

</template>

<style scoped>
.box {
  background-color: aqua;
}

</style>