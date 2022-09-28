<script setup>
/* eslint-disable */

// props
const props = defineProps({
    label: {type: String, default: "Label"},
    modelValue: {type: Boolean, default: false}
})

// emits
const emit = defineEmits(['update:modelValue'])
</script>

<template>
    <main class="flex items-center gap-2">

        <input
            type="checkbox"
            :name="props.label"
            :id="props.label"
            :checked="modelValue"
            @change="$emit('update:modelValue', $event.target.checked)"
            class="cursor-pointer focus:outline-none"
            />

        <label :for="props.label" class="text-xs text-gray-600 font-normal cursor-pointer md:text-sm">{{props.label}}</label>

    </main>
</template>