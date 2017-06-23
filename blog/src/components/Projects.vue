<template>
<div>
  <h1>{{ title }}</h1>
  <div class="loading" v-if="loading">
    <h1>Loading...</h1>
  </div>
  <div class="card-project" v-for="rep in repos">
    <div class="header">
      <h4>{{ rep.name }}</h4>
      <p>{{ rep.lang }}</p>
    </div>
    <div class="container">
      <p>{{ rep.description }}</p>
      <p>Updated: {{ rep.updated_at }}</p>
    </div>
    <div class="footer">
      <a :href="rep.homepage" target="_blank">Demo</a>
      <a :href="rep.url" target="_blank">GitHub</a>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    name: 'projects',
    data () {
      return {
        title: 'Projects',
        repos: null,
        loading: false,
        error: null
      }
    },
    methods: {
      getAllRepos: function () {
        this.error = this.repos = null
        this.loading = true
        this.$http.get('/api/repos').then(res => {
          this.loading = false
          this.repos = res.body.repos
        }, res => {
          console.log(res)
          if (res.body === null) {
            this.error = 'Not repository'
          }
        })
      }
    },
    created: function () {
      this.getAllRepos()
    }
  }
</script>

<style scoped>
  .card-project {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 40%;
    border-radius: 5px;
    display: inline-block;
    margin: 1em;
  }
  .card-project:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }
  .container {
    padding: 2px 16px;
  }
</style>
