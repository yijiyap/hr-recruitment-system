<!-- Header.vue -->
<template>
    <h2 class="tw-text-2xl tw-font-bold tw-text-center tw-mt-5">
      {{ headerText }}
    </h2>
</template>

<script setup>
const props = defineProps({
  headerText: String,
  required: true
});

</script>