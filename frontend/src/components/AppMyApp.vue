<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconCubeSolid from './icons/IconCubeSolid.vue';
import IconCogSolid from './icons/IconCogSolid.vue';

// props
const props = defineProps({
    title: {type: String, default: "Title"},
    description: {type: String, default: "Description"}
})
</script>

<template>
    <main class="w-full bg-transparent">
        <div
            class="relative flex flex-col gap-5 bg-white p-10 rounded-lg shadow-lg shadow-gray-200 overflow-hidden group transition-all duration-300 hover:bg-blue-500 md:p-7">
            <span class="flex items-center justify-between">
                <span class="flex items-center gap-3">
                    <IconCubeSolid
                        class="w-5 h-5 fill-gray-600 transition-all duration-300 group-hover:fill-white md:w-7 md:h-7" />
                    <p class="text-sm text-gray-600 font-medium transition-all duration-300 group-hover:text-white md:text-base">{{props.title}}</p>
                </span>
                <RouterLink :to="{name: 'dashboardapp'}" class="relative">
                    <IconCogSolid
                        class="hidden w-7 h-7 fill-white transition-all duration-300 group-hover:block md:w-7 md:h-7" />
                    <IconCogSolid
                        class="absolute top-0 hidden w-7 h-7 fill-white transition-all duration-300 group-hover:animate-ping group-hover:block md:w-7 md:h-7" />
                </RouterLink>
            </span>
            <p class="text-xs text-gray-600 font-light transition-all duration-300 group-hover:text-gray-50 md:text-sm">
                {{props.description}}
            </p>
        </div>
    </main>
</template>