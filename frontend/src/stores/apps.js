/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";
import VueCookies from "vue-cookies";
import { useRouter } from "vue-router";

export const useAppStore = defineStore("apps", () => {

  // router
  const router = useRouter()

  // stores
  const authStore = useAuthStore()


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
  // Create a new apps
  //////////////////////////////////////////////
  const createApp = reactive({loading: false, success: false, error: null})

  async function submitCreateApp(data) {
    createApp.loading = true
    createApp.success = false
    createApp.error = null

    await axios.post("api/v1/creators/me/apps/new/", data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        createApp.loading = false
        createApp.success = true
        createApp.error = null

        // update apps list and localStorage, to avoid making a get request for the list of app        
        const data = [...myApps.data, resp.data]
        localStorage.setItem("user_apps", JSON.stringify(data))

        // set current app in view
        appInView.value = resp.data
        myApps.data = data
        localStorage.setItem("app_in_view", JSON.stringify(resp.data))

        // clear create app localstorage
        localStorage.removeItem("app_create_name")
        localStorage.removeItem("app_create_description")
        localStorage.removeItem("app_create_profiles")
        localStorage.removeItem("app_create_password")
      })
      .catch((err) => {
        createApp.loading = createApp.success = false

        if (err.response) {
          if (err.response.status == 400) {
            'name' in err.response.data ? createApp.error = err.response.data['name'][0]:''
            'error' in err.response.data ? createApp.error = err.response.data['error'][0]:''
            'profiles' in err.response.data ? createApp.error = err.response.data['profiles'][0]:''
            'profile_password' in err.response.data ? createApp.error = err.response.data['profile_password'][0]:''
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
          else createApp.error = 'An error occured, please try again later.'
        }
      })
  }

  //////////////////////////////////////////////
  // App currently in view
  //////////////////////////////////////////////
  const appInView = ref(JSON.parse(localStorage.getItem("app_in_view")))


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

        // get all apps, update app in view and localStorage
        appInView.value = resp.data
        localStorage.setItem("app_in_view", JSON.stringify(resp.data))
        getMyApps()

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
          else {
            'name' in data ? updateAppDetails.error = 'An error occured, please try again later.':''
            'description' in data ? updateAppDetails.error = 'An error occured, please try again later.':''
            'profiles' in data ? updateAppProfiles.error = 'An error occured, please try again later.':''
            'profile_password' in data ? updateAppPassword.error = 'An error occured, please try again later.':''
        
          }
        }
      })
  }


  ////////////////////////////////////////////////////////////
  // delete app functionality
  ////////////////////////////////////////////////////////////
  const deleteApp = ref(false);

  async function submitDeleteApp() {
    await axios.delete(`api/v1/creators/me/apps/${appInView.value['name']}/delete/`, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        // close delete account modal
        deleteApp.value = false

        // clear remember me sign state
        localStorage.removeItem("app_in_view")

        // refresh apps
        getMyApps()

        // navigate to user dashboard
        router.push({name: 'dashboarduser', params: {username: authStore.userProfile['username']}})

        // show notify
        authStore.notify.open = true
        authStore.notify.detail = "App deleted successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        deleteApp.value = false
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
            }, 5000);
          }
        } 
        else console.log("Error: ", err.message)
      })
  }


  return {
    deleteApp, myApps, getMyApps, appInView,
    updateAppDetails, updateAppProfiles, updateAppPassword,
    submitUpdateApp, deleteApp, submitDeleteApp, createApp,
    submitCreateApp
  };

});
