import { createApp } from "vue";
import App from "./App.vue";
import VueApexCharts from "vue3-apexcharts";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/reset.css";

const app = createApp(App);
app.use(VueApexCharts);
app.use(Antd);
app.mount("#app");
