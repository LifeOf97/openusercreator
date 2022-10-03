<script setup>
/* eslint-disable */
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import IconCubeOutline from './icons/IconCubeOutline.vue';
import IconArrowLongLeft from './icons/IconArrowLongLeft.vue';
import IconCheckCircleSolid from './icons/IconCheckCircleSolid.vue';
import AppDashboardAppForm1 from './AppDashboardAppForm1.vue';
import AppDashboardAppForm2 from './AppDashboardAppForm2.vue';
import AppDashboardAppForm3 from './AppDashboardAppForm3.vue';
import AppDashboardAppCreateConfirm from './AppDashboardAppCreateConfirm.vue';
import AppDashboardAppCreateSuccess from './AppDashboardAppCreateSuccess.vue';
import { useAppStore } from '../stores/apps';
import { useTitle } from '@vueuse/core';

// router
const router = useRouter()

// stores
const appStore = useAppStore()

// refs
const currentTabId = ref(1)
const tabTransition = ref("slide-left")

const formTabs = [
    {id: 1, title: "Name your App", tab: AppDashboardAppForm1},
    {id: 2, title: "Number of Users", tab: AppDashboardAppForm2},
    {id: 3, title: "Users Password", tab: AppDashboardAppForm3},
    {id: 4, title: "Confirm App Details", tab: AppDashboardAppCreateConfirm},
    {id: 5, title: "Application Created Successfully", tab: AppDashboardAppCreateSuccess},
]

// computed
const currentTab = computed(() => {
    return formTabs.find((tab) => tab.id == currentTabId.value)
})

// methods
const updateTab = (value) => {
    if ((value == 'next') && currentTabId.value < 5) {
        tabTransition.value = "slide-left"
        currentTabId.value = currentTabId.value + 1
    }
    else if (value == 'back' && currentTabId.value > 1) {
        tabTransition.value = "slide-right"
        currentTabId.value = currentTabId.value - 1
    }
}

// hooks
onMounted(() => {
    useTitle("Create App | Open User Data")
})
</script>
    
<template>
    <main class="w-full mx-auto h-full">

        <!-- dashboard header -->
        <div class="relative w-full bg-white pt-48 pb-14 overflow-hidden">
            <div class="w-11/12 mx-auto md:w-10/12">
                <h3 class="text-3xl text-gray-600 font-bold md:text-4xl">Create App</h3>
            </div>
            <IconCubeOutline class="hidden absolute -top-7 right-0 w-86 h-96 stroke-gray-50 md:block" :strokeWidth="0.2" />
        </div>
        <!-- dashboard header -->

        <div class="w-full h-full bg-gray-50 py-10">
            
            <div class="w-11/12 mx-auto flex flex-col gap-16 md:w-10/12">

                <!-- back link -->
                <span class="w-full flex items-center justify-start">
                    <button type="button" @click.prevent="router.back()" class="group flex items-center gap-2">
                        <IconArrowLongLeft class="w-7 h-7 fill-gray-500 transition-all duration-300 group-hover:animate-bounce-hor group-hover:fill-gray-900" />
                        <p class="text-xs text-gray-500 font-medium transition-all duration-300 group-hover:text-blue-500 sm:text-sm">Back</p>
                    </button>
                </span>
                <!-- back link -->

                <div class="flex flex-col gap-10">

                    <span class="flex flex-col items-center gap-5 md:gap-10">
                        <h3 class="text-xl text-gray-900 font-semibold md:text-4xl">{{currentTab.title}}</h3>

                        <span class="flex items-center -space-x-1">
                            <IconCheckCircleSolid :class="currentTabId > 1 ? 'fill-blue-500':'fill-gray-200'" class="w-9 h-9 transition-all duration-700 md:w-12 md:h-12"/>
                            <div :class="currentTabId > 1 ? 'border-blue-500':'border-gray-200'" class="w-10 border-b transition-all duration-700 sm:w-20"></div>
                            <IconCheckCircleSolid :class="currentTabId > 2 ? 'fill-blue-500':'fill-gray-200'" class="w-9 h-9 transition-all duration-700 md:w-12 md:h-12"/>
                            <div :class="currentTabId > 2 ? 'border-blue-500':'border-gray-200'" class="w-10 border-b transition-all duration-700 sm:w-20"></div>
                            <IconCheckCircleSolid :class="currentTabId > 3 ? 'fill-blue-500':'fill-gray-200'" class="w-9 h-9 transition-all duration-700 md:w-12 md:h-12"/>
                            <div :class="currentTabId > 3 ? 'border-blue-500':'border-gray-200'" class="w-10 border-b transition-all duration-700 sm:w-20"></div>
                            <IconCheckCircleSolid :class="currentTabId > 4 ? 'fill-blue-500':'fill-gray-200'" class="w-9 h-9 transition-all duration-700 md:w-12 md:h-12"/> 
                        </span>
                    </span>

                    <Transition :name="tabTransition" mode="out-in">
                        <Component :is="currentTab.tab" @button-clicked="updateTab"></Component>
                    </Transition>

                </div>

            </div>

        </div>

    </main>
</template>