/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";
import VueCookies from "vue-cookies";

export const useUserStore = defineStore("user", () => {

  // stores
  const authStore = useAuthStore()

  ////////////////////////////////////////////////////////////
  // update user account functionality
  ////////////////////////////////////////////////////////////
  const updateUser = reactive({loading: false, username: null, email: null, error: null})

  async function submitUpdateUser(data) {
    updateUser.loading = true
    updateUser.username = updateUser.email = updateUser.error = null

    await axios.put("api/v1/creators/me/update/", data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        updateUser.loading = true
        updateUser.username = updateUser.email = updateUser.error = null
        
        // update localStorage
        authStore.userProfile = resp.data
        localStorage.setItem("user_profile", JSON.stringify(resp.data))

        // update notify
        authStore.notify.open = true
        authStore.notify.detail = "Profile deleted successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
  }

  ////////////////////////////////////////////////////////////
  // delete authenticated user account functionality
  ////////////////////////////////////////////////////////////
  const deleteAccount = ref(false);

  async function submitDeleteAccount() {
    await axios.delete("api/v1/creators/me/delete/", {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        // close delete account modal
        deleteAccount.value = false

        // sign out the user
        authStore.submitSignOut()

        // clear remember me sign state
        localStorage.removeItem("remember_me")

        // update notify
        authStore.notify.open = true
        authStore.notify.detail = "Account deleted successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        if (err.response) console.log("Response Error: ", err.response.data)
        if (err.request) console.log("Request Error: ", err.request.data)
        else console.log("Error: ", err.message)
      })
  }

  return {
    deleteAccount, submitDeleteAccount
  };
});
