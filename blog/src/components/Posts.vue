<template>
  <div class="post">
    <div v-for="post in posts">
      <h1>{{ post.title }}</h1>
      <p>{{ post.date }}</p>
      <p>{{ post.edit_date }}</p>
      <p>{{ post.content }}</p>
      <a href="#">read more...</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'posts',
  data () {
    return {
      title: 'Posts',
      posts: [],
      urlPosts: 'http://localhost:5000/'
    }
  },
  methods: {
    getAllPosts: function () {
      this.$http.get(this.urlPosts + 'posts').then(function (res) {
        this.posts = res.body
      }, function (err) {
        console.log(err)
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
