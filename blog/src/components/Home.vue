<template>
  <div class="post">
    <div class="loading" v-if="loading">
      <h1>Loading...</h1>
    </div>
    <div v-if="error" class="error">
      {{ error.status }},{{ error.statusText }}
    </div>
    <h1 class="not-posts" v-if="posts === null">Not posts</h1>
    <div v-for="post in orderBy(posts, 'date', -1)">
      <h1>{{ post.title }}</h1>
      <p>Published: {{ post.date }}</p>
      <p>{{ post.content | truncate(70) }}</p>
      <router-link :to="{ name: 'post', params: { id: post.id }}">read more...</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      title: 'Posts',
      posts: [],
      loading: false,
      error: null
    }
  },
  methods: {
    getAllPosts: function () {
      this.error = null
      this.loading = true
      this.$http.get('/api/posts').then(res => {
        this.loading = false
        this.posts = res.body.posts
      }, err => {
        this.error = err
      })
    }
  },
  created: function () {
    this.getAllPosts()
    document.title = this.title
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .not-posts {
    color: rgba(120, 124, 129, 0.51);
  }
  .error {
    color: #ee2735;
  }
</style>
