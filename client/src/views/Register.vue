<template>
  <section class="hero is-fullheight gradient" id="reg">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="box">
              <div class="card-content">
                <div class="container has-text-centered">
                  <p class="title">We're excited to have you 🎉</p>
                  <p>What can we call you?</p>
                  <br>
                  <b-input type="text" name="name" placeholder="Jane Doe"></b-input>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
export default {
  name: 'register',
};
</script>

<style lang="scss">

.box {
    border-radius: 8px;
}

#boxtitle {
    border-width: 0px 2px 0px 0px;
}

</style>
