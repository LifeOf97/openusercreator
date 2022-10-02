/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import { useRouter } from "vue-router";
import axios from "axios";
import VueCookies from "vue-cookies";


export const useUserStore = defineStore("user", () => {

  // stores
  const authStore = useAuthStore()

  // routers
  const router = useRouter()

  ////////////////////////////////////////////////////////////
  // update user account functionality
  ////////////////////////////////////////////////////////////
  const updateUser = reactive({
    loading: false,
    username: null,
    email: null,
    error: null
  })

  async function submitUpdateUser(data) {
    updateUser.loading = true
    updateUser.username = updateUser.email = updateUser.error = null

    await axios.put("api/v1/creators/me/update/", data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        updateUser.loading = false
        updateUser.username = updateUser.email = updateUser.error = null
        
        // update localStorage
        authStore.userProfile = resp.data
        localStorage.setItem("user_profile", JSON.stringify(resp.data))

        // navigate to user dashboard with new user data
        router.push({name: 'dashboard', params: {username: resp.data['username']}})

        // show notify
        authStore.notify.open = true
        authStore.notify.detail = "Profile updated successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        if (err.response) {
          updateUser.loading = false
          'username' in err.response.data ? updateUser.username = err.response.data['username'][0]:''
          'email' in err.response.data ? updateUser.email = err.response.data['email'][0]:''
          
          if (err.response.status == 401) {
            authStore.submitSignOut()
            
            // clear errors
            updateUser.username = updateUser.email = updateUser.error = null
            
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
        else {
          updateUser.loading = false
          updateUser.error = "An error occured, please try again."
        }
      })
  }


  ////////////////////////////////////////////////////////////
  // update user password functionality
  ////////////////////////////////////////////////////////////
  const updatePassword = reactive({
    loading: false,
    oldPassword: null,
    password1: null,
    password2: null,
    error: null
  })

  async function submitUpdatePassword(data) {
    updatePassword.loading = true
    updatePassword.oldPassword = updatePassword.password1 = updatePassword.password2 = updatePassword.error = null

    await axios.post("api/v1/creators/me/password/change/", data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        updatePassword.loading = false
        updatePassword.oldPassword = updatePassword.password1 = updatePassword.password2 = updatePassword.error = null
        
        // navigate to user dashboard
        router.push({name: 'dashboard', params: {username: authStore.userProfile['username']}})

        // show notify
        authStore.notify.open = true
        authStore.notify.detail = resp.data['detail']
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        if (err.response) {
          updatePassword.loading = false
          'old_password' in err.response.data ? updatePassword.oldPassword = err.response.data['old_password'][0]:''
          'new_password1' in err.response.data ? updatePassword.password1 = err.response.data['new_password1'][0]:''
          'new_password2' in err.response.data ? updatePassword.password2 = err.response.data['new_password2'][0]:''
          
          if (err.response.status == 401) {
            authStore.submitSignOut()
            
            // clear errors
            updatePassword.oldPassword = updatePassword.password1 = updatePassword.password2 = updatePassword.error = null
            
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
        else {
          updatePassword.loading = false
          updatePassword.error = "An error occured, please try again."
        }
      })
  }

  ////////////////////////////////////////////////////////////
  // delete user account functionality
  ////////////////////////////////////////////////////////////
  const deleteAccount = ref(false);

  async function submitDeleteAccount() {
    await axios.delete("api/v1/creators/me/delete/", {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then(() => {
        // close delete account modal
        deleteAccount.value = false

        // sign out the user
        authStore.submitSignOut()

        // clear remember me sign state
        localStorage.removeItem("remember_me")

        // show notify
        authStore.notify.open = true
        authStore.notify.detail = "Account deleted successfully"
        authStore.notify.state = "good"

        setTimeout(() => {
          authStore.notify.open = false
          authStore.notify.detail = authStore.notify.state = null
        }, 5000);
      })
      .catch((err) => {
        deleteAccount.value = false
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
    deleteAccount, submitDeleteAccount, updateUser,
    submitUpdateUser, updatePassword, submitUpdatePassword
  };
});
