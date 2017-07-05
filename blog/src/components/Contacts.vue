<template>
  <div>
    <ul class="contacts">
      <li>
        <a href="mailto:grinchfedorov@gmail.com"><icon name="envelope-o" scale="3"></icon></a>
      </li>
      <li>
        <a href="tg://resolve?domain=grinch_su"><icon name="telegram" scale="3"></icon></a>
      </li>
      <li>
        <a href="https://medium.com/grinch-su"><icon name="medium" scale="3"></icon></a>
      </li>
    </ul>
  </div>
</template>

<script>
  import 'vue-awesome/icons'

  export default {
    name: 'contacts',
    data () {
      return {
      }
    }
  }
</script>

<style scoped>
  .contacts li {
    display: inline-block;
    padding-right: 1%;
  }
  .contacts li a {
    color: #767676;
  }
  .contacts li a:hover {
    color: #000000;
  }
  .contacts{
    list-style: none;
    text-align: center;
  }
</style>
