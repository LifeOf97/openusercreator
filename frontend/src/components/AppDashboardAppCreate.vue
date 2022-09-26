<script setup>
/* eslint-disable */
import { useRouter } from 'vue-router';
import IconCubeOutline from './icons/IconCubeOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import IconCheckCircleSolid from './icons/IconCheckCircleSolid.vue';
import AppDashboardAppForm1 from './AppDashboardAppForm1.vue';
import AppDashboardAppForm2 from './AppDashboardAppForm2.vue';
import AppDashboardAppForm3 from './AppDashboardAppForm3.vue';
import AppDashboardAppCreateConfirm from './AppDashboardAppCreateConfirm.vue';
import AppDashboardAppCreateSuccess from './AppDashboardAppCreateSuccess.vue';

// router
const router = useRouter()
</script>
    
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">
                <h3 class="text-3xl text-gray-600 font-bold md:text-4xl">Create App</h3>
            </div>
            <IconCubeOutline class="hidden absolute -top-7 right-0 w-86 h-96 stroke-gray-50 md:block" :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">
            
            <div class="w-11/12 mx-auto flex flex-col gap-16 md:w-10/12">

                <!-- back link -->
                <span class="w-full flex items-center justify-start">
                    <button type="button" @click.prevent="router.back()" class="group flex items-center gap-2">
                        <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Back</p>
                    </button>
                </span>
                <!-- back link -->

                <div class="flex flex-col gap-10">

                    <span class="flex flex-col items-center gap-5 md:gap-10">
                        <h3 class="text-2xl text-gray-900 font-semibold md:text-4xl">Name Your App</h3>

                        <span class="flex items-center -space-x-1">
                            <IconCheckCircleSolid class="w-9 h-9 fill-gray-200 md:w-12 md:h-12"/>
                            <div class="w-10 border-b border-gray-200 sm:w-20"></div>
                            <IconCheckCircleSolid class="w-9 h-9 fill-gray-200 md:w-12 md:h-12"/>
                            <div class="w-10 border-b border-gray-200 sm:w-20"></div>
                            <IconCheckCircleSolid class="w-9 h-9 fill-gray-200 md:w-12 md:h-12"/>
                            <div class="w-10 border-b border-gray-200 sm:w-20"></div>
                            <IconCheckCircleSolid class="w-9 h-9 fill-gray-200 md:w-12 md:h-12"/> 
                        </span>
                    </span>

                    <AppDashboardAppCreateSuccess />

                </div>

            </div>

        </div>

    </main>
</template>