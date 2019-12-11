<template src="./template.html"></template>
<script lang="ts">
import 'reflect-metadata';

export default {
  data() {
    const data = [
      {
        habit: 'make bed',
      },
      {
        habit: 'drink water',
      },
      {
        habit: 'positive self talk',
      },
      {
        habit: 'exercise',
      },
      {
        habit: 'meditate',
      },
    ];

    return {
      data,
      isEmpty: false,
      isBordered: true,
    };
  },
};
</script>
<style src="../register/styles.scss" lang="scss"></style>
