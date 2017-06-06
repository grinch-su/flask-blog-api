<template>
  <div class="">
    <h1>{{ title }}</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'post',
  data () {
    return {
      title: 'Post title'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
