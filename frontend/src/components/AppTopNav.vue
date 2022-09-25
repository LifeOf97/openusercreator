<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { onMounted, onUnmounted } from 'vue';
import IconUserCircleSolid from './icons/IconUserCircleSolid.vue';
import IconGithub from './icons/IconGithub.vue';
import IconLogoutOutline from './icons/IconLogoutOutline.vue';

// stores
const authStore = useAuthStore()

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
        <div class="w-11/12 mx-auto flex justify-between items-center px-4 py-2 rounded-lg shadow-md shadow-gray-300 bg-gray-50 md:px-6 md:w-9/12">

            <!-- logo -->
            <RouterLink :to="{name: 'home'}">
                <IconUserCircleSolid class="w-7 h-7 fill-red-500 md:w-10 md:h-10" />
            </RouterLink>
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
                            <div v-if="toggleUserMenu" class="absolute top-12 -right-5 flex flex-col bg-gray-50 w-44 shadow-md rounded overflow-hidden z-10">
                                <div class="flex flex-col p-2 border-b">
                                    <p class="text-xs text-gray-400 font-medium tracking-tighter">Signed in as</p>
                                    <p class="text-sm text-gray-700 font-medium truncate">RealestKMA</p>
                                </div>
                                <RouterLink :to="{name: 'dashboard'}" @click.prevent="toggleUserMenu = false" class="text-left text-gray-700 text-xs px-4 py-2 transition-all duration-300 hover:text-white hover:bg-teal-400 md:text-sm">
                                    Dashboard
                                </RouterLink>
                                <button type="button" @click.prevent="authStore.signOut = true" class="group text-left text-xs text-gray-500 flex items-center gap-2 px-4 py-2 transition-all duration-300 hover:text-gray-900 hover:bg-white md:text-sm">
                                    <IconLogoutOutline class="w-5 h-5 fill-gray-500 transition-all duration-300 group-hover:fill-red-500" />
                                    <p>Sign out</p>
                                </button>
                            </div>
                    </transition>

                </div>
                <!-- Visible when a user is authenticated -->
                
                 <!-- Visible when no user is authenticated -->
                <div v-else class="flex items-center gap-2">
                    <RouterLink :to="{name: 'signin'}" class="text-xs text-gray-800 bg-transparent px-4 py-2 rounded-md transition-colors duration-300 hover:bg-white md:text-base">Log in</RouterLink>
                    <RouterLink :to="{name: 'signup'}" class="text-xs text-white bg-teal-400 px-4 py-2 rounded-md transition-colors duration-300 hover:bg-teal-500 md:text-base">Sign up</RouterLink>
                </div>
                 <!-- Visible when no user is authenticated -->
            </div>

        </div>
    </main>
</template>