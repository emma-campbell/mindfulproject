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
export default class Register extends Vue {
  path: string = 'http://localhost:5000/api/users/';

  name: string = '';

  email: string = '';

  password: string = '';

  password2: string = '';

  validated: boolean = false;

  @Prop() message!: string;

  @Prop() getName!: boolean;

  @Prop() getAccount!: boolean;

  @Prop() showMessage!: boolean;

  constructor() {
    super();
    this.message = '';
    this.getName = true;
    this.getAccount = false;
    this.showMessage = false;
  }

  public next(): void {
    let user;

    if (this.getName) {
      if (this.name.length > 0) {
        this.getName = false;
        this.getAccount = true;
        this.showMessage = false;
      } else {
        this.message = 'Please enter a valid name!';
        this.showMessage = true;
      }
    } else {
      // validate email
      if (this.email.length > 0
          && this.email.split('@').length === 2) {
        this.showMessage = false;

        // validate password
        if (this.password.length > 0
            && this.password2.length > 0
            && this.password === this.password2) {
          this.showMessage = false;
          this.validated = true;
        } else {
          this.message = 'Please make sure your passwords match!';
          this.showMessage = true;
        }

        if (!this.validated) {
          this.$router.push('/register');
        } else {
          user = this.addUser();
        }
      } else {
        this.message = 'Please enter a valid email.';
        this.showMessage = true;
      }
      console.log(user);
    }
  }

  @Emit()
  private addUser() {
    axios.post(this.path, {
      name: this.name,
      email: this.email,
      password: this.password,
      password2: this.password2,
    })
      .then(res => res.data)
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        this.$router.push('/register');
      });
  }
}
</script>
<style src="./styles.scss" lang="scss"></style>
