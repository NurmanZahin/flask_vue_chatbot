<template>
  <div id="app">
    <Chatbox />
  </div>
</template>

<script>
import Chatbox from "./components/Chatbox.vue";

export default {
  name: "App",
  components: {
    Chatbox,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
