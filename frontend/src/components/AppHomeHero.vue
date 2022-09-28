<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import bgSvg from '../assets/svgs/bg.svg'
import AppTopNav from './AppTopNav.vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';

// refs

// data
const data = {
  inlineStyles: {
    backgroundImage: `url(${bgSvg})`,
  }
}
</script>

<template>
    <main class="h-full w-full bg-fixed bg-center bg-no-repeat bg-cover" :style="data.inlineStyles">

        <div class="h-full w-full bg-white/90">

            <AppTopNav class="absolute top-0 right-0" />

            <div class="h-full w-11/12 mx-auto py-40 flex items-center justify-center lg:py-60">

                <div class="flex flex-col gap-2">

                    <div class="flex items-center justify-center">
                        <IconUserCircleSolid class="w-24 h-24 fill-red-500 md:w-40 md:h-40" />
                        <p class="self-center text-3xl font-black text-gray-800 sm:text-3xl md:text-6xl">pen User Data</p>
                    </div>

                    <div class="w-11/12 mx-auto text-center text-xl text-gray-700 font-normal md:text-2xl md:w-8/12 lg:w-9/12 lg:text-4xl">
                        <p class="leading-7 md:leading-9 lg:leading-[3rem]">Fully Functional Free Fake User Data API for Testing and Prototying with Authentication</p>
                    </div>

                    <div class="flex flex-col items-center justify-center gap-4 mt-10 sm:flex-row">
                        <RouterLink :to="{name: 'signup'}" class="px-6 py-4 bg-gray-900 rounded-md text-sm text-white transition-all duration-300 hover:-translate-y-1 md:text-base">Become a Creator</RouterLink>
                        <RouterLink to="#" class="px-6 py-4 bg-transparent rounded-md text-sm text-gray-900 transition-all duration-200 hover:border hover:bg-gray-50 hover:-translate-y-1 md:text-base">Hit an Endpoint</RouterLink>
                    </div>

                </div>

            </div>

        </div>

    </main>
</template>