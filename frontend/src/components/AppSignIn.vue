<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppInputField from './AppInputField.vue';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import AppPasswordField from './AppPasswordField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconGithub from './icons/IconGithub.vue';
import IconGoogle from './icons/IconGoogle.vue';
import IconTwitter from './icons/IconTwitter.vue';
import AppCheckbox from './AppCheckbox.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';

// refs
const username = ref("")
const password = ref("")
const rememberMe = ref(false)
const loading = ref(false)

// stores
const signInStore = useAuthStore()
</script>
        
<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="h-full flex flex-col items-center justify-center mt-24">

            <!-- header -->
            <div class="w-full flex flex-col">
                <h3 class="text-3xl text-gray-900 font-semibold capitalize sm:text-4xl">Sign into your account</h3>
                <span class="mt-2 flex items-center gap-2">
                    <p class="text-xs text-gray-400 font-normal sm:text-sm">Don't have an account?</p>
                    <RouterLink :to="{name: 'signup'}"
                        class="text-xs text-blue-400 font-medium hover:text-blue-500 sm:text-sm">Create one</RouterLink>
                </span>
            </div>

            <!-- form errors -->
            <div class="hidden mt-7 w-full list-inside list-disc">
                <span class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">Hello world</p>
                </span>
            </div>
            <!-- form errors -->

            <form @submit.prevent="loading = !loading" class="w-full flex flex-col gap-4 mt-12 mb-5">
                <AppInputField v-model="username" type="text" label="Username or Email address" :minLen="4"
                    iconPos="left" :disable="loading" class="bg-gray-50">
                    <template #icon>
                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <AppPasswordField v-model="password" label="password" :disable="loading" class="bg-gray-50">
                    <template #icon>
                        <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppPasswordField>

                <div class="mt-2 flex items-center justify-between">
                    <AppCheckbox v-model="rememberMe" label="Remember me" />
                    <RouterLink :to="{name: 'forgotpassword'}"
                        class="text-xs text-blue-400 font-medium hover:text-blue-500 sm:text-sm">Forgot password?
                    </RouterLink>
                </div>

                <AppButton label="Sign in" type="submit" :loading="loading"
                    class="mt-2 text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </form>


            <div class="w-full flex flex-col gap-5">
                <div class="w-full flex items-center">
                    <div class="w-full border-b border-gray-300"></div>
                    <span class="w-full text-xs text-center text-gray-400 font-light sm:text-sm">Or continue with</span>
                    <div class="w-full border-b border-gray-300"></div>
                </div>

                <div class="relative flex items-center gap-4">
                    <RouterLink :to="{name: 'signupsocial'}" @click="signInStore.setSocial('github')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconGithub class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </RouterLink>
                    <RouterLink :to="{name: 'signupsocial'}" @click="signInStore.setSocial('twitter')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconTwitter class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </RouterLink>
                    <RouterLink :to="{name: 'signupsocial'}" @click="signInStore.setSocial('google')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconGoogle class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </RouterLink>

                    <!-- shows up when form is submitting to disable social links -->
                    <div v-show="loading" class="absolute top-0 w-full h-full bg-transparent cursor-not-allowed"></div>
                    <!-- shows up when form is submitting to disable social links -->

                </div>
            </div>

        </div>
        <!-- form inputs -->

    </main>
</template>