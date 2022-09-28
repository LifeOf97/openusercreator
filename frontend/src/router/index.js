/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";
import DashboardView from "../views/DashboardView.vue";
import { useAuthStore } from "../stores/auth";
import { useUserStore } from "../stores/user";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        title: "Welcome | Open User Data"
      }
    },
    {
      path: "/:username",
      name: "dashboard",
      redirect: {name: 'dashboarduser'},
      component: DashboardView,
      meta: {requiresAuth: true},
      children: [
        {
          path: "",
          name: "dashboarduser",
          component: () =>  import("../components/AppDashboard.vue"),
        },
        {
          path: "settings",
          name: "dashboardusersettings",
          component: () =>  import("../components/AppDashboardSettings.vue"),
        },
        {
          path: "app",
          name: "dashboardapp",
          component: () =>  import("../components/AppDashboardApp.vue"),
        },
        {
          path: "app/create",
          name: "dashboardappcreate",
          component: () =>  import("../components/AppDashboardAppCreate.vue"),
        },
        {
          path: "app/settings",
          name: "dashboardappsettings",
          component: () =>  import("../components/AppDashboardAppSettings.vue"),
        },
      ]
    },
    {
      path: "/auth",
      name: "auth",
      component: AuthView,
      meta: {requiresAuth: false},
      children: [
        {
          path: "signup",
          name: "signup",
          component: () => import("../components/AppSignUp.vue"),
          meta: {title: "Sign up | Open User Data"}
        },
        {
          path: "signup/social",
          name: "signupsocial",
          component: () => import("../components/AppSignUpSocial.vue"),
        },
        {
          path: "signin",
          name: "signin",
          component: () => import("../components/AppSignIn.vue"),
          meta: {title: "Sign In | Open User Data"}
        },
        {
          path: "help/forgot-password",
          name: "forgotpassword",
          component: () => import("../components/AppForgotPassword.vue"),
          meta: {title: `Forgot password | Open User Data`}
        },
        {
          path: "help/success/reset-password",
          name: "resetpassword",
          component: () => import("../components/AppResetPassword.vue"),
          meta: {title: `Reset password | Open User Data`}
        },
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import("../components/AppNotFound.vue"),
      meta: {title: `404 | Page not found | Open User Data`}
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) return {el: to.hash,  behavior: "smooth"}
    else return { top: 0, behavior: "smooth" }
  }
});

router.beforeEach(async (to, from) => {
  document.title = to.meta.title
  const userStore = useUserStore()

  if (to.name == 'home' && JSON.parse(localStorage.getItem('is_auth'))) {
    return {name: 'dashboard', params: {username: userStore.userProfile['username']}}
  }
  if (to.meta.requiresAuth && !JSON.parse(localStorage.getItem('is_auth'))) {
    return {name: 'signin', query: {redirect: to.path}}
  }
})

export default router;
