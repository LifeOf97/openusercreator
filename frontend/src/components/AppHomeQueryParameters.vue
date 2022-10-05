<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconLinkSolid from './icons/IconLinkSolid.vue';

// data
const data = {
    filters: [
        {
            id: 1,
            title: "Data Filtering",
            detail: `
                You can filter based on the following parameters, username, first_name, last_name,
                other_name, gender, dob, dob__year, dob__year__gt and dob__year__lt. And they can
                also be chained to each other using the & ampersand sign. Note, values are case insensitive.
            `,
            method: "GET",
            endpoint: "/users?first_name=john&last_name=doe&dob__year_gt=2000"
        },
        {
            id: 2,
            title: "Data Searching",
            detail: `
                You can search for a specific data passing any of this values to the search parameter. username,
                first_name, last_name and other_name. This values should be an exact match of the user you are
                searching for. Note, values are case insensitive. Open user data uses the keyword "q" for searching.
            `,
            method: "GET",
            endpoint: "/users?q=john"
        },
        {
            id: 3,
            title: "Data Ordering",
            detail: `
                You can specify in what order you want your returned data to be in. The only supported ordering
                values are. username, email and dob. Open user data uses the keyword order as the url param key
                to order data.
            `,
            method: "GET",
            endpoint: "/users?order=john"
        },
    ]
}
</script>

<template>
    <main id="QueryParameters" class="w-11/12 mx-auto h-full flex flex-col gap-5 bg-white py-20 border-b border-gray-100 lg:w-10/12">

        <!-- this tag is only visible on small screens -->
        <RouterLink to="#QueryParameters" class="inline-flex items-center gap-2 md:hidden">
            <IconLinkSolid class="w-5 h-5 fill-gray-400" />
            <p class="px-4 py-2 bg-yellow-400 rounded-full text-xs text-white font-semibold">Query Parameters</p>
        </RouterLink>
        <!-- this tag is only visible on small screens -->

        <div class="flex flex-col gap-10">

            <div class="flex flex-col gap-2">
                <h3 class="text-xl text-gray-900 font-semibold md:text-3xl">URL Parameters</h3>
                <p class="text-xs text-gray-600 font-light md:text-base">
                    Open user data provides the following features that requires url query params.
                </p>
            </div>

            <div class="flex flex-col gap-2">
                <h4 class="text-gray-600 text-lg font-medium md:text-xl">Pagination</h4>
                <p class="text-xs text-gray-600 font-light md:text-sm">
                    Open user data includes support for customizable pagination styles. With these,
                    you can modify how result set are split into pages. Pagination links are provided
                    as part of the content of the response. Open user data uses the LimitOffsetPagination.
                </p>

                <ul class="pl-5 my-5 flex flex-col gap-3 list-inside text-xs text-gray-600 md:text-sm">
                    <li class="flex items-center gap-2">
                        <p class="font-bold">GET</p>
                        <p class="font-light">/users?limit=100&offset=400</p>
                    </li>
                </ul>

                <p class="text-xs text-gray-600 font-light md:text-base">
                    <b>NOTE:</b> The default number of users retrurned is 50, however you can change this to suit your needs.
                </p>
            </div>

            <div class="flex flex-col gap-2">
                <h4 class="text-gray-600 text-lg font-medium md:text-2xl">Filtering</h4>
                <p class="text-xs text-gray-600 font-light md:text-sm">
                    Usually the returned data from any successful request to the backend is the whole object in the database.
                    Sometimes, you'll want to retrieve just a subset of data from the backend.
                    Open user data provides just what you need.
                </p>

                <div class="pl-5 my-5 flex flex-col gap-3 text-xs text-gray-600 md:text-sm">
                   
                    <div v-for="data in data.filters" :key="data.id" class="flex flex-col gap-2">
                        <p class="text-gray-600 text-base font-medium md:text-xl">{{data.title}}</p>
                        <p class="text-xs text-gray-600 font-light md:text-sm">{{data.detail}}</p>
                        <ul class="pl-5 my-5 flex flex-col gap-3 list-inside text-xs text-gray-600 md:text-sm">
                            <li class="flex items-center break-all gap-2">
                                <p class="font-bold">{{data.method}}</p>
                                <p class="font-light">{{data.endpoint}}</p>
                            </li>
                        </ul>
                    </div>

                </div>

            </div>

        </div>

    </main>

</template>