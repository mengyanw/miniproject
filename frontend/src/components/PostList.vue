<script setup>
import Tweet from "vue-tweet";
</script>

<script>
import axios from "axios";
console.log(import.meta.env.VITE_API_URL);

export default {
  data() {
    return {
      sentiment_label: "positive",
      options: [
        { text: "Positive", value: "positive" },
        { text: "Negative", value: "negative" },
        { text: "Neutral", value: "neutral" },
      ],
      data: null,
      posts: null,
    };
  },
  methods: {
    async getData() {
      const response = await axios.get(
        import.meta.env.VITE_API_URL + "posts/topN/",
      );
      this.data = await response.data;
      this.updatePosts();
    },
    updatePosts() {
      this.posts = this.data[this.sentiment_label];
    },
  },
  watch: {
    sentiment_label() {
      this.updatePosts();
    },
  },
  mounted() {
    this.getData();
  },
};
</script>

<template>
  <div class="post-container">
    Top 3 fan posts with {{ sentiment_label }} sentiment
    <select v-model="sentiment_label">
      <option v-for="option in options" v-bind:value="option.value">
        {{ option.text }}
      </option>
    </select>
    <ul class="post-list">
      <li v-for="post in posts" :key="post.id" data-test="post" class="post">
        Engagement: {{ post.engagement }}
        <Tweet :tweet-id="post.medium_id" cards="hidden" width="500" />
      </li>
    </ul>
  </div>
</template>

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
