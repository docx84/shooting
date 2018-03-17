<template>
  <navbar is-dark role="navigation" aria-label="main navigation">
  <navbar-brand>
    <router-link active-class="is-active" to="/home" class="navbar-item vbc">VBC</router-link>
    <router-link active-class="is-active" to="/about" class="navbar-item">Grid</router-link>
    <router-link active-class="is-active" to="/box" class="navbar-item">Box</router-link>
    <router-link active-class="is-active" to="/form" class="navbar-item">Form</router-link>
    <router-link active-class="is-active" to="/buttons" class="navbar-item">Buttons</router-link>
    <router-link active-class="is-active" to="/more" class="navbar-item">
      <icon><fa fa-plus></fa></icon>
    </router-link>
  </navbar-brand>
</navbar>
</template>
<style scoped>
  .vbc {
    font-weight: bold;
    font-family: 'Poppins', sans-serif;
  }
  .navbar {
    margin-bottom: 1em;
  }
</style>
<script>
  export default {
    name: 'm-menu'
  }
</script>