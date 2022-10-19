<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconPencilOutline from './icons/IconPencilOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconCubeOutline from './icons/IconCubeOutline.vue';
import IconHashtag from './icons/IconHashtag.vue';
import IconLinkSolid from './icons/IconLinkSolid.vue';
import IconUserGroupOutline from './icons/IconUserGroupOutline.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import { onMounted } from 'vue';
import { useAppStore } from '../stores/apps';
import { useTitle } from '@vueuse/core';
import IconCalenderOutline from './icons/IconCalenderOutline.vue';
import { DateTime } from 'luxon';
import IconClockOutline from './icons/IconClockOutline.vue';
import { useAuthStore } from '../stores/auth';
import { useSlugify } from '../composables/slugify';

// stores
const appStore = useAppStore()
const authStore = useAuthStore()

// methods
const formatDate = (value) => {
    return value ? DateTime.fromISO(value).toFormat('LLLL dd, yyyy @ HH:mm'):
    DateTime.fromISO(authStore.userProfile['date_joined']).toFormat('LLLL dd, yyyy @ HH:mm');
}

// hooks
onMounted(() => {
    // set title
    useTitle(`Apps | ${useSlugify(appStore.appInView['name']).data.value}`)

    // get app users count
    appStore.getAppUserCount(appStore.appInView['endpoint'])
})
</script>
    
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">                
                <h3 class="text-3xl text-gray-600 font-bold capitalize md:text-4xl">{{useSlugify(appStore.appInView['name']).data.value}}</h3>
            </div>
            <IconCubeOutline class="hidden absolute -top-7 right-0 w-86 h-96 stroke-gray-50 md:block" :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">

            <div class="w-11/12 mx-auto flex flex-col gap-20 md:w-10/12">

                <!-- back link -->
                <span class="w-full flex items-center justify-start">
                    <RouterLink :to="{name: 'dashboarduser', params: {username: authStore.userProfile['username']}}" class="group flex items-center gap-2">
                        <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Dashboard</p>
                    </RouterLink>
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
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{appStore.appInView['id']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconCubeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Name:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{appStore.appInView['name']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconHashtag class="w-5 h-5 fill-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Description:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{appStore.appInView['description']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconLinkSolid class="w-5 h-5 fill-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App URL:</p>
                                    </td>
                                    <td class="text-xs font-medium md:text-sm">
                                        <a :href="appStore.appInView['endpoint']" target="_blank" class="text-blue-500 hover:text-blue-600">{{appStore.appInView['endpoint']}}</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconUserGroupOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App User Profiles:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{ appStore.appUserCount.data || appStore.appInView['profiles']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Users Password:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{appStore.appInView['profile_password']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconCalenderOutline :strokeWidth="1" class="w-3 h-3 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Date Created:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{formatDate(appStore.appInView['date_created'])}}</td>
                                </tr>
                                <tr class="">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconClockOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Last Updated:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{formatDate(appStore.appInView['last_updated'])}}</td>
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