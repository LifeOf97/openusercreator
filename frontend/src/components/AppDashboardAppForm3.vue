<script setup>
/* eslint-disable */
import { onMounted, ref, computed } from 'vue';
import AppButton from './AppButton.vue';
import AppPasswordField from './AppPasswordField.vue';

// refs
const appPassword = ref("")
const error = ref(null)

// data
const appName = localStorage.getItem("app_create_name")

// methods
const saveData = () => {
    if (verifyMinValue.value && verifyMaxValue.value) {
        error.value = null
        localStorage.setItem('app_create_profiles', appPassword.value)
    }
    else error.value = "Please correct the error causing fields"
}

// computed
const verifyMinValue = computed(() => {
    return appPassword.value.length >= 8 ? true : false
})

const verifyMaxValue = computed(() => {
    return appPassword.value.length <= 15 ? true : false
})

// hooks
onMounted(() => {
    appPassword.value = localStorage.getItem('app_create_password')
})
</script>
        
<template>
    <main class="w-11/12 mx-auto bg-transparent sm:w-8/12 lg:w-6/12 xl:w-5/12">

        <p class="text-xs text-gray-600 font-medium mb-4 md:text-sm">
            Every user profile in your app needs a password for authentication.
            This password will be given to all user account in your <b>{{appName}}</b> application.
        </p>

        <form @submit.prevent="saveData()" class="flex flex-col gap-5">
            <div class="w-full flex flex-col gap-1">
                <p v-if="error" class="text-xs text-red-500 font-medium mb-4">{{error}}</p>

                <AppPasswordField v-model="appPassword" label="Password" :minLen="8" :maxLen="15" class="bg-white" />
                <div class="flex items-center justify-between">
                    <p :class="verifyMinValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Min: 8</p>
                    <p :class="verifyMaxValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Max: 15</p>
                </div>
            </div>

            <div class="flex items-center justify-center gap-2">
                <AppButton type="button" label="Back"
                    class="text-gray-900 bg-transparent hover:bg-white disabled:bg-gray-300" />
                <AppButton type="submit" label="Next"
                    class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </div>
        </form>

    </main>
</template>