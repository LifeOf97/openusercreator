/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import { useRouter } from "vue-router";
import axios from "axios";
import VueCookies from "vue-cookies";

export const useUserStore = defineStore("user", () => {
  const deleteAccount = ref(false);
  const username = ref('RealestKMA');

  return {
    deleteAccount, username,
    
  };
});
