<script setup>
/* eslint-disable */
import { computed, onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppInputField from './AppInputField.vue';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import AppPasswordField from './AppPasswordField.vue';
import AppButton from './AppButton.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconGithub from './icons/IconGithub.vue';
import IconGoogle from './icons/IconGoogle.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';

// refs
const username = ref("")
const email = ref("")
const password1 = ref("")
const password2 = ref("")
const error = ref(null)

// stores
const authStore = useAuthStore()

// methods
const submit = () => {
    if (password2.value === password1.value) {
        error.value = null
        const data = {
            username: username.value,
            email: email.value,
            password: password2.value
        }
        authStore.submitSignUp(data)
    }
    else error.value = "Password fields does not match"
}

// computed
const isError = computed(() => {
    return error.value || authStore.signUp.error || authStore.signUp.username || authStore.signUp.email
})

// hooks
onMounted(() => {
    authStore.getGithubUrl()
    authStore.getTwitterUrl()
    authStore.getGoogleUrl()
})
</script>

<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="w-full h-full flex flex-col items-center mt-20">

            <!-- header -->
            <div class="w-full flex flex-col">
                <p class="my-6 self-start px-4 py-2 text-xs text-white font-semibold bg-gray-700 rounded-full">It's free
                </p>
                <h3 class="text-3xl text-gray-900 font-semibold sm:text-4xl">Become a Creator</h3>
                <span class="mt-2 flex items-center gap-2">
                    <p class="text-xs text-gray-400 font-normal sm:text-sm">Already a creator?</p>
                    <RouterLink :to="{name: 'signin'}"
                        class="text-xs text-blue-400 font-medium hover:text-blue-500 sm:text-sm">Sign in</RouterLink>
                </span>
            </div>

            <!-- form errors -->
            <div  v-if="isError" class="mt-7 w-full flex flex-col gap-1">
                <span v-if="error" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{error}}</p>
                </span>
                <span v-if="authStore.signUp.error" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUp.error}}</p>
                </span>
                <span v-if="authStore.signUp.username" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUp.username}}</p>
                </span>
                <span v-if="authStore.signUp.email" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUp.email}}</p>
                </span>
            </div>
            <!-- form errors -->

            <form @submit.prevent="submit()" class="w-full flex flex-col gap-4 mt-12 mb-5">
                <AppInputField v-model.lower="username" type="text" label="Username" :minLen="4" :maxLen="15"
                    iconPos="left" :disable="authStore.signUp.loading" class="bg-gray-50">
                    <template #icon>
                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <AppInputField v-model.lower="email" type="email" label="email" iconPos="left" :disable="authStore.signUp.loading" class="bg-gray-50">
                    <template #icon>
                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <div class="grid grid-cols-1 gap-4 pb-2 sm:grid-cols-2">
                    <AppPasswordField v-model="password1" label="Password" :disable="authStore.signUp.loading" class="bg-gray-50">
                        <template #icon>
                            <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppPasswordField>
                    <AppPasswordField v-model="password2" label="Confirm password" :disable="authStore.signUp.loading" class="bg-gray-50">
                        <template #icon>
                            <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppPasswordField>
                </div>
                <AppButton label="Create Account" type="submit" :loading="authStore.signUp.loading"
                    class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </form>

            <div class="w-full flex flex-col gap-5">
                <div class="w-full flex items-center">
                    <div class="w-full border-b border-gray-300"></div>
                    <span class="w-full text-xs text-center text-gray-400 font-light sm:text-sm">Or continue with</span>
                    <div class="w-full border-b border-gray-300"></div>
                </div>

                <div class="relative flex items-center gap-4">
                    <a :href="authStore.socialGithub.url" @click="authStore.setSocial('github')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconGithub class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </a>
                    <a :href="authStore.socialTwitter.url" @click="authStore.setSocial('twitter')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconTwitter class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </a>
                    <a :href="authStore.socialGoogle.url" @click="authStore.setSocial('google')"
                        class="w-full flex items-center justify-center p-2 rounded bg-transparent border border-gray-300 group transition-all duration-300 cursor-pointer hover:bg-gray-900">
                        <IconGoogle class="w-7 h-7 fill-gray-400 transition-all duration-300 group-hover:fill-white" />
                    </a>

                    <!-- shows up when form is submitting to disable social links -->
                    <div v-show="authStore.signUp.loading" class="absolute top-0 w-full h-full bg-transparent cursor-not-allowed"></div>
                    <!-- shows up when form is submitting to disable social links -->

                </div>
            </div>

        </div>
        <!-- form inputs -->

    </main>
</template>