<script setup>
/* eslint-disable */
import IconPencilOutline from './icons/IconPencilOutline.vue';

// props
const props = defineProps({
    type: {type: String, default: "text"},
    label: {type: String, default: "Label"},
    required: {type: Boolean, default: true},
    minLen: {type: Number, default: 0},
    maxLen: {type: Number, default: 200},
    iconPos: {type: String, default: "right"},
    modelValue: {type: String},
})

// emits
const emits = defineEmits(["update:modelValue"])
</script>

<template>
    <main
        :class="props.iconPos == 'left' ? 'gap-3':''"
        class="w-full p-2 flex items-center bg-gray-50 ring-1 ring-gray-200 ring-offset-white rounded overflow-hidden transition-all duration-300
        hover:ring hover:ring-blue-400 focus-within:ring focus-within:ring-blue-400">

        <input
            :type="props.type"
            :name="props.label"
            :id="props.label"
            :required="props.required"
            :minlength="props.minLen"
            :maxlength="props.maxLen"
            :placeholder="props.label"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            :class="props.iconPos == 'left' ? 'order-2':''"
            class="w-full bg-gray-50 text-xs text-gray-700 placeholder:text-gray-400 focus:outline-none md:text-sm"/>

        <slot name="icon">
            <IconPencilOutline class="w-5 h-5 stroke-gray-400" />
        </slot>

    </main>
</template>