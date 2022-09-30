/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";
import VueCookies from "vue-cookies";

export const useAppStore = defineStore("apps", () => {

  // stores
  const authStore = useAuthStore()
  const deleteApp = ref(false)
  const appName = ref("my-app-name")


  //////////////////////////////////////////////
  // Retrieve all users apps
  //////////////////////////////////////////////
  const myApps = reactive({
    loading: false,
    data: JSON.parse(localStorage.getItem("user_apps")),
    error: null
  })

  async function getMyApps() {
    myApps.loading = true
    myApps.error = null

    await axios.get("api/v1/creators/me/apps/", {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        myApps.loading = false
        myApps.error = null
        // save to localStorage
        localStorage.setItem("user_apps", JSON.stringify(resp.data))
        myApps.data = resp.data

      })
      .catch((err) => {
        myApps.loading = false

        if (err.response) {
          if (err.response.status == 401) {
            authStore.submitSignOut()

            // update notify
            authStore.notify.open = true
            authStore.notify.detail = "Token expired, please relog in"
            authStore.notify.state = "error"

            setTimeout(() => {
              authStore.notify.open = false
              authStore.notify.detail = authStore.notify.state = null
            }, 5000)
          }
          else myApps.error = "An error occured, please try agan later"
        }
      })
  }

  //////////////////////////////////////////////
  // App in focus
  //////////////////////////////////////////////
  const appInView = ref(JSON.parse(localStorage.getItem("app_in_view")))

  return { deleteApp, myApps, getMyApps, appInView };

});
