<template>
  <div class="post">
    <div class="loading" v-if="loading > 1">
      <h1> {{ $t('loading') }}...</h1>
    </div>
    <div v-if="error" class="error">
      {{ error.status }},{{ error.statusText }}
    </div>
    <h1 class="not-posts" v-if="posts === null">{{ $t('not_posts') }}</h1>
    <div class="card-blog" v-for="post in orderBy(posts, 'date', -1)">
      <div class="card-header">
        <router-link :to="{ name: 'post', params: { id: post.id }}">
          <h1>{{ post.title }}</h1>
        </router-link>
        <p>{{ $t('post.published') }}: {{ post.date }}</p>
      </div>
      <div class="card-container">
        <p>{{ post.content | truncate(70) }}</p>
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .not-posts {
    color: rgba(120, 124, 129, 0.51);
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
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    border-radius: 2px;
    display: inline-block;
    margin: 0.5em;
    padding: 1em;
    animation: fadein 2s;
  }

  .card-header a {
    color: #000000;
    text-decoration: none;
  }

  .card-header a:hover {
    color: #575757;
    text-decoration:none;
    cursor:pointer;
  }

  .card-footer .button {
    background-color: #606060;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.6s;
    border-radius: 2px;
    padding: 1%;
    text-decoration: none;
    color: #ffffff;
  }

  .card-footer .button:hover {
    background-color: black;
    box-shadow: 0 8px 16px 0 rgb(0, 0, 0);
  }
</style>
