// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import resource from 'vue-resource'
import VueQuillEditor from 'vue-quill-editor'
import Vue2Filters from 'vue2-filters'
import App from './App'
import router from './router'

Vue.use(Vue2Filters)
Vue.use(resource)
Vue.use(VueQuillEditor)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})
