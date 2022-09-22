<script setup>
/* eslint-disable */
import { ref } from 'vue';
import IconEyeOutline from './icons/IconEyeOutline.vue';
import IconEyeSlashOutline from './icons/IconEyeSlashOutline.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';

// props
const props = defineProps({
    label: { type: String, default: "Label" },
    required: {type: Boolean, default: true},
    minLen: {type: Number, default: 8},
    maxLen: {type: Number, default: 128},
    iconPos: {type: String, default: "right"},
    disable: {type: Boolean, default: false},
    modelValue: { type: String },
})

// emits
const emits = defineEmits(["update:modelValue"])

// refs
const inputType = ref("password")
</script>
    
<template>
    <main
        :class="props.disable ? 'bg-gray-200':'bg-gray-50 hover:ring hover:ring-blue-400 focus-within:ring focus-within:ring-blue-400'"
        class="w-full p-2 flex items-center gap-3 ring-1 ring-gray-200 ring-offset-white rounded overflow-hidden transition-all duration-300">

        <slot name="icon">
        </slot>

        <input
            :type="inputType"
            :name="props.label"
            :id="props.label"
            :required="props.required"
            :minlength="props.minLen"
            :maxlength="props.maxLen"
            :placeholder="props.label"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            :class="props.disable ? 'cursor-not-allowed':''"
            class="w-full bg-transparent text-xs text-gray-700 placeholder:text-gray-400 focus:outline-none md:text-sm" />


        <button v-if="inputType == 'text'" type="button" @click.prevent="inputType = 'password'">
            <IconEyeOutline class="w-5 h-5 stroke-gray-400" />
        </button>
        
        <button v-else type="button" @click.prevent="inputType = 'text'">
            <IconEyeSlashOutline class="w-5 h-5 stroke-gray-400" />
        </button>

    </main>
</template>