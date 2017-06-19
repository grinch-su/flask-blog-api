<template>
  <div class="" :key="post.id">
    <h1>{{ post.title }}</h1>
    <p>Date created:{{ post.date }}</p>
    <p>Date edit:{{ post.edit_date }}</p>
    <p>{{ post.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'post',
  data () {
    return {
      loading: false,
      post: {},
      error: null,
      url: 'post/'
    }
  },
  created () {
    this.getPost()
  },
  watch: {
    '$route': 'getPost'
  },
  methods: {
    getPost: function () {
      this.loading = true
      this.$http.get('/api/post/' + this.$route.params.id).then(res => {
        this.loading = false
        this.post = res.body.post
      }, res => {
        this.error = res.body
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
