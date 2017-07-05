import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Post from '@/components/Post.vue'
import NotFound from '@/components/error/404.vue'
import Projects from '@/components/Projects.vue'
import Contacts from '@/components/Contacts.vue'
import Admin from '@/components/admin.vue'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'home', component: Home, meta: {title: 'Home'} },
    { path: '/post/:id', name: 'post', component: Post },
    { path: '/projects', name: 'projects', component: Projects },
    { path: '/contacts', name: 'contacts', component: Contacts },
    { path: '/admin', name: 'admin', component: Admin },
    { path: '/404', name: '404', component: NotFound },
    { path: '*', redirect: '/404' }
  ]
})
