<script setup>
/* eslint-disable */
import IconExclamationTraingleOutline from './icons/IconExclamationTraingleOutline.vue';
</script>

<template>
    <main class="w-full h-full flex items-center justify-center bg-transparent overflow-auto">

        <span class="w-11/12 mx-auto flex flex-col sm:w-9/12 md:w-8/12 lg:w-5/12 xl:w-4/12">

            <div class="bg-white rounded-lg overflow-hidden shadow-lg shadow-gray-400">

                <div class="flex gap-4 py-6 px-4 md:p-6">

                    <!-- modal icon -->
                    <span class="self-start bg-red-100 p-2 rounded-full">
                        <slot name="icon">
                            <IconExclamationTraingleOutline class="w-4 h-4 stroke-red-600 md:w-7 md:h-7" />
                        </slot>
                    </span>
                    <!-- modal icon -->

                    <!-- modal content -->
                    <span class="flex flex-col gap-3">

                        <!-- modal title -->
                        <h3 class="text-lg text-gray-600 font-bold md:text-xl">
                            <slot name="title">Title of Modal</slot>
                        </h3>
                        <!-- modal title -->

                        <!-- modal detail -->
                        <p class="text-xs text-gray-500 font-normal leading-4 md:text-sm">
                            <slot name="details">
                                Details about this modal
                            </slot>
                        </p>
                        <!-- modal detail -->

                        <!-- modal form -->
                        <span class="mt-4">
                            <slot name="form"></slot>
                        </span>
                        <!-- modal form -->

                    </span>
                    <!-- modal icon -->

                </div>

                <div class="w-full flex items-center justify-end gap-4 px-4 py-2 bg-gray-50">
                    <slot name="actions"></slot>
                </div>

            </div>
        </span>
    </main>
</template>