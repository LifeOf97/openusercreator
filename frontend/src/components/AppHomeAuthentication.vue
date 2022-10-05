<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconLockClosedSolid from './icons/IconLockClosedSolid.vue';
import IconKeySolid from './icons/IconKeySolid.vue';
import IconLinkSolid from './icons/IconLinkSolid.vue';
</script>

<template>
    <main id="authentication" class="relative w-11/12 mx-auto h-full flex flex-col gap-5 bg-white py-20 border-b border-gray-100 lg:py-40 lg:w-10/12">

        <!-- this tag is only visible on small screens -->
        <RouterLink to="#authentication" class="inline-flex items-center gap-2 md:hidden">
            <IconLinkSolid class="w-5 h-5 fill-gray-400" />
            <p class="px-4 py-2 bg-green-500 rounded-full text-xs text-white font-semibold">Authentication</p>
        </RouterLink>
        <!-- this tag is only visible on small screens -->

        <div class="flex flex-col items-center justify-center gap-10 md:flex-row">

            <!-- crud text and table -->
            <div class="flex-1 flex flex-col gap-12 order-1 md:order-2">
                
                <div class="w-full flex flex-col gap-3">
                    <h3 class="text-xl font-semibold text-gray-900 md:text-3xl">Token Based Authentication</h3>
                    <p class="text-xs text-gray-600 font-light md:text-sm">
                        Open user data uses JWT (JSON WEB TOKEN) for it's token based authentication.
                        Once you make a POST request with a valid username/email & password to the login
                        via token endpoint, a refresh and access token will be sent back as response.
                        This access token should be passed in the Authorization request header as a Bearer token
                        for further request requiring authentication.
                    </p>
                </div>

                <div class="w-full flex flex-col gap-3">
                    <h3 class="text-xl font-semibold text-gray-900 md:text-3xl">Session Based Authentication</h3>
                    <p class="text-xs text-gray-600 font-light md:text-sm">
                        Session based authentication keeps authentication details in the form of cookies.
                        Once you make a POST request with a valid username/email & password to the login via
                        session endpoint, a sessionid is then added to the response cookies which is then
                        sent back and forth on every request so the server can verify the user making the request.
                    </p>
                </div>

            </div>
            <!-- crud text and table -->

            <div class="flex-1 grid grid-cols-2 items-start content-center order-2 md:order-1">
                <div class="justify-self-start bg-yellow-400 p-5 rounded-md col-start-2">
                    <IconLockClosedSolid class="w-20 h-20 fill-white md:w-32 md:h-32 lg:w-40 lg:h-40" />
                </div>
                <div class="justify-self-end bg-gray-600 p-5 rounded-md">
                    <IconKeySolid class="w-20 h-20 fill-white md:w-32 md:h-32 lg:w-40 lg:h-40" />
                </div>
            </div>
            
        </div>
        
    </main>
</template>