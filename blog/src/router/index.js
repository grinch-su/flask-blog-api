import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Post from '@/components/Post.vue'
import NotFound from '@/components/404.vue'
import Projects from '@/components/Projects.vue'

Vue.use(Router)
const Contacts = {
  template: '<div>Contacts</div>'
}

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/post/:id', name: 'post', component: Post },
    { path: '/projects', name: 'projects', component: Projects },
    { path: '/contacts', name: 'projects', component: Contacts },
    { path: '/404', name: '404', component: NotFound },
    { path: '*', redirect: '/404' }
  ]
})
