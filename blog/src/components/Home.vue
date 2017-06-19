<template>
  <div class="post">
    <div class="loading" v-if="loading">
      <h1>Закгрузка...</h1>
    </div>
    <div v-if="error" class="error">
      {{ error }}
    </div>
    <div v-for="post in orderBy(posts, 'date', -1)">
      <h1>{{ post.title }}</h1>
      <p>Опубликована: {{ post.date }}</p>
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
      posts: null,
      loading: false,
      error: null
    }
  },
  methods: {
    getAllPosts: function () {
      this.error = this.posts = null
      this.loading = true
      this.$http.get('/api/posts').then(res => {
        this.loading = false
        this.posts = res.body.posts
      }, res => {
        console.log(res)
        if (res.body === null) {
          this.error = 'Нет постов'
        }
      })
    }
  },
  created: function () {
    this.getAllPosts()
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
