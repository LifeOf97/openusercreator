<script setup>
/* eslint-disable */

// props
const props = defineProps({
    type: { type: String, default: "text" },
    label: { type: String, default: "Label" },
    cols: { type: Number, default: 30 },
    rows: { type: Number, default: 10 },
    required: { type: Boolean, default: true },
    minLen: { type: Number, default: 0 },
    maxLen: { type: Number, default: 255 },
    iconPos: { type: String, default: "right" },
    disable: { type: Boolean, default: false },
    autocomplete: { type: Boolean, default: false },
    modelValue: { type: String },
})

// emits
const emits = defineEmits(["update:modelValue"])
</script>
    
<template>
    <main
        :class="props.iconPos == 'left' ? 'gap-3':'', props.disable ? 'bg-gray-200':'hover:ring hover:ring-blue-400 focus-within:ring focus-within:ring-blue-400'"
        class="w-full p-2 flex items-center ring-1 ring-gray-200 ring-offset-white rounded overflow-hidden transition-all duration-300
            ">

        <textarea
            :name="props.label"
            :id="props.label"
            :cols="props.cols"
            :rows="props.rows"
            :minlength="props.minLen"
            :maxlength="props.maxLen"
            :required="props.required"
            :placeholder="props.label"
            :autocomplete="autocomplete"
            :disabled="props.disable"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            :class="props.iconPos == 'left' ? 'order-2':'', props.disable ? 'cursor-not-allowed':''"
            class="w-full bg-transparent text-xs text-gray-700 placeholder:text-gray-400 resize-none focus:outline-none md:text-sm"></textarea>

        <slot name="icon">
            <!-- <IconPencilOutline class="w-5 h-5 stroke-gray-400" /> -->
        </slot>

    </main>
</template>