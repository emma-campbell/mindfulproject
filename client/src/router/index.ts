import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home.vue';
import Register from '@/views/Register.vue';
import Confirm from '@/views/Confirm.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/confirm',
      name: 'confirm',
      component: Confirm,
    },
  ],
});
