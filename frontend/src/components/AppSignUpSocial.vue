<script setup>
/* eslint-disable */
import { onMounted, ref, computed } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import AppInputField from './AppInputField.vue';
import IconUserCircleOutline from './icons/IconUserCircleOutline.vue';
import IconEnvelopeOutline from './icons/IconEnvelopeOutline.vue';
import AppPasswordField from './AppPasswordField.vue';
import AppButton from './AppButton.vue';
import AppCheckbox from './AppCheckbox.vue';
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
import IconGithub from './icons/IconGithub.vue';
import IconGoogle from './icons/IconGoogle.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconKeyOutline from './icons/IconKeyOutline.vue';
import { useTitle } from '@vueuse/core';
import VueCookies from 'vue-cookies';

// routes & routers
const route = useRoute()
const router = useRouter()

// stores
const authStore = useAuthStore()

// refs
const username = ref("")
const email = ref("")
const password1 = ref("")
const password2 = ref("")
const error = ref(null)
const endpoint = ref("")
const termsAndCons = ref(false)

// methods
const submit = () => {
    const data = {
        username: username.value,
        email: email.value,
        auth_email: authStore.socialData.data['auth_email'],
        auth_provider: authStore.socialData.data['auth_provider'],
        auth_provider_id: authStore.socialData.data['auth_provider_id'],
        password: password2.value
    }

    if (password2.value === password1.value) authStore.submitSignUpSocial(data)
    else error.value = "Password fields does not match"
}

// computed
const isError = computed(() => {
    return error.value || authStore.signUpSocial.error ||
    authStore.signUpSocial.username || authStore.signUpSocial.email
})

// hooks
onMounted(async () => {
    // get user data from social provider via backend
    if (route.fullPath.includes('github')) endpoint.value = "api/v1/auth/github/get/user/"
    else if (route.fullPath.includes('google')) endpoint.value = "api/v1/auth/google/get/user/"
    else if (route.fullPath.includes('twitter')) endpoint.value = "api/v1/auth/twitter/get/user/"

    await authStore.getUserDataViaSocialProvider(
        endpoint.value,
        route.fullPath.slice(route.fullPath.indexOf('?'))
    )
        .then(() => {
            // if user has no account with us, create a new one
            if ('auth_provider' in authStore.socialData.data) {
                username.value = authStore.socialData.data['username']
                email.value = authStore.socialData.data['email']
            }
            // if user has an account with us, sign in the user
            else if ('access' in authStore.socialData.data) {
                // set cookies
                VueCookies.set("refresh", authStore.socialData.data['refresh'], "1d")
                VueCookies.set("access", authStore.socialData.data['access'], "12h")

                // set is authenticated to true
                localStorage.setItem("is_auth", JSON.stringify(true))
                authStore.isAuthenticated = true

                // get user profile
                authStore.getUserProfile()

                // update notify
                authStore.notify.open = true
                authStore.notify.detail = "Signed in successfully"
                authStore.notify.state = "good"
            
                setTimeout(() => {
                    authStore.notify.open = false
                    authStore.notify.detail = authStore.notify.state = null
                }, 10000);

                // remove sensitive data from localstorage
                localStorage.removeItem("auth_social_data")
            }
            else console.log("An error ocured")
        })
        .catch((err) => {
            console.log(err.message)
        })
})

// set page title
useTitle(`Sign Up | ${authStore.social.toUpperCase()} | Open User Data`)

// reset form
authStore.resetSignUpSocila()
</script>

<template>
    <main class="w-full h-full bg-transparent">

        <!-- form inputs -->
        <div class="h-full flex flex-col items-center mt-28">

            <!-- header -->
            <div class="w-full flex flex-col">
                <div class="my-6 self-start px-6 py-2 flex items-center justify-center p-2 rounded bg-gray-900">
                    <IconGithub v-if="authStore.social == 'github'" class="w-7 h-7 fill-white" />
                    <IconTwitter v-else-if="authStore.social == 'twitter'" class="w-7 h-7 fill-white" />
                    <IconGoogle v-else-if="authStore.social == 'google'" class="w-7 h-7 fill-white" />
                </div>
                <h3 class="text-3xl text-gray-900 font-semibold capitalize sm:text-4xl">Connect via
                    {{authStore.social}}</h3>
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
                <span v-if="authStore.signUpSocial.error" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUpSocial.error}}</p>
                </span>
                <span v-if="authStore.signUpSocial.username" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUpSocial.username}}</p>
                </span>
                <span v-if="authStore.signUpSocial.email" class="flex items-center gap-2">
                    <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-500" />
                    <p class="text-xs text-red-500 font-normal md:text-sm">{{authStore.signUpSocial.email}}</p>
                </span>
            </div>
            <!-- form errors -->

            <span class="w-full mt-10 mb-7">
                <p class="text-xs text-left text-gray-600 font-normal md:text-sm">
                    The details populated in the fields below where provided by <b>{{authStore.social.toUpperCase()}}</b>,
                    please provide a password to continue your sign up via <b>{{authStore.social.toUpperCase()}}</b>.
                </p>
            </span>

            <form @submit.prevent="submit()" class="relative w-full flex flex-col gap-4 mb-5">
                <AppInputField v-model.lower="username" type="text" label="Username" :minLen="4" :maxLen="15"
                    iconPos="left" :disable="authStore.signUpSocial.loading" class="bg-gray-50">
                    <template #icon>
                        <IconUserCircleOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <AppInputField v-model.lower="email" type="email" label="email" iconPos="left" :disable="authStore.signUpSocial.loading" class="bg-gray-50">
                    <template #icon>
                        <IconEnvelopeOutline class="w-5 h-5 stroke-gray-400" />
                    </template>
                </AppInputField>
                <div class="grid grid-cols-1 gap-4 pb-2 sm:grid-cols-2">
                    <AppPasswordField v-model="password1" label="Password" :disable="authStore.signUpSocial.loading" class="bg-gray-50">
                        <template #icon>
                            <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppPasswordField>
                    <AppPasswordField v-model="password2" label="Confirm password" :disable="authStore.signUpSocial.loading" class="bg-gray-50">
                        <template #icon>
                            <IconKeyOutline class="w-5 h-5 stroke-gray-400" />
                        </template>
                    </AppPasswordField>
                </div>

                <!-- accept terms and condition -->
                <AppCheckbox v-model="termsAndCons" label="termsAndCons" class="my-3">
                    <template #label>
                        I agree to Open User's
                        <RouterLink :to="{name: 'termsandcondition'}" class="text-blue-500 hover:text-blue-600">Terms & Conditions</RouterLink> and
                        <RouterLink :to="{name: 'privacypolicy'}" class="text-blue-500 hover:text-blue-600">Privacy Policy</RouterLink>
                    </template>
                </AppCheckbox>
                <!-- accept terms and condition -->

                <AppButton
                    label="Create Account"
                    type="submit"
                    :loading="authStore.signUpSocial.loading"
                    loadingText="Creating..."
                    class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />


                <!-- start of effect to show/hide social sign up form -->
                <div v-if="authStore.socialData.loading || authStore.socialData.error" class="absolute top-0 flex items-center justify-center w-full h-full bg-white/10 backdrop-blur-sm">
                    <span v-if="authStore.socialData.loading" class="flex flex-col items-center justify-center gap-2">
                        <p class="text-xs text-gray-900 font-medium animate-bounce-ver md:text-sm">Please wait...</p>
                    </span>
                    <span v-else-if="authStore.socialData.error" class="flex flex-col items-center justify-center gap-2">
                        <p class="text-xs text-gray-900 font-medium md:text-sm">{{authStore.socialData.error}}</p>
                        <RouterLink :to="{name: 'signup'}" class="text-xs text-center font-normal transition-all duration-300 text-white px-4 py-2 bg-blue-500 rounded hover:bg-blue-600 md:text-sm">Back</RouterLink>
                    </span>
                </div>
                <!-- start of effect to show/hide social sign up form -->

            </form>

        </div>
        <!-- form inputs -->

    </main>
</template>