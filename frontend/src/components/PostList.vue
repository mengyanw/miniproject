<template>
    <button @click="getPosts">Refresh</button>
    <ul>
        <li v-for="post in posts" :key="post.id" data-test="post">
            {{ post.description }}
        </li>
    </ul>
</template>

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
            this.posts = await response.data
            console.log(response, this.posts)
        }
    }
}
</script>