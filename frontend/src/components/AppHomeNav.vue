<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';

// route
const route = useRoute()
</script>

<template>
    <main class="w-11/12 mx-auto flex items-center justify-end gap-2 text-xs font-medium overflow-x-auto md:text-sm md:gap-5 lg:w-10/12">

        <RouterLink
            to="#crud"
            :class="route.fullPath.endsWith('crud') ? 'bg-red-600 text-white border-transparent':'text-gray-500'"
            class="shrink-0 px-4 py-1 bg-white rounded-xl border border-gray-300 transition-all duration-300 hover:bg-red-600 hover:border-transparent hover:text-white md:py-2">
                CRUD
        </RouterLink>

        <RouterLink
            to="#authentication"
            :class="route.fullPath.endsWith('authentication') ? 'bg-green-500 text-white border-transparent':'text-gray-500'"
            class="shrink-0 px-4 py-1 bg-white rounded-xl border border-gray-300 transition-all duration-300 hover:bg-green-500 hover:border-transparent hover:text-white md:py-2">
                Authentication
        </RouterLink>

        <RouterLink
            to="#ResourcesandEndpoints"
            :class="route.fullPath.endsWith('ResourcesandEndpoints') ? 'bg-blue-500 text-white border-transparent':'text-gray-500'"
            class="shrink-0 px-4 py-1 bg-white rounded-xl border border-gray-300 transition-all duration-300 hover:bg-blue-500 hover:border-transparent hover:text-white md:py-2">
                Resources & Endpoints
        </RouterLink>

        <RouterLink
            to="#QueryParameters"
            :class="route.fullPath.endsWith('QueryParameters') ? 'bg-yellow-400 text-white border-transparent':'text-gray-500'"
            class="shrink-0 px-4 py-1 bg-white rounded-xl border border-gray-300 transition-all duration-300 hover:bg-yellow-400 hover:border-transparent hover:text-white md:py-2">
                Query Parameters
        </RouterLink>


    </main>
</template>