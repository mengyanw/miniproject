<script setup>
import Tweet from "vue-tweet";
</script>

<script>
import axios from 'axios'
console.log(import.meta.env.VITE_API_URL)

export default {
    data() {
        return {
            posts: null
        }
    },
    watch: {
        '$store.state.list': {
            handler() {
                this.getPosts();
            },
            immediate: true,
        }
    },
    methods: {
        async getPosts() {
            const response = await axios.get(import.meta.env.VITE_API_URL + 'posts/')
            this.posts = await response.data.slice(0, 3)
            console.log(response, this.posts)
        }
    }
}
</script>

<template>
    <button @click="getPosts">Refresh</button>
    <div class="post-container">
        <ul class="post-list">
            <li v-for="post in posts" :key="post.id" data-test="post" class="post">
                Sentiment: {{ post.sentiment_label }},  {{ post.sentiment_score }}
                <Tweet :tweet-id="post.medium_id" cards="hidden" width="500"/>
            </li>
        </ul>
    </div>

</template>

<style scoped>
    .post-list {
        width: 500px;
        height: 500px;
        overflow-y: scroll;
        list-style: none;
    }
    .post-container {
        display: flex;
        flex-direction: row;
    }

    .post {
        padding-bottom: 50px;
    }
</style>