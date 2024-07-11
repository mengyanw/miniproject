<template>
  <a-col class="post-container">
    <div style="line-height: 20px; padding-bottom: 40px">
      with
      <select v-model="sentimentLabel" size="small">
        <option value="positive">positive</option>
        <option value="neutral">neutral</option>
        <option value="negative">negative</option>
      </select>
      sentiment
    </div>
    <a-list item-layout="horizontal">
      <a-list-item
        v-for="post in store.topNPosts[sentimentLabel]"
        :key="post.id"
        data-test="post"
        class="post"
      >
        Engagement: {{ post.engagement }}
        <Tweet :tweet-id="post.medium_id" cards="hidden" />
      </a-list-item>
    </a-list>
  </a-col>
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
</style>
