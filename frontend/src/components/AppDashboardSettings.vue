<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink , useRouter} from 'vue-router';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import IconClockOutline from './icons/IconClockOutline.vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconCogSolid from './icons/IconCogSolid.vue';
import AppEmptyState from './AppEmptyState.vue';
import IconPlusSolid from './icons/IconPlusSolid.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import IconCogOutline from './icons/IconCogOutline.vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';

// router
const router = useRouter()

// refs
const username = ref("")
const email = ref("")
const oldPassword = ref("")
const password1 = ref("")
const password2 = ref("")
const loading = ref(false)
</script>
    
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">
                <h3 class="text-3xl text-gray-600 font-bold md:text-4xl">Account Settings</h3>
            </div>
            <IconCogOutline class="hidden absolute -top-11 right-0 w-86 h-96 stroke-gray-50 md:block"
                :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">
            
            <div class="w-11/12 mx-auto flex flex-col gap-16 md:w-10/12">

                <!-- back link -->
                <span class="w-full flex items-center justify-start">
                    <button type="button" @click.prevent="router.back()" class="group flex items-center gap-2">
                        <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Home</p>
                    </button>
                </span>
                <!-- back link -->

                <!-- profile overview -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">User Settings</h3>

                    <div class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your personalinformation.</p>
                             <!-- form errors -->
                            <span>
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">Hello world</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent="loading = !loading" class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconQRCodeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">UID:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">1234567890</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Username:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="username" label="RealestKMA" :disable="loading" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Email address:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">
                                        <AppInputField v-model="email" type="email" label="kelvinmayoayeni@gmail.com" :disable="loading" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle" class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes" class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>
                    </div>
                </div>
                <!-- profile overview -->


                <!-- my apps -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">My Apps</h3>

                    <div class="grid gap-5 grid-cols-1 sm:grid-cols-2 xl:grid-cols-3">

                        <div
                            class="relative flex flex-col gap-5 bg-white p-6 rounded-lg shadow-lg shadow-gray-200 overflow-hidden group transition-all duration-300 hover:bg-blue-500">
                            <span class="flex items-center justify-between">
                                <span class="flex items-center gap-3">
                                    <IconUserCircleSolid
                                        class="w-5 h-5 fill-gray-600 transition-all duration-300 group-hover:fill-white md:w-10 md:h-10" />
                                    <p class="text-sm text-gray-600 font-medium group-hover:text-white md:text-base">My
                                        openuser app</p>
                                </span>
                                <RouterLink to="#" class="relative">
                                    <IconCogSolid
                                        class="hidden w-7 h-7 fill-white transition-all duration-300 group-hover:block md:w-7 md:h-7" />
                                    <IconCogSolid
                                        class="absolute top-0 hidden w-7 h-7 fill-white transition-all duration-300 group-hover:animate-ping group-hover:block md:w-7 md:h-7" />
                                </RouterLink>
                            </span>
                            <p
                                class="text-xs text-gray-600 font-light transition-all duration-300 group-hover:text-gray-50 md:text-sm">
                                Decription of my openuser app and will then follow, for better understanding
                            </p>
                        </div>

                        <AppEmptyState class="border-gray-200">
                            <template #head>
                                <p class="text-xs text-gray-400 font-medium md:text-sm">No Apps</p>
                            </template>
                            <template #body>
                                <p class="text-xs text-gray-400 font-light md:text-sm">Get started by creating a new app
                                </p>
                            </template>
                            <template #tail>
                                <button type="button"
                                    class="flex items-center gap-2 px-2 py-1 bg-blue-500 group transition-all duration-300 rounded">
                                    <IconPlusSolid class="w-5 h-5 fill-white" />
                                    <p class="text-xs text-white md:text-sm">New app</p>
                                </button>
                            </template>
                        </AppEmptyState>

                    </div>
                </div>
                <!-- my apps -->

            </div>

        </div>

    </main>
</template>