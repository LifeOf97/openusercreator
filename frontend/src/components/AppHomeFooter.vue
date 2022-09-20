<script setup>
/* eslint-disable */

import { computed } from 'vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconGithub from './icons/IconGithub.vue';
import IconLinkedin from './icons/IconLinkedin.vue';

const year = computed(() => {
    return new Date().getFullYear();
})
</script>

<template>
    <main class="w-11/12 mx-auto flex flex-col gap-5 items-center justify-between text-xs text-gray-400 py-10 md:text-sm md:flex-row">

        <div class="flex flex-col gap-2 md:gap-4">
            <div class="flex items-center gap-2">
                <p>&copy; {{year}}</p>
                <div class="flex items-center">
                    <IconUserCircleSolid class="w-5 h-5 fill-red-500" />
                    <p class="font-semibold text-gray-900">pen User Data</p>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <p class="text-gray-900 font-semibold">API Docs:</p>
                <a href="#" target="_blank" rel="noopener noreferrer" class="text-blue-500 font-light hover:text-blue-600">Swagger,</a>
                <a href="#" target="_blank" rel="noopener noreferrer" class="text-blue-500 font-light hover:text-blue-600">REDOC</a>
            </div>
        </div>

        <div class="flex flex-col gap-2 md:gap-4">
            <div class="flex items-center gap-2">
                <p>Developed by the</p>
                <a href="https://twitter.com/realestkma" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:text-blue-600">RealestKMA</a>
                <p>from the 234</p>
            </div>
            <div class="flex items-center justify-center gap-4 md:justify-start">
                <a href="http://twitter.com/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconTwitter class="w-5 h-5 fill-gray-900" />
                </a>
                <a href="http://github.com/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconGithub class="w-5 h-5 fill-gray-900" />
                </a>
                <a href="http://linkedin.com/in/realestkma" target="_blank" rel="noopener noreferrer">
                    <IconLinkedin class="w-5 h-5 fill-gray-900" />
                </a>
            </div>
        </div>

    </main>
</template>