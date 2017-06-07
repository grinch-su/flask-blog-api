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
      <p>Опубликована: {{ post.date | ago }}</p>
      <p>{{ post.content | truncate(30) }}</p>
      <router-link :to="{ name: 'post', params: { id: post.id }}">read more...</router-link>
    </div>
 
    <router-view class="view"></router-view>

  </div>
</template>
<script>
export default {
  name: 'home',
  data () {
    return {
      posts: null,
      loading: false,
      error: null,
      urlPosts: 'http://localhost:5000/'
    }
  },
  methods: {
    getAllPosts: function () {
      this.error = this.posts = null
      this.loading = true
      this.$http.get(this.urlPosts + 'posts').then(res => {
        this.loading = false
        this.posts = res.body
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
h1, h2 {
  font-weight: normal;
}

a {
  color: #42b983;
}
</style>
