import Vue from 'vue'
import Router from 'vue-router'
import Posts from '@/components/Posts.vue'
import Post from '@/components/Post.vue'
import Admin from '@/components/Admin.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'posts',
      component: Posts
    },
    {
      path: '/post',
      name: 'post',
      component: Post
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin
    }
  ]
})
