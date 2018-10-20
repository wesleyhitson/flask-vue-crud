<template>
  <div>
    <b-alert show dismissible variant="success">{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
