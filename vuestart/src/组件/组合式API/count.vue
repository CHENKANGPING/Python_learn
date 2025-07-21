<script setup name="com111">
import {ref} from "vue";
let count = ref(0);

function onUpdateCount(){
  count.value += 1;
}

</script>

<template>
  <div>
    <button @click="onUpdateCount">count is: {{count}}</button>
  </div>
</template>

<style scoped>

</style>