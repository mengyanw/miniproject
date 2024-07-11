<template>
  <div class="post-container">
    Top 3 fan posts with {{ sentimentLabel }} sentiment
    <select v-model="sentimentLabel">
      <option v-for="option in options" v-bind:value="option.value">
        {{ option.text }}
      </option>
    </select>
    <ul class="post-list">
      <li
        v-for="post in store.topNPosts[sentimentLabel]"
        :key="post.id"
        data-test="post"
        class="post"
      >
        Engagement: {{ post.engagement }}
        <Tweet :tweet-id="post.medium_id" cards="hidden" width="500" />
      </li>
    </ul>
  </div>
</template>

<script setup>
import { store } from "../store.js";
import Tweet from "vue-tweet";
</script>

<script>
export default {
  data() {
    return {
      sentimentLabel: "positive",
      options: [
        { text: "Positive", value: "positive" },
        { text: "Neutral", value: "neutral" },
        { text: "Negative", value: "negative" },
      ],
    };
  },
  async mounted() {
    await store.getTopNPosts();
  },
};
</script>

<style scoped>
.post-list {
  width: 300px;
  height: 500px;
  overflow-y: scroll;
  list-style: none;
}
.post-container {
  display: flex;
  flex-direction: row;
}

.post {
  padding-bottom: 10px;
}
</style>
