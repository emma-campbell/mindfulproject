<template src="./template.html"></template>
<script lang="ts">
import 'reflect-metadata';
import axios from 'axios';

import {
  Vue,
  Component,
  Prop,
  Emit,
} from 'vue-property-decorator';

import IconButton from '@/components/IconButton.vue';

@Component({
  components: { IconButton },
})

export default class Login extends Vue {
  path: string = 'http://localhost:5000/api/users/';

  email: string = '';

  password: string = '';

  @Prop() getLogin!: boolean;

  constructor() {
    super();
    this.getLogin = true;
  }
}
</script>
<style src="../register/styles.scss" lang="scss"></style>
