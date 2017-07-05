<template>
  <div class="posts">
    <div class="loading" v-if="loading">
      <h1> {{ $t('loading') }}...</h1>
    </div>
    <div v-if="error" class="error">
      {{ error.status }},{{ error.statusText }}
    </div>
    <h1 class="not-posts" v-if="posts === null">{{ $t('post.not_posts') }}</h1>
    <div class="card-blog" v-for="post in orderBy(posts, 'date', -1)">
      <div class="card-header">
        <router-link :to="{ name: 'post', params: { id: post.id }}">
          <h1>{{ post.title }}</h1>
        </router-link>
        <p>{{ $t('post.published') }}: {{ post.date }}</p>
      </div>
      <div class="card-content">
        <p>{{ post.content | truncate(100) }}</p>
      </div>
      <div class="card-footer">
        <router-link class="button" :to="{ name: 'post', params: { id: post.id }}">
          {{ $t('post.read_more') }}
        </router-link>
      </div>
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
  }
}

</script>

<style scoped>
  .not-posts {
    color: rgba(167, 155, 155, 0.84);
    text-align: center;
  }

  .loading {
    text-align: center;
  }

  .error {
    color: #ee2735;
  }

  .card-blog {
    background-color: white;
    width: 60%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
    border-radius: 2px;
    display: inline-block;
    position: relative;
    margin: 0.5%;
    height: 240px;
    padding: 1.5%;
  }
  .card-blog:hover {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }
  .card-header {
    height: 25%;
  }
  .card-header a {
    color: #575757;
    text-decoration: none;
  }

  .card-header a:hover {
    color: #000000;
  }
  .card-content {
    height: 46%;
    padding-top: 2%;
    padding-bottom:2%;
  }
  .card-footer {
    height: 25%;
  }
</style>
