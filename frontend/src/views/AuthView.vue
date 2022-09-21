<script setup>
/* eslint-disable */
import { RouterView } from 'vue-router';
import bgSvg from '../assets/svgs/bg.svg'
import IconUserCircleSolid from '../components/icons/IconUserCircleSolid.vue';

// data
const data = {
  inlineStyles: {
    backgroundImage: `url(${bgSvg})`,
  }
}
</script>

<template>
    <main class="w-full h-screen min-h-[20rem] bg-no-repeat bg-cover bg-center md:min-h-[40rem]" :style="data.inlineStyles">

        <div class="w-full h-full flex">

            <!-- visible on large screens -->
            <div class="hidden h-full w-2/5 items-center justify-center bg-white/50 backdrop-blur lg:flex">
                <div class="flex items-center">
                    <IconUserCircleSolid class="w-24 h-24 fill-red-500 xl:w-32 xl:h-32" />
                    <p class="-ml-2 text-3xl text-gray-900 font-bold xl:text-4xl">pen User Data</p>
                </div>
            </div>
            <!-- visible on large screens -->

            <div class="w-full bg-white lg:w-3/4">
                <RouterView />
            </div>
        </div>
    </main>
</template>