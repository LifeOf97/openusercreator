<script setup>
/* eslint-disable */
import { computed, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import {DateTime} from 'luxon';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconPencilOutline from './icons/IconPencilOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import IconClockOutline from './icons/IconClockOutline.vue';
import AppEmptyState from './AppEmptyState.vue';
import IconPlusSolid from './icons/IconPlusSolid.vue';
import AppMyApp from './AppMyApp.vue';
import { useAuthStore } from '../stores/auth';
import IconCalenderOutline from './icons/IconCalenderOutline.vue';
import IconCheckCircleSolid from './icons/IconCheckCircleSolid.vue';
import IconInfoCircleSolid from './icons/IconInfoCircleSolid.vue';

// stores
const authStore = useAuthStore()

// computed
const greet = computed(() => {
  const hour = DateTime.now().toLocaleString(DateTime.TIME_24_SIMPLE).slice(0,2)
  if (hour < 12) return "morning"
  else if ((hour >= 12) && (hour < 18)) return "afternoon"
  else return "evening"
})

// methods
const formatDate = (value) => {
    return value ? DateTime.fromISO(value).toFormat('LLLL dd, yyyy @ HH:mm'):
    DateTime.fromISO(authStore.userProfile['date_joined']).toFormat('LLLL dd, yyyy @ HH:mm');
}

// hooks
onMounted(() => {
    document.title = `${authStore.userProfile['username']} | Dashboard | Open User Data`
})
</script>

<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-44 pb-14 overflow-hidden md:pt-48">
            <div class="w-11/12 mx-auto md:w-10/12">
                <div class="flex flex-col gap-1">
                    <span class="text-sm text-gray-400 font-normal flex items-center gap-2 md:text-lg">
                        <code class="text-2xl">&#128075;</code>
                        Good {{greet}}
                    </span>
                    <h3 class="text-3xl text-gray-800 font-bold capitalize md:text-6xl">{{authStore.userProfile['username']}}</h3>
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
                    
                    <!-- loading user profile effect -->
                    <div v-if="authStore.getUser.loading" class="w-full h-96 bg-white rounded overflow-hidden shadow-lg shadow-gray-200 animate-pulse"></div>
                    <!-- loading user profile effect -->

                    <div v-else class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex items-center justify-between p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your personal information.</p>
                            <RouterLink :to="{name: 'dashboardusersettings'}" class="flex items-center gap-2 px-2 py-1 border border-gray-300 rounded transition-all duration-300 group hover:bg-blue-500">
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
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{authStore.userProfile['uid']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Username:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{authStore.userProfile['username']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Email address:</p>
                                    </td>
                                    <td class="relative text-xs text-gray-600 font-medium md:text-sm">
                                        {{authStore.userProfile['email']}}
                                        <IconCheckCircleSolid
                                            v-if="authStore.userProfile['is_verified']"
                                            class="absolute top-4 right-0 w-5 h-5 fill-green-500 cursor-pointer"
                                            v-tippy="{content: 'Email address verified', animation: 'scale', theme: 'translucent', placement: 'left'}" />
                                        <IconInfoCircleSolid
                                            v-else
                                            class="absolute top-4 right-0 w-5 h-5 fill-red-500 cursor-pointer"
                                            v-tippy="{content: 'Please verify your email address', animation: 'scale', theme: 'translucent', placement: 'left'}" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconCalenderOutline :strokeWidth="1" class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Date joined:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{formatDate(authStore.userProfile['date_joined'])}}</td>
                                </tr>
                                <tr class="">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconClockOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Last seen:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{formatDate(authStore.userProfile['last_login'])}}</td>
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

                        <AppMyApp title="My first app" description="Description about this app" />

                        <AppEmptyState  class="border-gray-200">
                            <template #head>
                                <p class="text-xs text-gray-400 font-medium md:text-sm">1/2 Apps</p>
                            </template>
                            <template #body>
                                <p class="text-xs text-gray-400 font-light md:text-sm">Get started by creating an app</p>
                            </template>
                            <template #tail>
                                <RouterLink :to="{name: 'dashboardappcreate'}" class="flex items-center gap-2 px-2 py-1 bg-blue-400 rounded hover:bg-blue-500">
                                    <IconPlusSolid class="w-5 h-5 fill-white" />
                                    <p class="text-xs text-white font-normal">New App</p>
                                </RouterLink>
                            </template>
                        </AppEmptyState>

                    </div>
                </div>
                <!-- my apps -->

            </div>

        </div>

    </main>
</template>