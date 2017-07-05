<template>
<div>
  <div class="loading" v-if="loading">
    <h1>{{ $t('loading') }}...</h1>
  </div>
  <div class="projects">
  <div class="card-project" v-for="rep in repos">
    <div class="header">
      <h4>{{ rep.name }}</h4>
      <p>{{ rep.lang }}</p>
    </div>
    <div class="content">
      <p>{{ rep.description }}</p>
      <p>{{ $t('project.updated') }}: {{ rep.updated_at }}</p>
    </div>
    <div class="footer">
      <a class="button" :href="rep.homepage" target="_blank">{{ $t('project.demo') }}</a>
      <a class="button" :href="rep.url" target="_blank">{{ $t('project.source') }}</a>
    </div>
  </div>
    </div>
</div>
</template>

<script>
  export default {
    name: 'projects',
    data () {
      return {
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
    background-color: white;
    width: 45%;
    display: inline-block;
    position: relative;
    border-radius: 2px;
    padding: 1.5%;
    height: 250px;
    margin: 0.5%;
  }
  .loading {
    text-align: center;
  }
  .card-project:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  }
  .header{
    text-align: center;
    height: 25%;
  }
  .content {
    height: 50%;
  }
  .footer {
    height: 25%;
  }
</style>
