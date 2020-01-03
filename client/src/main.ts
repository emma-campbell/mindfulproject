import Vue from 'vue';

import Buefy from 'buefy';
import 'buefy/dist/buefy.css';

import App from './App.vue';
import router from './router';

import 'bulma/bulma.sass';
import '@/assets/scss/styles.scss';

import '@mdi/font/css/materialdesignicons.css';
import 'vue-material-design-icons/styles.css';
import 'es6-promise';

Vue.config.productionTip = false;

Vue.use(Buefy);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
