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

  private data = {
    name: '',
    email: '',
    password: '',
    password2: '',
  };

  private errors: string[] = [];

  @Prop() public name!: string;

  @Prop() public email!: string;

  @Prop() public password!: string;

  @Prop() public password2!: string;

  @Prop() public validated!: boolean;

  @Prop() public getName!: boolean;

  @Prop() public getAccount!: boolean;

  @Prop() public showMessage!: boolean;

  @Prop() message!: string;

  constructor() {
    super();
    this.message = '';
    this.getName = true;
    this.getAccount = false;
    this.showMessage = false;
  }

  private validateName(): boolean {
    const { name } = this;
    if (name.length > 0) {
      if (name.split(' ').length !== 2) {
        this.message = 'Please enter your first and last name.';
        this.showMessage = true;
      } else {
        return true;
      }
    }
    return false;
  }

  private validateEmail(): boolean {
    const { email } = this;
    if (email.length > 0) {
      if (email.split('@').length !== 2) {
        this.message = 'Please enter a valid email address.';
        this.showMessage = true;
      } else {
        return true;
      }
    }
    return false;
  }

  private validatePassword(): boolean {
    const { password } = this;
    const { password2 } = this;

    if (password.length > 0 && password2.length > 0 && password === password2) {
      return true;
    }

    this.message = 'Please enter a valid password.';
    this.showMessage = true;
    return false;
  }

  public next(): void {
    let user;

    if (this.getName) {
      if (this.validateName()) {
        this.data.name = this.name;
        this.getName = false;
        this.getAccount = true;
      } else {
        this.errors.push(this.message);
      }
    } else {
      // validate email
      if (this.validateEmail()) {
        this.data.email = this.email;
      }

      if (this.validatePassword()) {
        this.data.password = this.password;
      } else {
        this.errors.push(this.message);
      }

      if (this.errors.length !== 0) {
        user = this.addUser(this.data);
      }

      console.log(user);
    }
  }

  @Emit()
  private addUser(payload : object) {
    axios.post(this.path, payload)
      .then(res => res.data)
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
  }
}
</script>
<style src="./styles.scss" lang="scss"></style>
