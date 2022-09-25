/* eslint-disable */
import { ref } from "vue";
import { defineStore } from "pinia";

export const useAppStore = defineStore("apps", () => {
  const deleteApp = ref(false)
  const appName = ref("my-app-name")

  return { deleteApp, appName };
});
