/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthView from "../views/AuthView.vue";
import DashboardView from "../views/DashboardView.vue";
import { useAuthStore } from "../stores/auth";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        title: "Welcome | Open User",
        transition: 1,
        transitionName: "",
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
          meta: {
            transition: 2,
            transitionName: "",
          }
        },
        {
          path: "settings",
          name: "dashboardusersettings",
          component: () =>  import("../components/AppDashboardSettings.vue"),
          meta: {
            transition: 3,
            transitionName: "",
          }
        },
        {
          path: "apps/:appName",
          name: "dashboardapp",
          component: () =>  import("../components/AppDashboardApp.vue"),
          meta: {
            transition: 4,
            transitionName: "",
          }
        },
        {
          path: "apps/:appName/settings",
          name: "dashboardappsettings",
          component: () =>  import("../components/AppDashboardAppSettings.vue"),
          meta: {
            transition: 5,
            transitionName: "",
          }
        },
        {
          path: "apps/create",
          name: "dashboardappcreate",
          component: () =>  import("../components/AppDashboardAppCreate.vue"),
          meta: {
            transition: 6,
            transitionName: "",
          }
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
          meta: {
            title: "Sign up | Open User",
            transition: 2,
            transitionName: "",
          }
        },
        {
          path: "signup/social/:provider",
          name: "signupsocial",
          component: () => import("../components/AppSignUpSocial.vue"),
          meta: {
            transition: 3,
            transitionName: "",
          }
        },
        {
          path: "signin",
          name: "signin",
          component: () => import("../components/AppSignIn.vue"),
          meta: {
            title: "Sign In | Open User",
            transition: 4,
            transitionName: "",
          }
        },
        {
          path: "help/forgot-password",
          name: "forgotpassword",
          component: () => import("../components/AppForgotPassword.vue"),
          meta: {
            title: 'Forgot password | Open User',
            transition: 5,
            transitionName: "",
          }
        },
        {
          path: "help/success/reset-password/:uid/:token",
          name: "resetpassword",
          component: () => import("../components/AppResetPassword.vue"),
          meta: {
            title: 'Reset password | Open User',
            transition: 6,
            transitionName: "",
          }
        },
        {
          path: "verify-email",
          name: "verifyemail",
          component: () => import("../components/AppVerifyEmail.vue"),
          meta: {
            title: 'Verify Email | Open User',
            transition: 7,
            transitionName: "",
          }
        },
      ]
    },
    {
      path: "/terms-and-condition",
      name: "termsandcondition",
      component: () => import("../components/AppTermsAndCondition.vue"),
      meta: {
        title: 'Terms & Condition | Open User',
        transition: 7,
        transitionName: "",
      }
    },
    {
      path: "/privacy-policy",
      name: "privacypolicy",
      component: () => import("../components/AppPrivacyPolicy.vue"),
      meta: {
        title: 'Privacy Policy | Open User',
        transition: 7,
        transitionName: "",
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import("../components/AppNotFound.vue"),
      meta: {
        title: '404 | Page not found | Open User',
        transition: 2,
        transitionName: "",
      }
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) return {el: to.hash,  behavior: "smooth"}
    else return { top: 0, behavior: "smooth" }
  }
});

router.beforeEach(async (to, from) => {
  // set page title
  document.title = to.meta.title

  // set the transition name of the incoming route, bases on transition id
  to.meta.transitionName = to.meta.transition > from.meta.transition ? "slide-left":"slide-right";
  
  // stores
  const authStore = useAuthStore()

  if (to.name == 'home' && JSON.parse(localStorage.getItem('is_auth'))) {
    return {name: 'dashboard', params: {username: authStore.userProfile['username']}}
  }
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return {name: 'signin', query: {redirect: to.path}}
  }
})


export default router;
