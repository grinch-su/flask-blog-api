<template>
  <div>
    <label for="username">Username: <input id="username" type="text"></label>
    <label for="password">Password: <input id="password" type="password"></label>
  </div>
</template>

<script>
  export default {
    name: 'admin',
    data () {
      return {
        title: 'Admin panel',
        username: null,
        password: null
      }
    }
  }
</script>

<style scoped>

</style>
