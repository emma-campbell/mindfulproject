<template>
  <section class="hero is-fullheight gradient">
    <div class="hero-body">
      <loading :active.sync="isWaiting"
        :can-cancel="false"
        :is-full-page="true"
        loader="dots"
        color="#ffff"
      >
      </loading>
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

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

@Component({
  components: {
    Loading,
  },
})
export default class Confirm extends Vue {
  @Prop({ default: true }) public isWaiting!: boolean;

  @Prop({ default: false }) public isConfirmed!: boolean;
}
</script>
