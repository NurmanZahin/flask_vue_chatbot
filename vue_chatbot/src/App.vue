<template>
  <div id="app">
    <Header />
    <Chatbox />
  </div>
</template>

<script>
import Chatbox from "./components/Chatbox.vue";
import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {
    Chatbox,
    Header,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
