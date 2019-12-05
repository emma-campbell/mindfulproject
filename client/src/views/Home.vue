<template>
  <div id="home">
    <header>
      <Nav/>
    </header>

    <p>Hello</p>
  </div>
</template>

<script lang="ts">
import Nav from '@/components/Nav.vue';

export default {
  name: 'home',
  components: { Nav },
};
</script>
