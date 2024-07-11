<template>
  <div>
    <apexchart
      type="bar"
      :options="chartOptions"
      :series="store.postCount"
    ></apexchart>
  </div>
</template>

<script setup>
import { store } from "../store.js";
</script>

<script>
import ApexCharts from "vue3-apexcharts";

export default {
  components: {
    apexchart: ApexCharts,
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: "bar",
        },
        plotOptions: {
          bar: {
            horizontal: true,
            dataLabels: {
              position: "top",
            },
          },
          // dataLabels: {
          //     enabled: true,
          //     style: {
          //         colors: ['#333']
          //     },
          //     offsetY: 50
          // },
        },
      },
    };
  },
  mounted() {
    store.getPostCount();
  },
};
</script>
