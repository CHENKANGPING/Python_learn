<script setup>
import {ref} from "vue";

let person1 = ref('ckp');
let person2 = ref('zj');
let person3 = ref('hyf');

</script>

<template>
  <div class="base-layout">
    <header>
      <slot name="header" :person="person1"></slot>
    </header>
    <main>
      <slot :person="person2"></slot>
    </main>
    <footer>
      <slot name="footer" :person="person3"></slot>
    </footer>
  </div>
</template>

<style scoped>
.base-layout {
  background-color: antiquewhite;
}
</style>