<script setup>
/* eslint-disable */
import { RouterView } from "vue-router";
import { useAuthStore } from "./stores/auth";
import AppModalState from "./components/AppModalState.vue";
import AppButton from "./components/AppButton.vue";
import IconLogoutOutline from "./components/icons/IconLogoutOutline.vue";
import { onMounted } from "vue";
import VueCookies from "vue-cookies";
import AppNotificationState from "./components/AppNotificationState.vue";
import IconCheckCircleSolid from "./components/icons/IconCheckCircleSolid.vue";
import IconInfoCircleSolid from "./components/icons/IconInfoCircleSolid.vue";

// stores
const authStore = useAuthStore()

// methods
const getUserProfile = () => {
  if (VueCookies.get("access") && !authStore.userProfile) authStore.getUserProfile()
  else if (!VueCookies.get("access")) authStore.submitSignOut()
  else authStore.submitSignOut()
}

// hooks
onMounted(() => {
  // check user data is present
  // getUserProfile()
})
</script>

<template>
  <main>
    <RouterView />

    <!-- notification -->
    <transition
      name="slide"
      enter-from-class="-translate-y-5 opacity-0"
      enter-active-class="transition-all duration-700"
      leave-to-class="-translate-y-5 opacity-0"
      leave-active-class="transition-all duration-700">
      <div v-if="authStore.notify.open" class="w-full bg-transparent absolute top-24 flex items-center justify-center z-30">
        <AppNotificationState @closeBtnClicked="authStore.notify.open = false">
          <template #icon>
            <IconCheckCircleSolid v-if="authStore.notify.state == 'good'" class="w-7 h-7 fill-green-500" />
            <IconInfoCircleSolid v-else-if="authStore.notify.state == 'error'" class="w-7 h-7 fill-yellow-500" />
          </template>
          <template #title>
            {{authStore.notify.detail}}
          </template>
        </AppNotificationState>
      </div>
    </transition>
    <!-- notification -->

    <!-- teleports -->
    <teleport to="body">
      <transition name="modal" enter-from-class="scale-0 opacity-0" enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0" leave-active-class="transition-all duration-200">
        <div v-if="authStore.signOut"
          class="w-full h-screen flex items-center justify-center fixed top-0 bg-gray-500/50 backdrop-blur-lg z-20">

          <AppModalState>

            <template #icon>
              <IconLogoutOutline class="w-4 h-4 fill-red-600 md:w-7 md:h-7" />
            </template>

            <template #title>
              Sign Out
            </template>

            <template #details>
              Are you sure you want to sign out?
            </template>

            <template #actions>
              <AppButton @click.prevent="authStore.signOut = false" type="button" label="Cancle"
                class="text-gray-900 hover:bg-white" />
              <AppButton @click.prevent="authStore.submitSignOut()" type="button" label="Yes, sign out"
                class="text-white bg-red-500 hover:bg-red-600" />
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