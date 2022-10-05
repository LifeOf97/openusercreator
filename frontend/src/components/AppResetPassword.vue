<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import AppPasswordField from './AppPasswordField.vue';

// route && router
const route = useRoute()

// refs
const password1 = ref("")
const password2 = ref("")
const error = ref(null)

// stores
const authStore = useAuthStore()

// methods
const submit = () => {
    error.value = null

    const data = {
        uid: route.params['uid'],
        token: route.params['token'],
        new_password1: password1.value,
        new_password2: password2.value
    }

    if (password2.value === password1.value) {
        authStore.submitResetPassword(
            route.params['uid'],
            route.params['token'],
            data
        )
    }
    else error.value = "Password fields does not match"
}
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
            <div  v-if="error || authStore.resetPassword.error" class="mt-7 w-full flex flex-col gap-1">
                <span v-if="error" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{error}}</p>
                </span>
                <span v-if="authStore.resetPassword.error" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.resetPassword.error}}</p>
                </span>
            </div>
            <!-- form errors -->

            <div class="mt-10 mb-5 w-full">
                <p class="text-xs text-gray-600 font-normal md:text-sm">
                    Create a new password.
                </p>
            </div>

            <form @submit.prevent="submit()" class="w-full flex flex-col gap-4 mb-5">
                <AppPasswordField v-model="password1" label="Password" :disable="authStore.resetPassword.loading" class="bg-gray-50" />
                <AppPasswordField v-model="password2" label="Confirm password" :disable="authStore.resetPassword.loading" class="bg-gray-50" />

                <AppButton
                    label="Save password"
                    type="submit"
                    :loading="authStore.resetPassword.loading"
                    loadingText="Reseting..."
                    class="mt-2 text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </form>

        </div>
        <!-- form inputs -->

    </main>
</template>