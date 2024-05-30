
<template>
    <div class="text-xl">
        Display role info
    </div>
</template>

<script setup>
import { onMounted, ref, useAttrs } from 'vue';
const route = useRoute();

onMounted(() => {
    console.log(route.query.roleId);
});


</script>