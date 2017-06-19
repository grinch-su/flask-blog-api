<template>
  <div id="app">
    <router-link v-bind:to="'/'">Blog</router-link>
    <router-link v-bind:to="'/projects'">Projects</router-link>
    <router-link v-bind:to="'/contacts'">Contacts</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Post from './components/Post.vue'
import Projects from './components/Projects.vue'
import Contacts from './components/Contacts.vue'

export default {
  name: 'app',
  components: {
    Home, Post, Projects, Contacts
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .router-link-exact-active {
    color: aqua;
  }
  h1, h2 {
  font-weight: normal;
  }
  a {
  color: #42b983;
  }
</style>
