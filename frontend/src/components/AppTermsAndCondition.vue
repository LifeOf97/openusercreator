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
                <h1 class="text-2xl text-gray-900 font-bold md:text-4xl">Terms</h1>
                <RouterLink :to="{ name: 'home' }" class="group flex items-center gap-2">
                    <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                    <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Home</p>
                </RouterLink>
            </div>
            <!-- back link and logo -->

            <div class="flex flex-col gap-5 text-gray-600">
                <p class="text-sm font-medium md:text-base">Last Update: October 12, 2022</p>

                <span class="text-sm font-normal md:text-base">
                    Open User is an open source fully functional free fake user data API for testing
                    and prototyping, with authentication provided. Can also be referred to as “Open User,”
                    “Open User Data,” ”Open User Creator” “we,” or “our,” operates the
                    <RouterLink :to="{ name: 'home' }" class="text-blue-500 hover:text-blue-600">www.openuser.xyz
                    </RouterLink>
                    and
                    <a href="#" class="text-blue-500 hover:text-blue-600">api.openuserdata.xyz</a>
                    website and offers services available on the www.openuser.xyz website.
                </span>

                <span class="text-sm font-normal md:text-base">
                    Your access to and use of the Service is conditioned on your acceptance of and
                    compliance with these Terms and Conditions (the “Terms.”) These Terms apply to
                    "Open User" users and all visitors of the www.openuser.xyz website. By accessing
                    or using the Service, you agree to be bound by these Terms. If you disagree with
                    any part of the Terms, then you may not access the Service.
                </span>

                <span class="text-sm font-normal md:text-base">
                    The service "We", "Open user" provides is free and open source, every infomation
                    stored on the API server is visible to all users who make request to the API,
                    and you are advised not to store any confidential information on the system whatsoever.
                </span>

                <span class="text-sm font-normal md:text-base">
                    Please note that all information automatically created by the system or users of
                    the system is completely fake and referred to as dummy values, this details be
                    it (username, email, first name, last name, other name, date of birth, and mugshot)
                    do not depict real life details about people. In situations where this detail are
                    identical or feels identical to people in real life, then it is purely coincidental
                    and should not be taking to heart.
                </span>
            </div>
        </div>

        <AppHomeFooter />

    </main>
</template>
