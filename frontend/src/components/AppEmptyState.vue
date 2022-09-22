<script setup>
/* eslint-disable */
import IconPlusSolid from './icons/IconPlusSolid.vue';
import AppButton from './AppButton.vue';
</script>

<template>
    <main class="w-full h-full flex flex-col items-center justify-center bg-transparent p-4 gap-2 border-2 border-dashed rounded-lg">

        <slot name="head">
            <p class="text-xs text-gray-500 font-medium md:text-sm">Empty State</p>
        </slot>

        <slot name="body">
            <p class="text-xs text-gray-500 font-light md:text-sm">more details about the empty state</p>
        </slot>

        <slot name="tail">
            <AppButton label="Action" class="bg-blue-500 hover:bg-blue-600">
                <template #icon>
                    <IconPlusSolid class="w-5 h-5 fill-white" />
                </template>
            </AppButton>
        </slot>

    </main>
</template>