<script setup>
/* eslint-disable */
import { onMounted } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { useAuthStore } from '../stores/auth';

// route && routers
const route = useRoute()

// stores
const authStore = useAuthStore()

// hooks
onMounted(() => {
    authStore.submitVerifyEmail(route.fullPath.slice(route.fullPath.indexOf('?')))
})
</script>

<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="h-full flex flex-col gap-10 items-center mt-40">

            <!-- header -->
            <div class="w-full flex flex-col">
                <h3 class="text-3xl text-gray-900 font-semibold capitalize sm:text-4xl">Verify your email address</h3>
                <span class="mt-2 flex items-center gap-2">
                    <p class="text-xs text-gray-400 font-normal sm:text-sm">Back to</p>
                    <RouterLink :to="{name: 'home'}" class="text-xs text-blue-400 font-medium hover:text-blue-500 sm:text-sm">Home</RouterLink>
                </span>
            </div>

            <span class="w-full">
                <p v-if="authStore.verifyEmail.loading" class="text-xs text-left text-green-500 font-normal animate-bounce-ver md:text-base">Verifying email address, please wait...</p>
                <p v-else-if="authStore.verifyEmail.error" class="text-xs text-left text-red-500 font-normal md:text-base">{{authStore.verifyEmail.error}}</p>
                <p v-else-if="authStore.verifyEmail.data" class="text-xs text-left text-gray-600 font-normal md:text-base">{{authStore.verifyEmail.data}}</p>
            </span>
        
        </div>

    </main>
</template>