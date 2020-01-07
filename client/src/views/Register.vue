<template>
  <section class="hero is-fullheight gradient">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="box">
              <div class="card-content">
                <div class="container">
                  <loading :active.sync="isLoading"
                          :can-cancel="false"
                          :is-full-page="false"
                          loader="dots"
                          color="#8C00B6"></loading>
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
                  <br>
                  <ValidationObserver ref="observer" v-slot="{ passes }">
                    <form>
                      <ValidationProvider name="Name" rules="required|min:3"
                        v-slot="{ errors, valid }" v-if="getName">
                        <b-field :type="{ 'is-danger': errors[0], 'is-success': valid }"
                          :message="errors">
                          <b-input type="text"
                                   v-model.lazy="form.name"
                                   placeholder="Jane Doe">
                          </b-input>
                        </b-field>
                      </ValidationProvider>
                      <ValidationProvider name="Email" rules="required|email"
                                          v-slot="{ errors, valid }">
                        <b-field label="Email" v-if="getAccount"
                                 :type="{ 'is-danger': errors[0], 'is-success': valid }"
                                 :message="errors">
                          <b-input type="email" v-model.lazy="form.email"
                            placeholder="janedoe@gmail.com"></b-input>
                        </b-field>
                      </ValidationProvider>
                      <ValidationProvider name="Password" rules="required|min:8"
                                          v-slot="{ errors, valid }">
                        <b-field label="Password" v-if="getAccount"
                                 :type="{ 'is-danger': errors[0], 'is-success': valid }"
                                 :message="errors">
                          <b-input type="password"
                                   v-model.lazy="form.password"
                                   placeholder="********">
                          </b-input>
                        </b-field>
                      </ValidationProvider>
                      <ValidationProvider name="Confirm" rules="required|confirmed:Password"
                                          v-slot="{ errors, valid }">
                        <b-field label="Confirm Password" v-if="getAccount"
                                 :type="{ 'is-danger': errors[0], 'is-success': valid }"
                                 :message="errors">
                          <b-input type="password"
                                   v-model.lazy="form.confirm"
                                   placeholder="********">
                          </b-input>
                        </b-field>
                      </ValidationProvider>
                    </form>
                  </ValidationObserver>
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
  Prop,
  Component,
} from 'vue-property-decorator';

import { ValidationProvider, ValidationObserver } from 'vee-validate';
import '@/plugins/vee-validate';

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

import IconButton from '@/components/IconButton.vue';
import { registerUser } from '@/services/apiService';

interface registerForm {
  name?: String,
  email?: String,
  password?: String,
  confirm?: String,
}

@Component({
  components: {
    IconButton,
    ValidationProvider,
    ValidationObserver,
    Loading,
  },
})
export default class Register extends Vue {
  @Prop({ default: true }) public getName!: boolean;

  @Prop({ default: false }) public getAccount!: boolean;

  @Prop({ default: false }) public showMessage!: boolean;

  @Prop({ default: false }) public isLoading!: boolean;

  @Prop({ default: '' }) public message!: string;

  @Prop({ default: {} }) public form!: registerForm;

  /**
   * @brief Guides the user thru the registration process
   */
  async handleClick(): Promise<any> {
    if (this.getName) {
      this.getName = false;
      this.getAccount = true;
    } else {
      this.isLoading = true;
      const user = await registerUser(this.form)
        .catch((err) => {
          this.message = err.message;
          this.$buefy.snackbar.open({
            message: this.message,
            type: 'is-danger',
            position: 'is-top',
            actionText: 'Dismiss',
          });
        });
      this.$router.push('/');
    }
  }
}
</script>
<style lang="scss">
  .container {
    margin: 1em;
    padding-bottom: 2em;
  }
</style>
