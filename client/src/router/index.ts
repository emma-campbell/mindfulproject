import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home.vue';
import Register from '@/views/register/Register.vue';
import Journals from '@/views/journals/Journals.vue';

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
      path: '/journal',
      name: 'journal',
      component: Journals,
    },
  ],
});
