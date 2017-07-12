/* eslint-disable no-unused-vars */
// eslint-disable-next-line no-undef
const app = new Vue({
  el: '#api-map',
  data: {
    message: 'Hello Vue!',
    links: [],
    error: null,
    title: 'My API'
  },
  methods: {
    getMap: function () {
      this.$http.get('/api-map').then(res => {
        this.links = res.body.links
        console.log(res)
      }, res => {
        this.error = res
      })
    }
  },
  created: function () {
    this.getMap()
  }
})
