<template>
<div>
    <h1>{{title}}</h1>
</div>
</template>

<script>
export default {
  name: 'contacts',
  data () {
    return {
      title: 'Contacts',
      contacts: null
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}

a {
  color: #42b983;
}
</style>
