<template>
  <div class="header">
    <b-navbar toggleable type="dark" variant="info">
      <b-navbar-brand>AI Chatbot</b-navbar-brand>

      <b-navbar-toggle target="navbar-toggle-collapse">
        <template v-slot:default="{ expanded }">
          <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
          <b-icon v-else icon="chevron-bar-down"></b-icon>
        </template>
      </b-navbar-toggle>

      <b-collapse id="navbar-toggle-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item
            target="_blank"
            href="https://www.linkedin.com/in/nurman-jupri-20655814a/"
            >LinkedIn</b-nav-item
          >
          <b-nav-item target="_blank" href="https://github.com/NurmanZahin"
            >Github</b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
export default {
  data: () => ({
    activeItem: 0,
  }),
};
</script>

