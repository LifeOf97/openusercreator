<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import bgSvg from '../assets/svgs/bg.svg'
import IconStory404 from './icons/IconStory404.vue';

// refs

// data
const data = {
  inlineStyles: {
    backgroundImage: `url(${bgSvg})`,
  }
}
</script>

<template>
    <main class="w-full h-screen min-h-[20rem] bg-cover bg-center md:min-h-[40rem]" :style="data.inlineStyles">
        
        <div class="relative w-full h-full bg-white/80 backdrop-blur-lg">

            <IconStory404 class="w-full h-full"/>
            
            <div class="absolute w-full bottom-20 flex items-center justify-center md:bottom-10">
                <RouterLink :to="{name: 'home'}" class="text-sm text-white bg-blue-500 px-4 py-2 rounded transition-all duration-300 hover:-translate-y-1 hover:bg-blue-600 md:text-base">Go back home</RouterLink>
            </div>

        </div>

    </main>
</template>