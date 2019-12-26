<template>
<div id="home">
    <header>
      <Nav/>
    </header>
    <section class="hero is-fullheight is-light">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title"> Placeholder </h1>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import Nav from '@/components/Nav.vue';

export default {
  name: 'home',
  components: { Nav },
};
</script>
