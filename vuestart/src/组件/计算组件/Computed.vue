<script setup>
import {ref, computed} from "vue";
let width = ref(0);
let height = ref(0);
let area = computed(() => {
  return width.value * height.value;
})
</script>

<template>

  <div>
    <label>宽度:</label>
    <input type="text" v-model="width" placeholder="宽度" />
  </div>

  <div>
    <label>高度</label>
    <input type="text" v-model="height" placeholder="高度" />
  </div>

  <div>
    <label>面积</label>
    <input type="text" readonly v-model="area" />
  </div>

</template>

<style scoped>

</style>