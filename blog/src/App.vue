<template>
  <div id="app">
    <ul id="nav">
      <li>
        <router-link v-bind:to="'/'">{{ $t('nav.blog') }}</router-link>
      </li>
      <li>
        <router-link v-bind:to="'/projects'">{{ $t('nav.projects') }}</router-link>
      </li>
      <li>
        <router-link v-bind:to="'/contacts'">{{ $t('nav.contacts') }}</router-link>
      </li>
    </ul>
    <label for="locale"></label>
    <select id="locale" v-model="locale">
      <option value="en">EN</option>
      <option value="ru">RU</option>
      <option value="ro">RO</option>
    </select>
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
    },
    data () {
      return {
        locale: 'en'
      }
    },
    watch: {
      locale (val) {
        this.$i18n.locale = val
      }
    }
  }
</script>

<style>
  html {
    margin: 0;
    padding: 0;
    background-color: #dddddd;
  }
  @keyframes fadein {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    padding-left: 10%;
    padding-right: 10%;
  }

  h1, h2 {
  font-weight: normal;
  }

  #nav {
    list-style-type: none;
    margin:0;
    padding:0;
    text-align: center;
  }

  #nav li {
    height: 25px;
    display: inline-block;
    margin-right: 0;
    border-right: 1px solid #303030;
    padding: 10px 10px 10px 10px;
  }
  #nav li a {
    text-decoration: none;
    color: #767676;
    font: 25px/1 Helvetica, Verdana, sans-serif;
    text-transform: uppercase;
    transition: all 0.5s ease;
  }

  #nav li:last-child {
    border-right: none;
  }

  #nav li a:hover {
    color: #666;
  }

  #nav .router-link-exact-active{
    font-weight: bold;
    color: #333;
  }
  #locale {
    appearance: none;
    background-color: #000;
    color: white;
    padding: 3px;
    font: 16px/1 Helvetica, Verdana, sans-serif;
  }
</style>
