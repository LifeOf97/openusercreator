/* eslint-disable */
import { ref } from "vue";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", () => {
  const social = ref(localStorage.getItem('oud_signup_social_name'));
  function setSocial(value) {
    social.value = value
    localStorage.setItem('oud_signup_social_name', value)
  }

  const signOut = ref(false)

  return { social, setSocial, signOut };
});
