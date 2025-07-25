import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // setup
  const count = ref(0)
  const project = ref('篮球比赛')
  const doubleCount = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  // 如果使用setup（组合式API），那么必须返回变量，计算属性，和方法，没有返回的
  // 外面就用不了
  return { count, doubleCount, increment, project }
})
