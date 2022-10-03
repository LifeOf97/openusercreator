<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import AppPasswordField from './AppPasswordField.vue';

// refs
const password1 = ref("")
const password2 = ref("")
const loading = ref(false)

// stores
const signInStore = useAuthStore()
</script>
                
<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="h-full flex flex-col items-center justify-center mt-28">

            <!-- header -->
            <div class="w-full flex flex-col">
                <h3 class="text-3xl text-gray-900 font-semibold capitalize sm:text-4xl">Reset my password</h3>
                <span class="mt-2 flex items-center gap-2">
                    <p class="text-xs text-gray-400 font-normal sm:text-sm">Back to</p>
                    <RouterLink :to="{name: 'signin'}"
                        class="text-xs text-blue-400 font-medium hover:text-blue-500 sm:text-sm">Sign in</RouterLink>
                </span>
            </div>

            <!-- form errors -->
            <div class="hidden mt-7 w-full list-inside list-disc">
                <span class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">Error details</p>
                </span>
            </div>
            <!-- form errors -->

            <div class="mt-10 mb-5 w-full">
                <p class="text-xs text-gray-600 font-normal md:text-sm">
                    Create a new password.
                </p>
            </div>

            <form @submit.prevent="loading = !loading" class="w-full flex flex-col gap-4 mb-5">
                <AppPasswordField v-model="password1" label="Password" :disable="loading" class="bg-gray-50" />
                <AppPasswordField v-model="password2" label="Confirm password" :disable="loading" class="bg-gray-50" />

                <AppButton label="Reset my password" type="submit" :loading="loading" loadingText="Reseting..."
                    class="mt-2 text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </form>

        </div>
        <!-- form inputs -->

    </main>
</template>