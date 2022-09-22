<script setup>
/* eslint-disable */

// props
const props = defineProps({
    label: {type: String, default: "Label"},
    modelValue: {type: Boolean}
})
</script>

<template>
    <main class="flex items-center gap-2">

        <input
            type="checkbox"
            :name="props.label"
            :id="props.label"
            :value="modelValue"
            @change="$emit('update:modelValue', $event.target.checked)"
            class="cursor-pointer indeterminate:bg-green-500 focus:outline-none checked:bg-pink-500"
            />

        <label :for="props.label" class="text-xs text-gray-600 font-normal cursor-pointer md:text-sm">{{props.label}}</label>

    </main>
</template>