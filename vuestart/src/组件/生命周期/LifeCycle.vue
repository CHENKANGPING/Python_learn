<script setup>
import {ref, onBeforeMount, onMounted, onUpdated, onBeforeUpdate, onBeforeUnmount, onUnmounted} from "vue";

let count = ref(0);

// 1.创建阶段
console.log("setup");
const updateCount = () =>{
  count.value += 1;
}

// 2.挂载阶段
onBeforeMount(() =>{
  console.log('before mount');
})

onMounted(() =>{
  console.log('mounted');
})

// 3.更新阶段
onBeforeUpdate(() =>{
  console.log("before update");
})

onUpdated(() =>{
  console.log("updated")
})

// 4.卸载阶段
onBeforeUnmount(() =>{
  console.log("before unmount")
})

onUnmounted(() =>{
  console.log("Unmounted")
})


</script>

<template>
  <p>{{count}}</p>
  <button @click="updateCount">更新count</button>

</template>

<style scoped>

</style>