<script setup>
/* eslint-disable */
import { RouterView } from 'vue-router';
import bgSvg from '../assets/svgs/bg.svg'
import IconUserCircleSolid from '../components/icons/IconUserCircleSolid.vue';
import IconArrowLongLeft from '../components/icons/IconArrowLongLeft.vue';

// data
const data = {
  inlineStyles: {
    backgroundImage: `url(${bgSvg})`,
  }
}
</script>

<template>
    <main class="w-full h-screen min-h-[20rem] bg-cover bg-center md:min-h-[40rem]" :style="data.inlineStyles">

        <div class="w-full h-full flex">

            <!-- visible on large screens -->
            <div class="hidden h-full w-2/5 items-center justify-center bg-white/50 backdrop-blur lg:flex">
                <span class="flex items-center">
                    <IconUserCircleSolid class="w-24 h-24 fill-red-500 xl:w-32 xl:h-32" />
                    <p class="-ml-2 text-3xl text-gray-900 font-bold xl:text-4xl">pen User Data</p>
                </span>
            </div>
            <!-- visible on large screens -->

            <div class="w-full flex flex-col bg-white lg:w-3/4">

                <div class="w-10/12 h-full mx-auto flex flex-col sm:w-9/12 md:w-8/12 lg:w-6/12">
                    
                    <!-- back link and logo -->
                    <div class="w-full flex items-center justify-between pt-10 lg:justify-end">
                        <IconUserCircleSolid class="w-10 h-10 fill-red-500 lg:hidden" />
                        <RouterLink :to="{name: 'home'}" class="group flex items-center gap-2">
                            <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                            <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Home</p>
                        </RouterLink>
                    </div>
                    <!-- back link and logo -->
    
                    <div class="w-full">
                        <RouterView />
                    </div>
                    
                </div>

            </div>
        </div>
    </main>
</template>