<script setup>
/* eslint-disable */
import { onMounted, ref, computed } from 'vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

// emits
const emit = defineEmits(["button-clicked"])

// refs
const appProfiles = ref(5)
const error = ref(null)

// data
const appName = localStorage.getItem("app_create_name")

// methods
const saveData = () => {
    if (verifyMinValue.value && verifyMaxValue.value) {
        error.value = null
        localStorage.setItem('app_create_profiles', appProfiles.value)
        emit("button-clicked", "next")
    }
    else error.value = "Please correct the error causing fields"
}

// computed
const verifyMinValue = computed(() => {
    return appProfiles.value >= 5 ? true:false
})

const verifyMaxValue = computed(() => {
    return appProfiles.value <= 50 ? true:false
})

// hooks
onMounted(() => {
    appProfiles.value = localStorage.getItem('app_create_profiles')
})
</script>
    
<template>
    <main class="w-11/12 mx-auto bg-transparent sm:w-8/12 lg:w-6/12 xl:w-5/12">

        <p class="text-xs text-gray-600 font-medium mb-4 md:text-sm">
            The number of user profiles you will like the system to automatically create under the (<b>{{appName}}</b>) app.
        </p>

        <form @submit.prevent="saveData()" class="flex flex-col gap-5">
            <div class="w-full flex flex-col gap-1">
                <p v-if="error" class="text-xs text-red-500 font-medium mb-4">{{error}}</p>
                
                <AppInputField v-model="appProfiles" label="5" type="number" :minLen="5" :maxLen="50" class="bg-white" />
                <div class="flex items-center justify-between">
                    <p :class="verifyMinValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Min: 5</p>
                    <p :class="verifyMaxValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Max: 50</p>
                </div>
            </div>

            <div class="flex items-center justify-center gap-2">
                <AppButton @click.prevent="$emit('button-clicked', 'back')" type="button" label="Back" class="text-gray-900 bg-transparent hover:bg-white disabled:bg-gray-300" />
                <AppButton type="submit" label="Next" class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </div>
        </form>

    </main>
</template>