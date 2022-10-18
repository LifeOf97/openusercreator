<script setup>
/* eslint-disable */

// props
const props = defineProps({
    label: {type: String, default: "Label"},
    required: {type: String, default: true},
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
            :required="props.required"
            :checked="modelValue"
            @change="$emit('update:modelValue', $event.target.checked)"
            class="cursor-pointer focus:outline-none"
            />

        <label :for="props.label" class="text-xs text-gray-600 font-normal cursor-pointer md:text-sm">
            <slot name="label">Label</slot>
        </label>

    </main>
</template>