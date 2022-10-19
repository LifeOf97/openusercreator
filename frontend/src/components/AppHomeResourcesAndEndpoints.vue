<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import IconLinkSolid from './icons/IconLinkSolid.vue';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/ScrollTrigger';

// register gsap plugins
gsap.registerPlugin(ScrollTrigger)

// refs
const reqHeaderOne = ref(null)
const reqHeaderTwo = ref(null)
const reqHeaderThree = ref(null)

// data
const data = {
    endpointOne: [
        {id: 1, method: "GET", endpoint: "/users/"},
        {id: 2, method: "GET", endpoint: "/users/:username/"}
    ],
    endpointTwo: [
        {id: 1, method: "GET", endpoint: "/:cid/:app_name/app/users/"},
        {id: 2, method: "GET", endpoint: "/:cid/:app_name/app/users/:username/"},
        {id: 3, method: "POST", endpoint: "/:cid/:app_name/app/users/new/"},
        {id: 4, method: "GET", endpoint: "/:cid/:app_name/app/users/me/"},
        {id: 5, method: "PUT", endpoint: "/:cid/:app_name/app/users/me/update/"},
        {id: 6, method: "PATCH", endpoint: "/:cid/:app_name/app/users/me/update/"},
        {id: 7, method: "DELETE", endpoint: "/:cid/:app_name/app/users/me/delete/"},
    ],
    endpointThree: [
        {id: 1, method: "POST", endpoint: "/auth/login/token/"},
        {id: 2, method: "POST", endpoint: "/auth/refresh/token/"},
        {id: 3, method: "POST", endpoint: "/auth/verify/token/"},
        {id: 4, method: "POST", endpoint: "/auth/login/session/"},
        {id: 5, method: "POST", endpoint: "/auth/logout/session/"},
    ],
}

// methods
const animate = () => {
    gsap.from(
        [reqHeaderOne.value],
        {
            scrollTrigger: {trigger: reqHeaderOne.value, start: "200px bottom"},
            duration: 1.5, y: 50, opacity: 0, stagger: 0.3
        }
    )
    gsap.from(
        [reqHeaderTwo.value],
        {
            scrollTrigger: {trigger: reqHeaderTwo.value, start: "200px bottom"},
            duration: 1.5, y: 50, opacity: 0, stagger: 0.3
        }
    )
    gsap.from(
        [reqHeaderThree.value],
        {
            scrollTrigger: {trigger: reqHeaderThree.value, start: "200px bottom"},
            duration: 1.5, y: 50, opacity: 0, stagger: 0.3
        }
    )
}

// hooks
onMounted(() => {
    animate()
})
</script>

<template>
    <main id="ResourcesandEndpoints" class="w-11/12 mx-auto h-full flex flex-col gap-5 bg-white py-20 border-b border-gray-200 lg:w-10/12">

        <!-- this tag is only visible on small screens -->
        <RouterLink to="#ResourcesandEndpoints" class="inline-flex items-center gap-2 md:hidden">
            <IconLinkSolid class="w-5 h-5 fill-gray-400" />
            <p class="px-4 py-2 bg-blue-500 rounded-full text-xs text-white font-semibold">Docs, Resources & Endpoint</p>
        </RouterLink>
        <!-- this tag is only visible on small screens -->

        <!-- start of docs -->
        <div ref="reqHeaderOne" class="flex flex-col gap-2">
            <h3 class="text-xl text-gray-900 font-semibold md:text-3xl">Documentation</h3>
            
            <span class="pl-5 my-2 flex flex-col gap-2">
                <a href="https://api.openuserdata.xyz/api/v1/schema/swagger/" target="_blank" class="text-xs text-blue-500 md:text-base hover:text-blue-600">Swagger</a>
                <a href="https://api.openuserdata.xyz/api/v1/schema/redoc/" target="_blank" class="text-xs text-blue-500 md:text-base hover:text-blue-600">REDOC</a>
            </span>
        </div>
        <!-- end of docs -->

        <!-- start of resources -->
        <div ref="reqHeaderTwo" class="flex flex-col gap-2">
            <h3 class="text-xl text-gray-900 font-semibold md:text-3xl">Resources</h3>
            <p class="text-xs text-gray-600 font-light md:text-base">Open user data provides only a  user resource for now, but more resources will be added in the future.</p>
            
            <ul class="pl-5 my-2 list-inside">
                <li>
                    <a href="https://api.openuserdata.xyz/api/v1/users/" target="_blank" class="text-xs text-blue-500 md:text-base hover:text-blue-600">/users</a>
                </li>
            </ul>

            <p class="text-xs text-gray-600 font-light md:text-base">
                <b>NOTE:</b> A maximum of 50 users are returned by default, but you can however change this using the
                <RouterLink to="#QueryParameters" class="text-blue-500 hover:text-blue-600">limit/offset</RouterLink>
                url query parameters to increase or decrease the number of users returned.
            </p>
        </div>
        <!-- end of resources -->

        <div ref="reqHeaderThree" class="mt-10 flex flex-col gap-2">
            <h3 class="text-xl text-gray-900 font-semibold md:text-3xl">Endpoints</h3>
            
            <!-- endpoint one -->
            <p class="text-xs text-gray-600 font-light md:text-base">All endpoints listed below can be hit via HTTP or HTTPS.</p>
            <ul class="pl-5 my-5 flex flex-col gap-3 list-inside text-xs text-gray-600 md:text-base">
                <li v-for="data in data.endpointOne" :key="data.id" class="flex items-center gap-2">
                    <p class="font-bold">{{data.method}}</p>
                    <p class="font-light">{{data.endpoint}}</p>
                </li>
            </ul>
            <!-- endpoint one -->

            <!-- endpoint two -->
            <p class="py-2 text-xs text-gray-600 font-light md:text-base">The following endpoints requires a creators account.</p>
            <ul class="pl-5 my-2 flex flex-col gap-3 list-inside text-xs text-gray-600 md:text-base">
                <li v-for="data in data.endpointTwo" :key="data.id" class="flex items-center gap-2">
                    <span class="font-bold">{{data.method}}</span>
                    <span class="font-light">{{data.endpoint}}</span>
                </li>
            </ul>
            <!-- endpoint two -->

            <p class="py-2 text-xs text-gray-600 font-light md:text-base">
                <b>NOTE:</b> A creator account gives you the ability to create your own open user application which you can
                then use to create users belonging to you under that specific application, this users can however be
                retrieved by all other request to the
                <a href="https://api.openuserdata.xyz/api/v1/users/" target="_blank" class="text-blue-500 hover:text-blue-600 visited:text-yellow-500">/users/</a>
                endpoint in read only mode by both creators and non creators. Requests to creators endpoint do not require application authentication,
                all you need is to query one of the aforementioned endpoints passing in your creator’s id (cid) and
                application name (app_name). This details can be found on the specific app details dashboard.
            </p>

            <!-- endpoint three -->
            <p class="py-2 text-xs text-gray-600 font-light md:text-base">The following endpoints are for authenticating a user.</p>
            <ul class="pl-5 my-2 flex flex-col gap-3 list-inside text-xs text-gray-600 md:text-base">
                <li v-for="data in data.endpointThree" :key="data.id" class="flex items-center gap-2">
                    <p class="font-bold">{{data.method}}</p>
                    <p class="font-light">{{data.endpoint}}</p>
                </li>
            </ul>
            <!-- endpoint three -->
        </div>

    </main>
</template>