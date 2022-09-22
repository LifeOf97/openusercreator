<script setup>
/* eslint-disable */
import { RouterView } from 'vue-router';
import AppTopNav from '../components/AppTopNav.vue';
</script>

<template>
    <main class="relative w-full h-full min-h-[20rem] bg-cover bg-center md:min-h-[40rem]">
        
        <div class="w-full absolute top-0 z-10">
            <AppTopNav />
        </div>

        <div class="w-full h-full">
            <RouterView />
        </div>

    </main>
</template>