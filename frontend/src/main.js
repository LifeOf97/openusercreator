/* eslint-disable */
import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueCookies from "vue-cookies";
import "./assets/styles/index.css";

// axios settings
axios.defaults.baseURL = "http://192.168.43.208:8000/";
// axios.defaults.baseURL = "http://127.0.0.1:8000/";
axios.defaults.headers.common["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
