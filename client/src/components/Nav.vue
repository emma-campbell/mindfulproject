<template>
  <b-navbar class="navbar gradient-dark" id="nav">
    <template slot="brand">
     <b-navbar-item tag="router-link" :to="{ path : '/' }">
       <img class="image" id="logo" src="@/assets/logo-sm.png">
      </b-navbar-item>
    </template>

    <template slot="start"></template>

    <template slot="end">
      <b-navbar-item tag="div">
            <router-link :to="{ path : '/login' }">
              <div class="button" id="login">
                <strong>Log In</strong>
              </div>
            </router-link>
          </b-navbar-item>
      <b-navbar-item tag="div">
        <router-link :to="{ path : '/register' }">
          <div class="button" id="register">
            <strong>Register</strong>
          </div>
        </router-link>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script lang="ts">
export default {
  name: 'nav',
};
</script>

<style lang="scss">

#logo {
    min-width: 75px;
    min-height: 75px;
}


#register {
    background-color: #D584FF;

    border-color: #8C00B6;
    border-radius: 4px;

    color: white;
}
</style>
