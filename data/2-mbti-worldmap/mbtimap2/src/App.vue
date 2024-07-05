<template>
  <div id="app">
    <MainContent></MainContent>
  </div>
</template>

<script>
import MainContent from './components/MainContent.vue';

export default {
  name: 'App',
  components: {
    MainContent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>