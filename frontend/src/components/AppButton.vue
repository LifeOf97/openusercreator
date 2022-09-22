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
        class="flex items-center gap-3 px-4 py-2 text-xs text-center font-normal transition-all duration-300 rounded cursor-pointer disabled:cursor-not-allowed md:text-sm">
            <slot name="icon"></slot>
            <div class="w-full">
                <p v-if="props.loading">{{props.loadingText}}</p>
                <p v-else>{{props.label}}</p>
            </div>
    </button>
</template>