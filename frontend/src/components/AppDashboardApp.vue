<script setup>
/* eslint-disable */
import { RouterLink, useRouter } from 'vue-router';
import IconPencilOutline from './icons/IconPencilOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconClockOutline from './icons/IconClockOutline.vue';
import IconCubeOutline from './icons/IconCubeOutline.vue';
import IconHashtag from './icons/IconHashtag.vue';
import IconLinkSolid from './icons/IconLinkSolid.vue';
import IconUserGroupOutline from './icons/IconUserGroupOutline.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';

// routers
const router = useRouter()

</script>
    
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">                
                <h3 class="text-3xl text-gray-600 font-bold md:text-4xl">My App Name</h3>
            </div>
            <IconCubeOutline class="hidden absolute -top-7 right-0 w-86 h-96 stroke-gray-50 md:block" :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">

            <div class="w-11/12 mx-auto flex flex-col gap-20 md:w-10/12">

                <!-- back link -->
                <span class="w-full flex items-center justify-start">
                    <button type="button" @click.prevent="router.back()" class="group flex items-center gap-2">
                        <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Dashboard</p>
                    </button>
                </span>
                <!-- back link -->

                <!-- profile overview -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">App Overview</h3>

                    <div class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex items-center justify-between p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your app details.</p>
                            <RouterLink :to="{name: 'dashboardappsettings'}"
                                class="flex items-center gap-2 px-2 py-1 border border-gray-300 rounded transition-all duration-300 group hover:bg-blue-500">
                                <IconPencilOutline
                                    class="w-4 h-4 stroke-gray-600 transition-all duration-300 group-hover:stroke-white" />
                                <p
                                    class="text-xs text-gray-600 font-normal transition-all duration-300 group-hover:text-white md:text-sm">
                                    Edit</p>
                            </RouterLink>
                        </div>

                        <div class="w-full p-4 overflow-auto">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconQRCodeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App ID:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">143ad74c-5726-4d38-940a-1f801108ac92</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconCubeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Name:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">My-app-name</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconHashtag class="w-5 h-5 fill-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Description:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">Application description comes here</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconLinkSolid class="w-5 h-5 fill-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App URL:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">https://openuserdata.com/api/v1/25445099391964575813/my-first-app/users/</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconUserGroupOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App User Profiles:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">50</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Users Password:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">p@ssw0rd</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconClockOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Date Created:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">September 22, 2022 @14:40
                                    </td>
                                </tr>
                                <tr class="">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconClockOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Last Updated:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">September 22, 2022 @14:40
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>
                <!-- profile overview -->

            </div>

        </div>

    </main>
</template>