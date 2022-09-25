<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterView } from 'vue-router';
import { useUserStore } from '../stores/user';
import { useAppStore } from '../stores/apps';
import AppTopNav from '../components/AppTopNav.vue';
import AppModalState from '../components/AppModalState.vue';
import AppInputField from '../components/AppInputField.vue';
import IconUserCircleOutline from '../components/icons/IconUserCircleOutline.vue';
import AppButton from '../components/AppButton.vue';
import IconCubeOutline from '../components/icons/IconCubeOutline.vue';

// stores
const userStore = useUserStore()
const appStore = useAppStore()

// refs
const username = ref("")
const appName = ref("")

// methods
const closeAccountModal = () => {
    userStore.deleteAccount = false
    username.value = ""
}
const closeAppModal = () => {
    appStore.deleteApp = false
    appName.value = ""
}
</script>

<template>
    <main class="relative w-full h-full min-h-[20rem] bg-cover bg-center md:min-h-[40rem]">

        <div class="w-full absolute top-0 z-10">
            <AppTopNav />
        </div>

        <div class="w-full h-full">
            <RouterView />
        </div>

        <!-- delete account -->
        <teleport to="body">
            <transition name="modal" enter-from-class="scale-0 opacity-0"
                enter-active-class="transition-all duration-200" leave-to-class="scale-0 opacity-0"
                leave-active-class="transition-all duration-200">
                <div v-if="userStore.deleteAccount"
                    class="w-full h-screen flex items-center justify-center fixed top-0 bg-gray-500/50 backdrop-blur-lg z-20">
                    <AppModalState>

                        <template #title>
                            Delete my Account
                        </template>

                        <template #details>
                            You are about to delete your account permanently. If you are sure you want to take this
                            action please
                            type in your username in the field provided below. This action cannot be undone.
                        </template>

                        <template #form>
                            <AppInputField v-model="username" :label="userStore.username" iconPos="left">
                                <template #icon>
                                    <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                                </template>
                            </AppInputField>
                        </template>

                        <template #actions>
                            <AppButton @click.prevent="closeAccountModal()" type="button" label="Cancle"
                                class="text-gray-900 hover:bg-white" />
                            <AppButton type="button" label="Delete Account"
                                :disabled="userStore.username.toLowerCase() !== username.toLowerCase()"
                                :class="userStore.username.toLowerCase() == username.toLowerCase() ? 'bg-red-500 hover:bg-red-600':'bg-red-300'"
                                class="text-white" />
                        </template>

                    </AppModalState>
                </div>
            </transition>
        </teleport>
        <!-- delete account -->

        <!-- Delete app modal -->
        <teleport to="body">
            <transition name="modal" enter-from-class="scale-0 opacity-0"
                enter-active-class="transition-all duration-200" leave-to-class="scale-0 opacity-0"
                leave-active-class="transition-all duration-200">
                <div v-if="appStore.deleteApp"
                    class="w-full h-screen flex items-center justify-center fixed top-0 bg-gray-500/50 backdrop-blur-lg z-20">
                    <AppModalState>

                        <template #title>
                            Delete App
                        </template>

                        <template #details>
                            You are about to delete this app permanently. If you are sure you want to take this
                            action please type in the application name in the field provided below. This action cannot be undone.
                        </template>

                        <template #form>
                            <AppInputField v-model="appName" label="My app name" iconPos="left">
                                <template #icon>
                                    <IconCubeOutline class="w-5 h-5 stroke-gray-400" />
                                </template>
                            </AppInputField>
                        </template>

                        <template #actions>
                            <AppButton @click.prevent="closeAppModal()" type="button" label="Cancle"
                                class="text-gray-900 hover:bg-white" />
                            <AppButton type="button" label="Delete Account"
                                :disabled="appStore.appName.toLowerCase() !== appName.toLowerCase()"
                                :class="appStore.appName.toLowerCase() == appName.toLowerCase() ? 'bg-red-500 hover:bg-red-600':'bg-red-300'"
                                class="text-white" />
                        </template>

                    </AppModalState>
                </div>
            </transition>
        </teleport>
        <!-- Delete app modal -->

    </main>
</template>