<script setup>
import Person from "@/组件/自定义组件/Person.vue";
import {ref, watch} from "vue";
import SubmitButton from "@/组件/自定义组件/SubmitButton.vue";
import BaseLayout from "@/组件/自定义组件/BaseLayout.vue";


let name = 'zj';
let age = ref(1);
watch(age, (value) => {
  console.log('MyComponent监听到的age:', age.value)
})

const personWalk = (step) => {
  console.log("父组件得到的step:", step);
}

const updateAge = () => {
  age.value += 1;
}
</script>

<template>
  <Person v-model="age" :body="{height:180,weight:180}" :username="name" gender="女" @walk="personWalk"></Person>
  <button @click="updateAge">MyComponent修改age</button>
  <SubmitButton>登录</SubmitButton>
  <BaseLayout>
    <template #header>
      <ul>
        <li><a href="#">首页</a></li>
        <li><a href="#">博客</a></li>
      </ul>
    </template>
    <h1>这是main里的内容</h1>
    <template #footer>
      北京百度科技有限公司
    </template>
  </BaseLayout>

  <br>

  <BaseLayout>
    <template #header="scope">
      <ul>
        <li><a href="#">首页</a></li>
        <li><a href="#">博客</a></li>
      </ul>
      <p>{{ scope.person }}</p>
    </template>

    <template #default="scope">
      <h1>这是mian里的内容</h1>
      <P>{{ scope.person }}</P>
    </template>

    <template #footer="scope">
      北京百度科技有限公司
      <P>{{ scope.person }}</P>
    </template>
  </BaseLayout>
</template>

<style scoped>

</style>