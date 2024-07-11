<script setup>
import PostList from "./components/PostList.vue";
import TimeSeriesChart from "./components/TimeSeriesChart.vue";
import { store } from "./store.js";
</script>

<script>
export default {
  data() {
    return {
      options: [
        { text: "fan", value: "fan" },
        { text: "stadium", value: "stadium" },
        { text: "branded", value: "branded_without_fans" },
      ],
    };
  },
};
</script>

<template>
  <select
    v-model="store.postType"
    @change="store.setPostType($event.target.value)"
  >
    <option v-for="option in options" v-bind:value="option.value">
      {{ option.text }}
    </option>
  </select>
  <PostList />
  <TimeSeriesChart />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
