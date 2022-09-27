<script setup>
/* eslint-disable */
import { computed, onMounted, ref } from 'vue';
import AppInputField from './AppInputField.vue';
import AppTextArea from './AppTextArea.vue';
import AppButton from './AppButton.vue';

// emit
const emit = defineEmits(["button-clicked"])

// refs
const appName = ref("")
const appDes = ref("")
const error = ref(null)

// methods
const saveData = () => {
    if (verifyMinValue.value && verifyMaxValue.value && appNameIsValid.value) {
        error.value = null
        localStorage.setItem('app_create_name', appName.value)
        localStorage.setItem('app_create_description', appDes.value)
        emit("button-clicked", "next")
    }
    else error.value = "Please correct the error causing fields"
}

// computed
const verifyMinValue = computed(() => {
    return appName.value.length >= 4 ? true:false
})

const verifyMaxValue = computed(() => {
    return appName.value.length <= 20 ? true:false
})

const appNameIsValid = computed(() => {
    const re = /^[a-zA-Z]([a-zA-Z0-9 ]*[a-zA-Z])?$/
    const valid = re.exec(appName.value)

    return valid ? true:false
})

// hooks
onMounted(() => {
    appName.value = localStorage.getItem('app_create_name')
    appDes.value = localStorage.getItem('app_create_description')
})
</script>

<template>
    <main class="w-11/12 mx-auto bg-transparent sm:w-8/12 lg:w-6/12 xl:w-5/12">

        <p class="text-xs text-gray-600 font-medium mb-4 md:text-sm">Apps are where you create your users, the app name will be part of your api url </p>
        
        <form @submit.prevent="saveData()" class="flex flex-col gap-5">
            <div class="w-full flex flex-col gap-1">
                <p v-if="error" class="text-xs text-red-500 font-medium mb-4">{{error}}</p>
                <AppInputField v-model.lower="appName" label="App name..." :minLen="4" :maxLen="20" class="bg-white"/>
                <div class="flex items-center justify-between">
                    <p :class="appNameIsValid ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Most begin and end with a letter</p>
                    <p :class="verifyMinValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Min: 4</p>
                    <p :class="verifyMaxValue ? 'text-green-400':'text-red-400'" class="text-xs font-normal">-Max: 20</p>
                </div>
            </div>

            <div class="w-full flex flex-col gap-1">
                <AppTextArea v-model="appDes" label="App description..." :cols="30" :rows="5" :maxLen="255" class="bg-white" />
                <p class="self-end text-xs text-gray-300 font-normal md:text-sm">Max: 255</p>
            </div>

            <div class="flex items-center justify-center gap-2">
                <AppButton
                    type="submit"
                    label="Next"
                    class="text-white bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300" />
            </div>
        </form>

    </main>
</template>