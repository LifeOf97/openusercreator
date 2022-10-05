<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';

// refs
const email = ref("")

// stores
const authStore = useAuthStore()
</script>
            
<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="h-full flex flex-col items-center justify-center mt-28">

            <!-- header -->
            <div class="w-full flex flex-col">
                <h3 class="text-3xl text-gray-900 font-semibold capitalize sm:text-4xl">Forgot Password</h3>
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
                <p class="text-xs text-left text-gray-600 font-normal md:text-sm">
                    Please enter the email address linked to your account, we’ll send you
                    instructions on how to reset your password.
                </p>
            </div>

            <form @submit.prevent="authStore.submitForgotPassword({email: email})" class="w-full flex flex-col gap-4 mb-5">
                <AppInputField
                    v-model.lower="email"
                    type="email"
                    label="Email address"
                    iconPos="left"
                    :disable="authStore.forgotPassword.loading || authStore.forgotPassword.success"
                    class="bg-gray-50">
                    <template #icon>
                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <AppButton
                    label="Send instruction"
                    type="submit"
                    :loading="authStore.forgotPassword.loading"
                    loadingText="Sending..."
                    :disabled="authStore.forgotPassword.loading || authStore.forgotPassword.success"
                    class="mt-2 text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </form>

            <div v-if="authStore.forgotPassword.error || authStore.forgotPassword.success" class="w-full mt-2 flex flex-col gap-5">
                <div class="w-full flex items-center">
                    <div class="w-full border-b border-gray-300"></div>
                    <span
                        :class="authStore.forgotPassword.success ? 'text-green-500':'text-red-500'"
                        class="w-full text-xs font-medium text-center sm:text-sm">Messsage</span>
                    <div class="w-full border-b border-gray-300"></div>
                </div>
                <p v-if="authStore.forgotPassword.success" class="text-xs text-left text-gray-600 font-normal md:text-sm">
                    If this email address belongs to an account, you will recieve an email to reset your email address.
                </p>
                <p v-else-if="authStore.forgotPassword.error" class="text-xs text-left text-gray-600 font-normal md:text-sm">
                    {{authStore.forgotPassword.error}}
                </p>
            </div>

        </div>
        <!-- form inputs -->

    </main>
</template>