/* eslint-disable */
import { reactive, ref } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import { useUserStore } from "./user";
import axios from "axios";
import VueCookies from 'vue-cookies';


export const useAuthStore = defineStore("auth", () => {
  // router
  const router = useRouter()
  
  const isAuthenticated = ref(JSON.parse(localStorage.getItem("is_auth")))

  ////////////////////////////////////////////
  // social authentication functionality
  ///////////////////////////////////////////
  const social = ref(localStorage.getItem('auth_social'));
  function setSocial(value) {
    social.value = value
    localStorage.setItem('auth_social', value)
  }

  ////////////////////////////////////////////
  // sign up functionalitiy
  ////////////////////////////////////////////
  const signUp = reactive({loading: false, username: null, email: null, error: null})

  async function submitSignUp(data) {
    signUp.loading = true
    signUp.username = signUp.email = signUp.error = null

    await axios.post("api/v1/creators/new/", data)
      .then((resp) => {
        signUp.loading = false
        signUp.username = signUp.email = signUp.error = null

        // set cookies
        VueCookies.set("access", resp.data['tokens']['access'], "12h")
        VueCookies.set("refresh", resp.data['tokens']['refresh'], "1d")

        // save user data in localStorage
        userProfile.value = resp.data['user']
        localStorage.setItem("user_profile", JSON.stringify(resp.data['user']))
        localStorage.setItem("is_auth", JSON.stringify(true))
        isAuthenticated.value = true

        // navigate to dashboard
        router.push({name :'dashboard', params: {username: resp.data['user']['username']}})
      })
      .catch((err) => {
        if (err.response) {
          signUp.loading = isAuthenticated.value = false
          'username' in err.response.data ? signUp.username = err.response.data['username'][0]:''
          'email' in err.response.data ? signUp.email = err.response.data['email'][0]:''
        }
        else {
          signUp.error = "An error occured, please try again."
          signUp.loading = isAuthenticated.value = false
        }
      })
  }

  ////////////////////////////////////////////
  // sign in functionality
  ////////////////////////////////////////////
  const signIn = reactive({loading: false, username: null, password: null, error: null})

  async function submitSignIn(data) {
    signIn.loading = true
    signIn.username = signIn.password = signIn.error = null

    // await axios.post("api/v1/creators/new/", data, {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
    await axios.post("api/v1/auth/login/token/", data)
      .then((resp) => {
        signIn.loading = false
        signIn.username = signIn.password = signIn.error = null

        // set auth cookies
        VueCookies.set("access", resp.data['access'], "12h")
        VueCookies.set("refresh", resp.data['refresh'], "1d")

        // set localStorage
        data['rememberMe'] ? localStorage.setItem("remember_me", data['username']) :
        localStorage.removeItem("remember_me")
        localStorage.setItem("is_auth", JSON.stringify(true))

        // get the authenticated users profile
        getUserProfile()
        isAuthenticated.value = true
      })
      .catch((err) => {
        if (err.response) {
          signIn.loading = isAuthenticated.value = false
          'username' in err.response.data ? signIn.username = err.response.data['username'][0]:''
          'password' in err.response.data ? signIn.password = err.response.data['password'][0]:''
          'detail' in err.response.data ? signIn.error = 'Wrong username or password provided':''
          console.log(err.response.data)
        }
        else {
          signIn.loading = isAuthenticated.value = false
          signIn.error = "An error occured, please try again."
          console.log(err.message)
        }
      })
  }

  ////////////////////////////////////////////
  // user profiles functionality
  ////////////////////////////////////////////
  const userProfile = ref(JSON.parse(localStorage.getItem("user_profile")))
  const getUser = reactive({loading: false, error: null})

  async function getUserProfile() {
    getUser.loading = true
    getUser.error = null

    await axios.get("api/v1/creators/me/", {headers: {'Authorization': `Bearer ${VueCookies.get('access')}` }})
      .then((resp) => {
        getUser.loading = false
        getUser.error = null
        userProfile.value = resp.data
        localStorage.setItem("user_profile", JSON.stringify(resp.data))

        // navigate to users dashboard
        router.push({name: 'dashboard', params: {username: resp.data['username']}})
      })
      .catch((err) => {
        if (err.response) {
          getUser.loading = false
          err.response.status == 401 ? getUser.error = 'Token expired, please relog in':'Connection error'
          submitSignOut()
        }
        else {
          getUser.error = "An error occured, please try again."
          getUser.loading = false
        }
      })
  }

  ////////////////////////////////////////////
  // sign out functionality
  ////////////////////////////////////////////
  const signOut = ref(false)

  function submitSignOut() {
    // close signOut modal
    signOut.value = false

    // clear localStorage data
    localStorage.removeItem("user_profile")
    localStorage.setItem("is_auth", JSON.stringify(false))
    isAuthenticated.value = false
    
    // clear cookies data also
    VueCookies.remove("access")
    VueCookies.remove("refresh")
    
    // navigate to home page
    router.push({name: 'home'})
  }

  return {
    isAuthenticated, social, setSocial, signUp, submitSignUp,
    signIn, submitSignIn, getUser, userProfile, getUserProfile,
    signOut, submitSignOut
  };
});
