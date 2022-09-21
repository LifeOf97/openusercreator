<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconCheckAllSolid from './icons/IconCheckAllSolid.vue';
import IconUserPlusSolid from './icons/IconUserPlusSolid.vue';
import IconUserMinusSolid from './icons/IconUserMinusSolid.vue';
import IconLinkSolid from './icons/IconLinkSolid.vue';

// data
const data = {
    crud: [
        {
            id: 1,
            title: "Create",
            detail: `
                With open user data, creators can create new user accounts under
                an application through your creator’s dashboard or creator API endpoint.
            `
        },
        {
            id: 2,
            title: "Read",
            detail: `
                You can retrieve a particular user data by their username, a refined list of
                users in a paginated form and also query for certain users by related first
                name, last name, other name and date of birth.
            `
        },
        {
            id: 3,
            title: "Update",
            detail: `
                User data can be updated via it’s creator endpoint. To update a user data the
                user has to be authenticated either via token authentication or session authentication.
            `
        },
        {
            id: 4,
            title: "Delete",
            detail: `
                You can also delete a user permanently from the system through it’s creator endoint.
                Note the only way to delete a  user is to make an authenticated request to the delete
                usrer creators endpoint.
            `
        },
    ],
}
</script>

<template>
    <main id="crud" class="relative w-11/12 mx-auto h-full flex flex-col gap-5 bg-white py-20 border-b border-gray-100 lg:w-10/12">

        <!-- this tag is only visible on small screens -->
        <RouterLink to="#crud" class="inline-flex items-center gap-2 md:hidden">
            <IconLinkSolid class="w-5 h-5 fill-gray-400" />
            <p class="px-4 py-2 bg-red-500 rounded-full text-xs text-white font-semibold">CRUD</p>
        </RouterLink>
        <!-- this tag is only visible on small screens -->

        <div class="grid grid-cols-1 content-center items-center gap-10 md:grid-cols-2">

            <!-- crud text and table -->
            <div class="flex flex-col gap-7">
                
                <div class="w-full flex flex-col gap-3">
                    <h3 class="text-xl font-semibold text-gray-900 md:text-3xl">Create, Read, Update & Delete</h3>
                    <p class="text-xs text-gray-600 font-light md:text-sm">
                        Open user data provides full CRUD operations over REST API.
                        You can create new users, retrieve one or more user data,
                        update the data of a user instance and also delete users
                        permanently from the systtem.
                    </p>
                </div>

                <table class="table-fixed rounded-md overflow-hidden text-sm text-left">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="border p-2 text-gray-500 font-light">Action</th>
                            <th class="border p-2 text-gray-500 font-light">HTTP Verb</th>
                            <th class="border p-2 text-gray-500 font-light">DB Operation</th>
                        </tr>
                    </thead>
                    <tbody class="bg-white">
                        <tr>
                            <td class="border p-2 text-gray-500 font-light">Create</td>
                            <td class="border p-2 text-gray-500 font-light">POST</td>
                            <td class="border p-2 text-gray-500 font-light">Insert</td>
                        </tr>
                        <tr>
                            <td class="border p-2 text-gray-500 font-light">Read/Retrieve</td>
                            <td class="border p-2 text-gray-500 font-light">GET</td>
                            <td class="border p-2 text-gray-500 font-light">Select</td>
                        </tr>
                        <tr>
                            <td class="border p-2 text-gray-500 font-light">Update</td>
                            <td class="border p-2 text-gray-500 font-light">PUT/PATCH</td>
                            <td class="border p-2 text-gray-500 font-light">Update</td>
                        </tr>
                        <tr>
                            <td class="border p-2 text-gray-500 font-light">Delete</td>
                            <td class="border p-2 text-gray-500 font-light">DELETE</td>
                            <td class="border p-2 text-gray-500 font-light">Delete</td>
                        </tr>
                    </tbody>
                </table>

            </div>
            <!-- crud text and table -->

            <div class="h-full grid grid-cols-2 items-start content-center">
                <div class="justify-self-end bg-cyan-400 p-5 rounded-md">
                    <IconUserPlusSolid class="w-20 h-20 fill-white md:w-32 md:h-32 lg:w-40 lg:h-40" />
                </div>
                <div class="justify-self-start bg-purple-500 p-5 rounded-md col-start-2 row-start-2">
                    <IconUserMinusSolid class="w-20 h-20 fill-white md:w-32 md:h-32 lg:w-40 lg:h-40" />
                </div>
            </div>
            
        </div>
        
        <div class="grid grid-cols-1 gap-10 mt-10 sm:grid-cols-2 lg:grid-cols-4">
            <div v-for="data in data.crud" :key="data.id" class="flex flex-col gap-3">
                <div class="flex items-center gap-5">
                    <div class="p-1 rounded-full bg-gray-100 shadow-inner shadow-gray-400">
                        <IconCheckAllSolid class="w-7 h-7 fill-gray-600" />
                    </div>
                    <h3 class="text-lg text-gray-600 font-semibold">{{data.title}}</h3>
                </div>

                <div>
                    <p class="text-gray-600 text-xs font-light md:text-sm">{{data.detail}}</p>
                </div>
            
            </div>
        </div>

    </main>
</template>