<script setup>
/* eslint-disable */
import { useAppStore } from '../stores/apps';
import AppMyApp from './AppMyApp.vue';

// store
const appStore = useAppStore()
</script>

<template>
    <main class="w-11/12 mx-auto bg-transparent sm:w-8/12 lg:w-6/12 xl:w-5/12">
        <AppMyApp v-bind="appStore.appInView" />
    </main>
</template>