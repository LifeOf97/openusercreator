<script setup>
/* eslint-disable */
import { ref } from 'vue';
import AppButton from './AppButton.vue';

// emits
const emit = defineEmits(["button-clicked"])

// refs
const appName = ref(localStorage.getItem("app_create_name"))
const appDes = ref(localStorage.getItem("app_create_description"))
const appProfiles = ref(localStorage.getItem("app_create_profiles"))
const appPassword = ref(localStorage.getItem("app_create_password"))
</script>

<template>
    <main class="w-11/12 mx-auto bg-transparent sm:w-8/12 lg:w-6/12 xl:w-5/12">

        <div class="flex flex-col gap-4">

            <span class="flex flex-col gap-1 p-6 bg-white text-gray-600 rounded-lg shadow shadow-gray-300">
                <p class="text-xs font-semibold">APP NAME</p>
                <p class="text-sm font-normal md:text-base">{{appName}}</p>
            </span>

            <span class="flex flex-col gap-1 p-6 bg-white text-gray-600 rounded-lg shadow shadow-gray-300">
                <p class="text-xs font-semibold">APP DESCRIPTION</p>
                <p class="text-sm font-normal md:text-base">{{appDes}}</p>
            </span>

            <span class="flex flex-col gap-1 p-6 bg-white text-gray-600 rounded-lg shadow shadow-gray-300">
                <p class="text-xs font-semibold">APP USER PROFILES</p>
                <p class="text-sm font-normal md:text-base">{{appProfiles}}</p>
            </span>

            <span class="flex flex-col gap-1 p-6 bg-white text-gray-600 rounded-lg shadow shadow-gray-300">
                <p class="text-xs font-semibold">APP USER PROFILE PASSWORD</p>
                <p class="text-sm font-normal md:text-base">{{appPassword}}</p>
            </span>

            <div class="flex items-center justify-center mt-10 gap-2">
                <AppButton @click.prevent="$emit('button-clicked', 'back')" type="button" label="Back"
                    class="text-gray-900 bg-transparent hover:bg-white disabled:bg-gray-300" />
                <AppButton  @click.prevent="$emit('button-clicked', 'next')" type="button" label="Create App"
                    class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </div>

        </div>

    </main>
</template>