<script setup>
/* eslint-disable */
import IconCloseBig from './icons/IconCloseBig.vue';
import IconCheckCircleSolid from './icons/IconCheckCircleSolid.vue';

// emits
const emit = defineEmits(["closeBtnClicked"])
</script>

<template>
    <main class="bg-transparent">

        <div class="bg-white flex items-center gap-5 px-4 py-2 shadow-lg shadow-graye-300 rounded-lg">

            <!-- icon -->
            <div class="flex items-center justify-center rounded-full">
                <slot name="icon">
                    <IconCheckCircleSolid class="w-7 h-7 fill-green-500" />
                </slot>
            </div>
            <!-- icon -->

            <div class="flex flex-col gap-3">

                <!-- title & close button -->
                <span class="flex items-center gap-5">
                    <!-- title -->
                    <p class="text-sm text-slate-900 font-medium md:text-base">
                        <slot name="title">Notification title</slot>
                    </p>
                    <!-- title -->
        
                    <!-- close button -->
                    <button type="button" @click.prevent="$emit('closeBtnClicked')">
                        <IconCloseBig class="w-5 h-5 fill-slate-400" />
                    </button>
                    <!-- close button -->

                </span>
                <!-- title & close button -->

                <slot name="description"></slot>

            </div>


        </div>
    </main>
</template>