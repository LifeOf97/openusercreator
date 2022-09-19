<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { onMounted, onUnmounted } from 'vue';
import { RouterLink } from 'vue-router';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconGithub from './icons/IconGithub.vue';

// refs
const root = ref(null)
const isAuth = ref(true)
const toggleUserMenu = ref(false)

// methods
const closeUserMenu = (e) => {
    if (!root.value.contains(e.target)) {
        toggleUserMenu.value = false;
    }
}

// hooks
onMounted(() => {
    document.addEventListener("click", closeUserMenu)
})

onUnmounted(() => {
    document.removeEventListener("click", closeUserMenu)
})
</script>

<template>
    <main ref="root" class="w-full pt-7 z-20">
        <div class="w-11/12 mx-auto flex justify-between items-center px-4 py-2 rounded-2xl shadow-md shadow-gray-300 bg-gray-50 md:px-6 md:w-9/12">

            <!-- logo -->
            <IconUserCircleSolid class="w-7 h-7 fill-red-500 md:w-10 md:h-10" />
            <!-- logo -->
            
            <div class="flex items-center gap-2 font-normal">
                <a href="#" class="border-r border-gray-300 pr-2 group">
                    <IconGithub class="w-6 h-6 fill-gray-500 group-hover:fill-blue-500" />
                </a>

                <!-- Visible when a user is authenticated -->
                <div v-if="isAuth" class="relative flex items-center">
                    <button
                        type="button"
                        @click="toggleUserMenu = !toggleUserMenu"
                        :class="toggleUserMenu ? 'ring-2':''"
                        class="w-6 h-6 bg-teal-400 rounded-full outline-none overflow-hidden ring-teal-400 ring-offset-2 ring-offset-gray-50 transition-all duration-200 hover:ring-2 md:w-8 md:h-8">
                        <p class="text-white text-xs font-bold md:text-base">R</p>
                    </button>

                    <transition
                        name="user-menu"
                        enter-from-class="-translate-y-5 opacity-0"
                        enter-active-class="transition-all duration-200"
                        leave-to-class="-translate-y-5 opacity-0"
                        leave-active-class="transition-all duration-200">
                            <div v-if="toggleUserMenu" class="absolute top-12 -right-5 bg-gray-50 w-40 h-40 shadow-md rounded z-10"></div>
                    </transition>

                </div>
                <!-- Visible when a user is authenticated -->
                
                 <!-- Visible when no user is authenticated -->
                <div v-else class="flex items-center gap-2">
                    <RouterLink to="#" class="text-xs text-gray-800 bg-transparent px-4 py-2 rounded-md transition-colors duration-300 hover:bg-white md:text-base">Log in</RouterLink>
                    <RouterLink to="#" class="text-xs text-white bg-teal-400 px-4 py-2 rounded-md transition-colors duration-300 hover:bg-teal-500 md:text-base">Sign up</RouterLink>
                </div>
                 <!-- Visible when no user is authenticated -->
            </div>

        </div>
    </main>
</template>