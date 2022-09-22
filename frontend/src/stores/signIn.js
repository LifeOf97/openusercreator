/* eslint-disable */
import { ref } from "vue";
import { defineStore } from "pinia";

export const useSignInStore = defineStore("signin", () => {
  const social = ref(localStorage.getItem('oud_signup_social_name'));
  function setSocial(value) {
    social.value = value
    localStorage.setItem('oud_signup_social_name', value)
  }

  return { social, setSocial };
});
