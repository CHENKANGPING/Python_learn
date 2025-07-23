<script setup>
import {ref, watch} from "vue";
// 1.使用数组,制定属性的名称
// const props = defineProps(['username'])

// 2.使用对象,指定数组
const props = defineProps({
  username: String,
  gender: {
    type: String,
    default: '男'
  },
  body: {
    height: Number,
    weight: Number
  },
})

// 自定义事件
let step = ref(0);
const emit = defineEmits(['walk']);

const updateStep = () => {
  step.value += 1;
  // 触发事件
  emit('walk', step.value);
}

// 自定义v-model
let age = defineModel();
watch(age, (newValue, oldValue) => {
  console.log("Person组件中监听到的age:", age.value);
})

const oneBirthday = () => {
  age.value += 1;
}
</script>

<template>

  <div>
    <p>用户名:{{ props.username }}</p>
    <p>性别:{{ props.gender }}</p>
    <p>身高:{{ props.body.height }}</p>
    <p>体重:{{ props.body.weight }}</p>
  </div>

  <div>
    <p>子组件中的step:{{ step }}</p>
    <button @click="updateStep">走路</button>
  </div>

  <div>
    <button @click="oneBirthday">过一次生日</button>
  </div>
</template>

<style scoped>

</style>