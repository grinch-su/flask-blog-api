// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import resource from 'vue-resource'
import VueQuillEditor from 'vue-quill-editor'
import Vue2Filters from 'vue2-filters'
import Icon from 'vue-awesome/components/Icon'
import VueI18n from 'vue-i18n'
import App from './App'
import router from './router'

Vue.use(Vue2Filters)
Vue.use(resource)
Vue.use(VueQuillEditor)
Vue.use(VueI18n)
Vue.component('icon', Icon)

Vue.config.productionTip = false

const messages = {
  en: {
    nav: {
      blog: 'Blog',
      projects: 'Projects',
      contacts: 'Contacts'
    },
    project: {
      updated: 'Updated',
      demo: 'Demo',
      source: 'Source'
    },
    post: {
      not_posts: 'Not posts',
      published: 'Published',
      updated: 'Updated',
      read_more: 'Read more'
    },
    contact: {
      email: 'Email',
      tg: 'Telegram'
    },
    loading: 'Loading'
  },
  ro: {
    nav: {
      blog: 'Blog',
      projects: 'Proiecte',
      contacts: 'Contacte'
    },
    project: {
      updated: 'Actualizat',
      demo: 'Demonstrație',
      source: 'Sursă'
    },
    post: {
      not_posts: 'Nu există articole',
      published: 'Publicat',
      updated: 'Actualizat',
      read_more: 'Citeste mai departe'
    },
    contact: {
      email: 'Poştă electronică',
      tg: 'Telegram'
    },
    loading: 'încărcare'
  },
  ru: {
    nav: {
      blog: 'Блог',
      projects: 'Проекты',
      contacts: 'Контакты'
    },
    project: {
      updated: 'Обновлено',
      demo: 'Демонстрация',
      source: 'Исходники'
    },
    post: {
      not_posts: 'Нет постов',
      published: 'Опубликован',
      updated: 'Обновлен',
      read_more: 'Читать дальше'
    },
    contact: {
      email: 'Почта',
      tg: 'Телеграм'
    },
    loading: 'Загрузка'
  }
}

const i18n = new VueI18n({
  locale: 'en',
  messages
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  i18n,
  router,
  template: '<App/>',
  components: {
    App, Icon
  }
})
