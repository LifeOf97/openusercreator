<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import AppInputField from './AppInputField.vue';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import AppPasswordField from './AppPasswordField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconGithub from './icons/IconGithub.vue';
import IconGoogle from './icons/IconGoogle.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';

// refs
const username = ref("")
const email = ref("")
const password1 = ref("")
const password2 = ref("")
const loading = ref(false)
</script>

<template>
    <main class="w-full h-full min-h-[20rem] bg-transparent md:min-h-[40rem]">

        <div class="w-10/12 h-full mx-auto flex flex-col sm:w-9/12 md:w-8/12 lg:w-6/12">

            <!-- back link -->
            <div class="flex items-center justify-between pt-5 md:pt-10 lg:justify-end">
                <IconUserCircleSolid class="w-10 h-10 fill-red-500 lg:hidden" />
                <RouterLink :to="{name: 'home'}" class="group flex items-center gap-2">
                    <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                    <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Back</p>
                </RouterLink>
            </div>
            <!-- back link -->

            <!-- form inputs -->
            <div class="h-full flex flex-col items-center mt-20">

                <!-- header -->
                <div class="w-full flex flex-col">
                    <p class="my-6 self-start px-4 py-2 text-xs text-white font-semibold bg-gray-700 rounded-full">It's free</p>
                    <h3 class="text-3xl text-gray-900 font-semibold sm:text-4xl">Become a Creator</h3>
                    <span class="mt-2 flex items-center gap-2">
                        <p class="text-xs text-gray-400 font-normal sm:text-sm">Already a creator?</p>
                        <RouterLink to="#" class="text-xs text-blue-500 font-medium hover:text-blue-600 sm:text-sm">Sign in</RouterLink>
                    </span>
                </div>

                <!-- form errors -->
                <div class="hidden my-10 w-full list-inside list-disc">
                    <span class="flex items-center gap-2">
                        <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                        <p class="text-xs text-red-500 font-normal md:text-sm">Hello world</p>
                    </span>
                </div>
                <!-- form errors -->

                <form @submit.prevent="loading = !loading" class="w-full flex flex-col gap-4 mt-12 mb-5">
                    <AppInputField v-model="username" type="text" label="Username" minLen="4" maxLen="15" iconPos="left">
                        <template #icon>
                            <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppInputField>
                    <AppInputField v-model="email" type="email" label="email" iconPos="left">
                        <template #icon>
                            <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppInputField>
                    <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                        <AppPasswordField v-model="password1" label="Password" />
                        <AppPasswordField v-model="password2" label="Confirm password" />
                    </div>
                    <AppButton
                        label="Create Account"
                        type="submit"
                        :loading="loading"
                        class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
                </form>

                <div class="w-full flex flex-col gap-5">
                    <div class="w-full flex items-center">
                        <div class="w-full border-b border-gray-300"></div>
                        <span class="w-full text-xs text-center text-gray-400 font-light sm:text-sm">Or continue with</span>
                        <div class="w-full border-b border-gray-300"></div>
                    </div>

                    <div class="flex items-center gap-4">
                        <div class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                            <IconGithub class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                        </div>
                        <div class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                            <IconTwitter class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                        </div>
                        <div class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                            <IconGoogle class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                        </div>
                    </div>
                </div>

            </div>
            <!-- form inputs -->

        </div>

    </main>
</template>