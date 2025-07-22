<script setup>
import {ref, watch, reactive} from "vue";

let width = ref(0);
let person = ref({
  username:'ckp',
  age:18
})
let university = reactive({
  name:'清华大学',
  year:1911
})

// 1. 监听基本数据类型:width
watch(width, (newValue, oldValue) => {
  console.log("new width:", newValue);
})
const changeWidth = () =>{
  width.value += 1;
}

// 2. 监听使用ref定义的对象类型
// 2.1 监听使用ref定义的对象类型
watch(person,(newValue, oldValue) => {
  console.log("newPerson:", newValue);
})
const changePerson = () =>{
  person.value = {'username':'zj', 'age':22};
}

// 2.2 监听对象的下一个属性的改变,采用getter函数的形式
watch(() => person.value.username,(newValue, oldValue) => {
  console.log("new Person username:", newValue);
})
const changePersonUsername = () =>{
  person.value.username += '1'
}

// 2.3 监听对象下所有属性的改变,那么哟啊开启深度监听
watch(person,(newValue, oldValue) => {
  console.log("监听所有子属性的改变:", newValue);
}, {deep:true})
const changePersonAge = () =>{
  person.value.age += 1
}

// 3 监听reactive函数定义的属性
// 3.1 监听一个属性的变化
watch(() => university.name,(newValue, oldValue) => {
  console.log("新大学名称:", newValue);
})

// 3.2 监听所有属性的变化,就直接监听对象即可
// 对于使用reactive定义的响应式变量,不需要手动开启深度监听
watch(university,(newValue, oldValue) => {
  console.log("新大学名称:", newValue.name);
  console.log("新大学年份:", newValue.year);
})
const changeUniversityName = () =>{
  university.name +='1';
}

const changeUniversityYear = () =>{
  university.year += 1;
}

</script>

<template>

  <div>
    <p>宽度:{{width}}</p>
    <button @click="changeWidth">改变width</button>
  </div>

  <div>
     <p>用户名:{{person.username}}, 年龄:{{person.age}}</p>
     <button @click="changePerson">改变person</button>
     <button @click="changePersonUsername">改变personUsername</button>
     <button @click="changePersonAge">改变personAge</button>
  </div>

  <div>
    <p>大学名:{{university.name}}, 年份:{{university.year}}</p>
    <button @click="changeUniversityName">改变UniversityName</button>
    <button @click="changeUniversityYear">改变UniversityYear</button>

  </div>

</template>

<style scoped>

</style>