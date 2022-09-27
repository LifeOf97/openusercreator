<script setup>
/* eslint-disable */
import { RouterView } from "vue-router";
import { useAuthStore } from "./stores/auth";
import AppModalState from "./components/AppModalState.vue";
import AppButton from "./components/AppButton.vue";
import IconLogoutOutline from "./components/icons/IconLogoutOutline.vue";

// stores
const authStore = useAuthStore()
</script>

<template>
  <main>
    <RouterView />

    <teleport to="body">
      <transition
        name="modal"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="authStore.signOut" class="w-full h-screen flex items-center justify-center fixed top-0 bg-gray-500/50 backdrop-blur-lg z-20">
          
            <AppModalState>

              <template #icon>
                <IconLogoutOutline class="w-4 h-4 fill-red-600 md:w-7 md:h-7"/>
              </template>

              <template #title>
                Sign Out
              </template>

              <template #details>
                Are you sure you want to sign out?
              </template>

              <template #actions>
                <AppButton @click.prevent="authStore.signOut = false" type="button" label="Cancle" class="text-gray-900 hover:bg-white" />
                <AppButton type="button" label="Yes, sign out" class="text-white bg-red-500 hover:bg-red-600" />
              </template>

            </AppModalState>
          </div>
      </transition>

    </teleport>

  </main>
</template>

<style>
  .slide-right-enter-active,
  .slide-right-leave-active,
  .slide-left-enter-active,
  .slide-left-leave-active {
    @apply transition-all duration-200
  }
  .slide-right-enter-from {
    @apply -translate-x-20 opacity-0
  }
  .slide-left-enter-from {
    @apply translate-x-20 opacity-0
  }
</style>