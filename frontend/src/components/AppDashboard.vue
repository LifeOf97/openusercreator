<script setup>
/* eslint-disable */
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import {DateTime} from 'luxon';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconPencilOutline from './icons/IconPencilOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import IconClockOutline from './icons/IconClockOutline.vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconCogSolid from './icons/IconCogSolid.vue';
import AppEmptyState from './AppEmptyState.vue';
import IconPlusSolid from './icons/IconPlusSolid.vue';
import AppButton from './AppButton.vue';

// computed
const greet = computed(() => {
  const hour = DateTime.now().toLocaleString(DateTime.TIME_24_SIMPLE).slice(0,2)
  if (hour < 12) return "morning"
  else if ((hour >= 12) && (hour < 18)) return "afternoon"
  else return "evening"
})

</script>

<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">
                <div class="flex flex-col gap-1">
                    <span class="text-xs text-gray-400 font-normal flex items-center gap-2 md:text-base">
                        <code class="text-2xl">&#128075;</code>
                        Good {{greet}}
                    </span>
                    <h3 class="text-3xl text-gray-600 font-bold md:text-4xl">RealestKMA</h3>
                </div>
            </div>
            <IconUserCircleOutline class="hidden absolute -top-7 right-0 w-86 h-96 stroke-gray-50 md:block" :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-20">
            
            <div class="w-11/12 mx-auto flex flex-col gap-20 md:w-10/12">
                
                <!-- profile overview -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">Profile Overview</h3>

                    <div class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex items-center justify-between p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your personal information.</p>
                            <RouterLink :to="{name: 'dashboardsettings'}" class="flex items-center gap-2 px-2 py-1 border border-gray-300 rounded transition-all duration-300 group hover:bg-blue-500">
                                <IconPencilOutline class="w-4 h-4 stroke-gray-600 transition-all duration-300 group-hover:stroke-white" />
                                <p class="text-xs text-gray-600 font-normal transition-all duration-300 group-hover:text-white md:text-sm">Edit</p>
                            </RouterLink>
                        </div>

                        <div class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconQRCodeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">UID:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">1234567890</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Username:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">RealestKMA</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Email address:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">kelvinmayoayeni@gmail.com</td>
                                </tr>
                                <tr class="">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconClockOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Last seen:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">September 22, 2022 @14:40</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
                <!-- profile overview -->


                <!-- my apps -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">My Apps</h3>

                    <div class="grid gap-5 grid-cols-1 sm:grid-cols-2 xl:grid-cols-3">

                        <div class="relative flex flex-col gap-5 bg-white p-6 rounded-lg shadow-lg shadow-gray-200 overflow-hidden group transition-all duration-300 hover:bg-blue-500">
                            <span class="flex items-center justify-between">
                                <span class="flex items-center gap-3">
                                    <IconUserCircleSolid class="w-5 h-5 fill-gray-600 transition-all duration-300 group-hover:fill-white md:w-10 md:h-10" />
                                    <p class="text-sm text-gray-600 font-medium group-hover:text-white md:text-base">My openuser app</p>
                                </span>
                                <RouterLink to="#" class="relative">
                                    <IconCogSolid class="hidden w-7 h-7 fill-white transition-all duration-300 group-hover:block md:w-7 md:h-7" />
                                    <IconCogSolid class="absolute top-0 hidden w-7 h-7 fill-white transition-all duration-300 group-hover:animate-ping group-hover:block md:w-7 md:h-7" />
                                </RouterLink>
                            </span>
                            <p class="text-xs text-gray-600 font-light transition-all duration-300 group-hover:text-gray-50 md:text-sm">
                                Decription of my openuser app and will then follow, for better understanding
                            </p>
                        </div>

                        <AppEmptyState  class="border-gray-200">
                            <template #head>
                                <p class="text-xs text-gray-400 font-medium md:text-sm">No Apps</p>
                            </template>
                            <template #body>
                                <p class="text-xs text-gray-400 font-light md:text-sm">Get started by creating a new app</p>
                            </template>
                            <template #tail>
                                <AppButton label="New app" class="bg-blue-500 text-white hover:bg-blue-600">
                                    <template #icon>
                                        <IconPlusSolid class="w-5 h-5 fill-white" />
                                    </template>
                                </AppButton>
                            </template>
                        </AppEmptyState>

                    </div>
                </div>
                <!-- my apps -->

            </div>

        </div>

    </main>
</template>