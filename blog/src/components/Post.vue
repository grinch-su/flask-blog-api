<template>
  <div>
  <div class="error" v-if="error">
    <h1>Error {{ error.status }}, {{ error.statusText }}</h1>
  </div>
  <div class="post" :key="post.id">
    <h1>{{ post.title }}</h1>
    <p v-if="post.date">{{ $t('post.published') }}: {{ post.date }}</p>
    <p v-if="post.edit_date">{{ $t('post.updated') }}: {{ post.edit_date }}</p>
    {{ post.content }}
  </div>
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
  watch: {
    '$route': 'getPost'
  },
  methods: {
    getPost: function () {
      this.loading = true
      this.$http.get('/api/post/' + this.$route.params.id).then(res => {
        this.loading = false
        this.post = res.body.post
        document.title = this.post.title
      }, err => {
        this.error = err
      })
    }
  },
  created () {
    this.getPost()
  }
}
</script>

<style scoped>

  .error {
    color: rgba(11, 116, 238, 0.93);
  }
  .post {
    animation: fadein 2s;
  }

</style>
