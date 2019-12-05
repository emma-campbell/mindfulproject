<template>
  <b-navbar>
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        Mindful
      </b-navbar-item>
    </template>
    <template slot="start"></template>
    <template slot="end">
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-primary" tag="router-link" :to="{ path : '/register'}">
            Register
          </a>
          <a class="button" tag="router-link" :to="{ path : '/login'}">
            Log In
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script lang="ts">
export default {
  name: 'nav',
};
</script>
