<script setup name="Person">
//ref
import {onUpdated, ref} from "vue";

//ref函数，既可以定义基本数据类型的响应式变量（数值类型 字符串 布尔类型）
//还可以定义复合的数据类型（对象 数组）
//在script标签中 访问和修改ref函数定义的响应式变量 需要通过“变量名.value”的形式
//在template中 不需要加.value
let username = ref('ckp');
let person = ref({
  username:'hyf',
  age:'23'
})

const onUpdateUsername = () => {
  username.value = 'zj';
}

const onUpdateAge = () =>{
  person.value.age ++;
}


</script>

<template>


  <div>
    <h1>用户名为：{{username}}</h1>
    <button @click="onUpdateUsername">点击修改用户名</button>
  </div>

  <div>
    <h1>person的年龄：{{person.age}}</h1>
    <button @click="onUpdateAge">点击修改用户年龄</button>
  </div>



</template>

<style scoped>

</style>