<script setup>
/* eslint-disable */
import { RouterLink } from "vue-router";
import IconArrowLongLeft from "./icons/IconArrowLongLeft.vue";
import AppTopNav from "./AppTopNav.vue";
import AppHomeFooter from "./AppHomeFooter.vue";
</script>

<template>
    <main class="w-full h-full bg-transparent">

        <AppTopNav />

        <div class="w-11/12 mx-auto h-full flex flex-col gap-10 items-center mt-32 mb-10 md:mb-20 md:gap-16 md:w-9/12">
            
            <!-- back link and logo -->
            <div class="w-full flex items-center justify-between">
                <h1 class="text-2xl text-gray-900 font-bold md:text-4xl">Privacy Policy</h1>
                <RouterLink :to="{ name: 'home' }" class="group flex items-center gap-2">
                    <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                    <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Home</p>
                </RouterLink>
            </div>
            <!-- back link and logo -->

            <div class="flex flex-col gap-5 text-gray-600">
                <p class="text-sm font-medium md:text-base">Last Update: October 12, 2022</p>

                <span class="text-sm font-normal md:text-base">
                    The Privacy Policy applies to the processing of personal data in connection with the provision
                    of services available on
                    <RouterLink :to="{ name: 'home' }" class="text-blue-500 hover:text-blue-600">www.openuser.xyz
                    </RouterLink>.
                </span>

                <span class="text-sm font-normal md:text-base">
                    Connecting via any of the provided third party platforms are fully secure.
                    Just your basic profile details are used by "Us", "We", "Open User". We do not
                    make use of your profile images. Just your username and email address.
                </span>

                <span class="text-sm font-normal md:text-base">
                    You can delete your account at any time
                </span>

                <span class="text-sm font-normal md:text-base">
                    Please, i will really appreciate any feedback on the service. God bless you.
                </span>
            </div>
        </div>

        <AppHomeFooter />

    </main>
</template>
