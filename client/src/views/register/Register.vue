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
                     v-bind="this.name" >
                    Welcome, {{ this.name.split(" ")[0] }} 👋
                  </p>
                  <p class="instructions"
                     v-if="getAccount">
                    Please enter your email and password.
                  </p>

                  <br v-if="getName">
                  <form>
                    <b-field>
                      <b-input type="text"
                               v-model.lazy="name"
                               v-if="getName"
                               v-bind="{ 'is-danger' : errors }"
                               placeholder="Jane Doe">
                      </b-input>
                    </b-field>

                    <b-field label="Email" v-if="getAccount">
                      <b-input type="email"
                               v-model.lazy="email"
                               placeholder="janedoe@gmail.com"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>
                    <b-field label="Password" v-if="getAccount">
                      <b-input type="password"
                               v-model.lazy="password"
                               placeholder="********"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>

                    <b-field label="Confirm Password" v-if="getAccount" v-slot="{ errors }">
                      <b-input type="password"
                               v-model.lazy="confirmed"
                               placeholder="********"
                               v-bind="{ 'is-danger' : errors }">
                      </b-input>
                    </b-field>
                  </form>

                  <div class="container is-pulled-right" id="submit-container">
                    <IconButton v-on:click="next"/>
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
import axios from 'axios';
import { validate, extend, ValidationProvider } from 'vee-validate';

import {
  Vue, Inject,
  Component,
  Prop, Watch,
} from 'vue-property-decorator';

import IconButton from '@/components/IconButton.vue';

@Component({
  components: { IconButton, ValidationProvider },
})
export default class Register extends Vue {
  path: string = 'http://localhost:5000/api/users/';

  private errors: string[] = [];

  @Prop({ default: '' }) public name!: string;

  @Prop({ default: '' }) public email!: string;

  @Prop({ default: '' }) public password!: string;

  @Prop({ default: '' }) public confirmation!: string;

  @Prop({ default: false }) public validated!: boolean;

  @Prop({ default: true }) public getName!: boolean;

  @Prop({ default: false }) public getAccount!: boolean;

  @Prop({ default: false }) public showMessage!: boolean;

  @Prop({ default: '' }) public message!: string;

  private payload: {
    password: string;
    name: string;
    email: string
  } = { password: '', name: '', email: '' };

  @Watch('name')
  async onNameChange(val: string): Promise<any> {
    if (val) {
      await this.validateName(val);
    }
  }

  async validateName(val: string): Promise<any> {
    const { errors } = await validate(val, 'min:3');
    this.errors = errors;
  }

  @Watch('email')
  async onEmailChange(val: string): Promise<any> {
    if (val) {
      await this.validateEmail(val);
    }
  }

  async validateEmail(val: string): Promise<any> {
    const { errors } = await validate(val, 'email');
    this.errors = errors;
  }

  @Watch('password')
  async onPasswordChange(val: string): Promise<any> {
    if (val) {
      await this.validatePassword(val);
    }
  }

  async validatePassword(val:string): Promise<any> {
    const { errors } = await validate(val, 'password:@confirmation');
    this.errors = errors;
  }

  /**
   * @brief Guides the user thru the registration process
   */
  async next(): Promise<any> {
    if (this.getName) {
      this.getName = false;
      this.getAccount = true;
    } else {
      this.payload = {
        name: this.name,
        email: this.email,
        password: this.password,
      };

      if (this.errors.length === 0) {
        const user = this.addUser();
      }
    }
  }

  async addUser(): Promise<any> {
    axios.post(this.path, this.payload)
      .then(res => res.data)
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
  }
}
</script>
<style src="./styles.scss" lang="scss"></style>
