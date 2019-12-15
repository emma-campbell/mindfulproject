<template>
  <b-icon
    icon="arrow-right-bold-circle-outline"
    size="is-large"
    type="button is-grey"
    @click.native="onClick()"></b-icon>
</template>

<script lang="ts">
import {
  Vue,
  Component,
  Emit,
} from 'vue-property-decorator';

@Component({})
export default class IconButton extends Vue {
  @Emit()
  public onClick(): void {
    // eslint-disable-next-line
    this.$emit('click')
    console.log('click');
  }
}
</script>

<style lang="scss">
.mdi-arrow-right-bold-circle-outline {
  text-shadow: 2px 2px 4px #808B96;
}

.mdi-arrow-right-bold-circle-outline:hover {
  color: #8C00B6;
  transition: color .25s, background .25s;
}

.mdi-arrow-right-bold-circle-outline:active {
  color: #6C3483;
  transform: translateY(4px);
}
</style>
