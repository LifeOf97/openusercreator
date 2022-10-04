/* eslint-disable */
import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueTippy from "vue-tippy";
import FlagIcon from "vue-flag-icon";

import "./assets/styles/index.css";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";
import "tippy.js/themes/translucent.css";

const app = createApp(App);

// axios settings
axios.defaults.baseURL = "http://192.168.43.208:8000/";
// axios.defaults.baseURL = "http://127.0.0.1:8000/";
axios.defaults.headers.common["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;

// tippy.js
app.use(
    VueTippy,
    // optional
    {
        directive: "tippy", // => v-tippy
        component: "tippy", // => <tippy/>
        componentSingleton: "tippy-singleton", // => <tippy-singleton/>,
        defaultProps: {
            placement: "top",
            allowHTML: true,
        }, // => Global default options * see all props
    }
);

app.use(createPinia());
app.use(router);
app.use(FlagIcon);

app.mount("#app");
