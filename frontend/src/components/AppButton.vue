<script setup>
/* eslint-disable */

// props
const props = defineProps({
    type: { type: String, default: "button" },
    label: { type: String, default: "Button" },
    loading: {type: Boolean, default: false},
    loadingText: {type: String, default: "Loading..."}
})
</script>

<template>
    <button
        :type="props.type"
        :disabled="props.loading"
        class="p-3 text-xs text-center font-medium transition-all duration-300 rounded cursor-pointer disabled:cursor-not-allowed md:text-base">
            <p v-if="props.loading">{{props.loadingText}}</p>
            <p v-else>{{props.label}}</p>
    </button>
</template>