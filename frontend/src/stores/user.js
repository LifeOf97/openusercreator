/* eslint-disable */
import { ref } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", () => {
  const deleteAccount = ref(false);

  return { deleteAccount };
});
