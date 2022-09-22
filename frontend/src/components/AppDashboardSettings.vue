<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useRouter} from 'vue-router';
import { useUserStore } from '../stores/user';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import IconCogOutline from './icons/IconCogOutline.vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';
import AppPasswordField from './AppPasswordField.vue';

// router
const router = useRouter()

// stores
const userStore = useUserStore()

// refs
const username = ref("")
const email = ref("")
const oldPassword = ref("")
const password1 = ref("")
const password2 = ref("")
const userLoading = ref(false)
const passwordLoading = ref(false)
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

                <!-- user settings -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">User Settings</h3>

                    <div class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your personal information.</p>
                             <!-- form errors -->
                            <span>
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">Hello world</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent="userLoading = !userLoading" class="w-full p-4">
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
                                        <AppInputField v-model="username" label="RealestKMA" :disable="userLoading" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Email address:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="email" type="email" label="kelvinmayoayeni@gmail.com" :disable="userLoading" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle" class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes" :loading="userLoading" loadingText="Saving..." class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>
                    </div>
                </div>
                <!-- user settings -->

                <!-- password settings -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">Password</h3>

                    <div class="w-full flex flex-col bg-white rounded overflow-hidden shadow-lg shadow-gray-200">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Change your password.</p>
                             <!-- form errors -->
                            <span>
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">Hello world</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent="passwordLoading = !passwordLoading" class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Old Password:</p>
                                    </td>
                                    <td>
                                        <AppPasswordField v-model="oldPassword" label="Old Password" :disable="passwordLoading" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">New Password:</p>
                                    </td>
                                    <td>
                                        <AppPasswordField v-model="password1" label="New Password" :disable="passwordLoading" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">Confirm Password:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">
                                        <AppPasswordField v-model="password2" label="Confirm Password" :disable="passwordLoading" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle" class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes" :loading="passwordLoading" loadingText="Saving..." class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>

                    </div>
                </div>
                <!-- profile overview -->
                
                <div class="w-full flex items-center justify-center">
                    <AppButton @click.prevent="userStore.deleteAccount = true" label="Delete my Account" class="text-white bg-red-500 transition-all duration-300 hover:bg-red-600" />
                </div>

            </div>

        </div>

    </main>
</template>