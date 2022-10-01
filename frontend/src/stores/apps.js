/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";
import { useStorage } from "@vueuse/core";
import VueCookies from "vue-cookies";
import { useRouter } from "vue-router";

export const useAppStore = defineStore("apps", () => {

  // router
  const router = useRouter()

  // stores
  const authStore = useAuthStore()
  const deleteApp = ref(false)

  //////////////////////////////////////////////
  // Retrieve all users apps
  //////////////////////////////////////////////
  const myApps = reactive({
    loading: false,
    data: useStorage("user_apps", {}),
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

            // show notify
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
  // App currently in view
  //////////////////////////////////////////////
  const appInView = useStorage("app_in_view", {})


  //////////////////////////////////////////////
  // Update app details
  //////////////////////////////////////////////
  const updateAppDetails = reactive({loading: false, error: null})
  const updateAppProfiles = reactive({loading: false, error: null})
  const updateAppPassword = reactive({loading: false, error: null})

  async function submitUpdateApp(data) {
    'name' in data ? updateAppDetails.loading = true:''
    'description' in data ? updateAppDetails.loading = true:''
    'profiles' in data ? updateAppProfiles.loading = true:''
    'profile_password' in data ? updateAppPassword.loading = true:''

    // clear errors
    updateAppDetails.error = updateAppProfiles.error = updateAppPassword.error = null

    await axios.put(`api/v1/creators/me/apps/${appInView.value['name']}/update/`, data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        updateAppDetails.loading = false
        updateAppProfiles.loading = false
        updateAppPassword.loading = false

        // clear errors
        updateAppDetails.error = updateAppProfiles.error = updateAppPassword.error = null

        // update data and localStorage
        appInView = resp.data
        localStorage.setItem("app_in_view", JSON.stringify(resp.data))

        // navigate to app view
        router.push({name: 'dashboardapp', params: {appName: resp.data['name']}})

        // show notify
        authStore.notify.open = true
        authStore.notify.detail = "App details updated successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        updateAppDetails.loading = false
        updateAppProfiles.loading = false
        updateAppPassword.loading = false

        if (err.response) {
          if (err.response.status == 400) {
            'name' in err.response.data ? updateAppDetails.error = err.response.data['name'][0]:''
            'error' in err.response.data ? updateAppDetails.error = err.response.data['error'][0]:''
            'profiles' in err.response.data ? updateAppProfiles.error = err.response.data['profiles'][0]:''
            'profile_password' in err.response.data ? updateAppPassword.error = err.response.data['profile_password'][0]:''
          }
          else if (err.response.status == 401) {
            // auth token expired
            authStore.submitSignOut()
            
            // show notify
            authStore.notify.open = true
            authStore.notify.detail = "Token expired, please relog in"
            authStore.notify.state = "error"

            setTimeout(() => {
              authStore.notify.open = false
              authStore.notify.detail = authStore.notify.state = null
            }, 5000);
          }
          else updateApp.error = "An error occured, please try again later."
        }
      })
  }

  return {
    deleteApp, myApps, getMyApps, appInView,
    updateAppDetails, updateAppProfiles, updateAppPassword,
    submitUpdateApp
  };

});
