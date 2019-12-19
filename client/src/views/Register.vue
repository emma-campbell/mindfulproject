<template>
  <section class="hero is-fullheight gradient" id="reg">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="box">
              <div class="card-content">
                <div class="container">

                  <p class="title"
                     v-if="getName">
                    We're excited to have you 🎉
                  </p>
                  <div id="instructions"
                       v-if="getName">
                    <p>What can we call you?</p>
                  </div>

                  <p class="title"
                     v-if="getAccount"
                     v-bind="form.name" >
                    Welcome, {{ form.name.split(' ')[0] }} 👋
                  </p>
                  <p class="instructions"
                     v-if="getAccount">
                    Please enter your email and password.
                  </p>

                  <br v-if="getName">
                  <form>
                    <b-field slot="{{ errors[0]}}">
                      <b-input type="text"
                               v-model.lazy="form.name"
                               v-if="getName"
                               v-bind="{ 'is-danger' : errors }"
                               placeholder="Jane Doe">
                      </b-input>
                    </b-field>

                    <b-field label="Email" v-if="getAccount">
                      <b-input type="email"
                               v-model.lazy="form.email"
                               placeholder="janedoe@gmail.com"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>
                    <b-field label="Password" v-if="getAccount">
                      <b-input type="password"
                               v-model.lazy="form.password"
                               placeholder="********"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>

                    <b-field label="Confirm Password" v-if="getAccount" v-slot="{ errors }">
                      <b-input type="password"
                               v-model.lazy="form.confirm"
                               placeholder="********"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>
                  </form>

                  <div class="container is-pulled-right" id="submit-container">
                    <IconButton v-on:click="handleClick"/>
                  </div>
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
import 'reflect-metadata';

import {
  Vue,
  Component,
  Prop,
  Watch,
} from 'vue-property-decorator';

import IconButton from '../components/IconButton.vue';

import ApiService from '@/services/apiService';
import Validator from '@/utils/validate';

interface registerForm {
  name?: String,
  email?: String,
  password?: String,
  confirm?: String,
}

@Component({
  components: { IconButton },
})
export default class Register extends Vue {
  path: string = 'http://localhost:5000/api/users/';

  private errors: Error[] = [];

  @Prop({ default: false }) public validated!: boolean;

  @Prop({ default: true }) public getName!: boolean;

  @Prop({ default: false }) public getAccount!: boolean;

  @Prop({ default: false }) public showMessage!: boolean;

  @Prop({ default: '' }) public message!: string;

  @Prop({ default: {} }) public form!: registerForm;

  @Watch('form.name')
  private validateName = (value: string) => {
    console.log('Validating name');
    if (!Validator.isValidName(value)) {
      this.errors.push(new Error('Please be sure to enter your first and last name.'));
    }
  };

  //
  // @Watch('form.email')
  // private validateEmail = (rule: any, value: string, callback: Function) => {
  // eslint-disable-next-line
  //   const regexp = new RegExp(/\^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
  //
  //   if (!regexp.test(value)) {
  //     callback(new Error('Please enter a valid email.'));
  //   } else {
  //     callback();
  //   }
  // };
  //
  // @Watch('form.password')
  // private validatePassword = (rule: any, value: string, callback: Function) => {
  //   if (value.length > 8) {
  //     callback(new Error('Your password cannot be less than 8 characters.'));
  //   } else {
  //     callback();
  //   }
  // };
  //
  // @Watch('form.confirm')
  // private validateConfirmation = (rule: any, value: string, callback: Function) => {
  //   if (value !== this.form.password) {
  //
  //   } else {
  //     callback();
  //   }
  // };

  // private registerRules = {
  //   name: [{ validator: this.validateName, trigger: 'blur' }],
  //   email: [{ validator: this.validateEmail, trigger: 'blur' }],
  //   password: [{ validator: this.validatePassword, trigger: 'blur' }],
  // };

  /**
   * @brief Guides the user thru the registration process
   */
  private handleClick(): void {
    if (this.getName) {
      this.getName = false;
      this.getAccount = true;
    } else {
      console.log(this.form);
    }
  }
}
</script>
