<script setup>
/* eslint-disable */

// props
const props = defineProps({
    strokeWidth: {type: Number, default: 1.5}
})
</script>

<template>
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" :stroke-width="props.strokeWidth" stroke="currentColor"
        >
        <path stroke-linecap="round" stroke-linejoin="round"
            d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9" />
    </svg>
</template>