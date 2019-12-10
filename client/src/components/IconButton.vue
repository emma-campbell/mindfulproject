<template>
  <b-icon
    icon="arrow-right-bold-circle-outline"
    size="is-large"
    type="button is-grey"
    id="next"
    v-on:click="$emit('click', $event)"></b-icon>
</template>

<script lang="ts">
// import { Component, Watch } from 'vue-property-decorator';
// @Component()

export default {
  name: 'icon-button',
};
</script>

<style lang="scss">
.mdi-arrow-right-bold-circle-outline {
  text-shadow: 2px 2px 4px #808B96;
}

.mdi-arrow-right-bold-circle-outline:hover {
  color: #8C00B6;
  transition: color .25s, background .25s;
}

.mdi-arrow-right-bold-circle-outline:active {
  color: #6C3483;
  transform: translateY(4px);
}
</style>
