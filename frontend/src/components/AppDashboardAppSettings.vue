<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAppStore } from '../stores/apps'
import IconQRCodeOutline from './icons/IconQRCodeOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import IconCogOutline from './icons/IconCogOutline.vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';
import IconCubeOutline from './icons/IconCubeOutline.vue';
import IconUserGroupOutline from './icons/IconUserGroupOutline.vue';
import IconHashtag from './icons/IconHashtag.vue';
import { useTitle } from '@vueuse/core';

// router
const router = useRouter()

// stores
const appStore = useAppStore()

// refs
const appName = ref("")
const appDes = ref("")
const appUserProfiles = ref("")
const appUserPassword = ref("")

// hooks
onMounted(() => {
    useTitle(`Apps | ${appStore.appInView['name'].replaceAll("-", " ")} | Settings`)
})
</script>
        
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto flex flex-col gap-2 md:w-10/12">
                <h3 class="text-sm text-gray-400 font-medium md:text-lg">Settings</h3>
                <h3 class="text-3xl text-gray-600 font-bold capitalize md:text-4xl">{{appStore.appInView['name'].replaceAll("-", " ")}}</h3>
            </div>
            <IconCogOutline class="hidden absolute -top-11 right-0 w-86 h-96 stroke-gray-50 md:block"
                :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">

            <div class="w-11/12 mx-auto flex flex-col gap-16 md:w-10/12">

                <!-- back button -->
                <span class="w-full flex items-center justify-start">
                    <button type="button" @click.prevent="router.back()" class="group flex items-center gap-2">
                        <IconArrowLongLeft
                            class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p
                            class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">
                            Back</p>
                    </button>
                </span>
                <!-- back button -->

                <!-- app settings -->
                <div class="flex flex-col gap-5">
                    <h3 class="text-xl text-gray-600 font-normal md:text-2xl">App Details</h3>

                    <div class="w-full flex flex-col bg-white rounded shadow-lg shadow-gray-200 overflow-auto">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">Below are your app details.</p>
                            <!-- form errors -->
                            <span class="hidden">
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">Error</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-4">
                                        <IconQRCodeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App ID:</p>
                                    </td>
                                    <td class="text-xs text-gray-600 font-medium md:text-sm">{{appStore.appInView['id']}}</td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconCubeOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Name:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="appName" :label="appStore.appInView['name'].replaceAll('-', ' ')" />
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconHashtag class="w-5 h-5 fill-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Description:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="appDes" :label="appStore.appInView['description']" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle"
                                    class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes" loadingText="Saving..."
                                    class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>
                    </div>
                </div>
                <!-- app settings -->

                <!-- app user profiles -->
                <div class="flex flex-col gap-5">

                    <div class="w-full flex flex-col bg-white rounded overflow-auto shadow-lg shadow-gray-200">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">The number of user profiles in your app.</p>
                            <!-- form errors -->
                            <span class="hidden">
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">error</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconUserGroupOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App User Profiles:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="appUserProfiles" :label="appStore.appInView['profiles']" type="number" :minLen="5" :maxLen="50" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle"
                                    class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes"
                                    loadingText="Saving..."
                                    class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>

                    </div>
                </div>
                <!-- app users profiles -->

                <!-- app user password -->
                <div class="flex flex-col gap-5">

                    <div class="w-full flex flex-col bg-white rounded overflow-auto shadow-lg shadow-gray-200">
                        <div class="flex flex-col gap-4 justify-center p-4 border-b border-gray-100">
                            <p class="text-sm text-gray-500 font-normal md:text-base">The default password for all user profiles in your app.</p>
                            <!-- form errors -->
                            <span class="hidden">
                                <span class="flex items-center gap-2">
                                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                                    <p class="text-xs text-red-500 font-normal">error</p>
                                </span>
                            </span>
                            <!-- form errors -->
                        </div>

                        <form @submit.prevent class="w-full p-4">
                            <table class="w-full table-auto">
                                <tr class="border-b border-gray-100">
                                    <td class="flex items-center gap-3 py-6">
                                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                                        <p class="text-xs text-gray-400 font-normal md:text-sm">App Users Password:</p>
                                    </td>
                                    <td>
                                        <AppInputField v-model="appUserPassword" :label="appStore.appInView['profile_password']" />
                                    </td>
                                </tr>
                            </table>

                            <div class="flex items-center justify-end gap-5 pt-4">
                                <AppButton label="Cancle"
                                    class="text-gray-900 bg-transparent transition-all duration-300 hover:bg-gray-100" />
                                <AppButton type="submit" label="Save changes"
                                    loadingText="Saving..."
                                    class="text-white bg-blue-400 transition-all duration-300 hover:bg-blue-500" />
                            </div>
                        </form>

                    </div>
                </div>
                <!-- app user password -->


                <div class="w-full flex items-center justify-center">
                    <AppButton @click.prevent="appStore.deleteApp = true" label="Delete App"
                        class="text-white bg-red-500 transition-all duration-300 hover:bg-red-600" />
                </div>

            </div>

        </div>

    </main>
</template>