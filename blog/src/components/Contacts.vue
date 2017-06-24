<template>
<div>
  <h1>{{title}}</h1>
  <ul>
    <li>
      <a href="mailto:grinchfedorov@gmail.com">Email</a>
    </li>
    <li><a href="tg://resolve?domain=grinch_su">Telegram</a></li>
  </ul>
</div>
</template>

<script>
  export default {
    name: 'contacts',
    data () {
      return {
        title: 'Contacts'
      }
    }
  }
</script>

<style scoped>
</style>
