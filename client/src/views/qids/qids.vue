<template src="./template.html"></template>
<script lang="ts">
import 'reflect-metadata';

import {
  Vue,
  Component,
  Prop,
} from 'vue-property-decorator';

import IconButton from '@/components/IconButton.vue';

@Component({
  components: { IconButton },
})

export default class Qids extends Vue {
  @Prop() getQ1!: boolean;

  @Prop() getQ2!: boolean;

  @Prop() getQ3!: boolean;

  @Prop() getQ4!: boolean;

  @Prop() getQ5!: boolean;

  @Prop() getQ6Q7!: boolean;

  @Prop() getQ8Q9!: boolean;

  @Prop() getQ9!: boolean;

  @Prop() getQ10!: boolean;

  @Prop() getQ11!: boolean;

  @Prop() getQ12!: boolean;

  @Prop() getQ13!: boolean;

  @Prop() getQ14!: boolean;

  @Prop() getQ15!: boolean;

  @Prop() getQ16!: boolean;

  @Prop() getComplete! : boolean;

  constructor() {
    super();
    this.getQ1 = true;
  }

  public next(): void {
    if (this.getQ1) {
      this.getQ1 = false;
      this.getQ2 = true;
    } else if (this.getQ2) {
      this.getQ2 = false;
      this.getQ3 = true;
    } else if (this.getQ3) {
      this.getQ3 = false;
      this.getQ4 = true;
    } else if (this.getQ4) {
      this.getQ4 = false;
      this.getQ5 = true;
    } else if (this.getQ5) {
      this.getQ5 = false;
      this.getQ6Q7 = true;
    } else if (this.getQ6Q7) {
      this.getQ6Q7 = false;
      this.getQ8Q9 = true;
    } else if (this.getQ8Q9) {
      this.getQ8Q9 = false;
      this.getQ10 = true;
    } else if (this.getQ10) {
      this.getQ10 = false;
      this.getQ11 = true;
    } else if (this.getQ11) {
      this.getQ11 = false;
      this.getQ12 = true;
    } else if (this.getQ12) {
      this.getQ12 = false;
      this.getQ13 = true;
    } else if (this.getQ13) {
      this.getQ13 = false;
      this.getQ14 = true;
    } else if (this.getQ14) {
      this.getQ14 = false;
      this.getQ15 = true;
    } else if (this.getQ15) {
      this.getQ15 = false;
      this.getQ16 = true;
    } else if (this.getQ16) {
      this.getQ16 = false;
      this.getComplete = true;
    }
  }
}
</script>
<style src="../register/styles.scss" lang="scss"></style>
