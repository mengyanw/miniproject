<template>
  <div>
    <div style="padding-bottom: 40px">
      <label for="truncBy">Truncate by:</label>
      <select
        v-model="store.truncBy"
        @change="store.setTruncBy($event.target.value)"
        size="small"
      >
        <option value="day">Day</option>
        <option value="week">Week</option>
        <option value="month">Month</option>
      </select>
    </div>
    <apexchart
      type="line"
      :options="chartOptions"
      :series="store.timeSeriesData"
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
      chartOptions: {
        chart: {
          type: "area",
          stacked: "true",
        },
        xaxis: {
          type: "datetime",
        },
        yaxis: {
          labels: {
            formatter: function (val) {
              return val.toFixed(0);
            },
          },
        },
        colors: ["#008FFB", "#00E396", "#CED4DC"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "monotoneCubic",
        },
        fill: {
          type: "gradient",
          gradient: {
            opacityFrom: 0.6,
            opacityTo: 0.8,
          },
        },
        legend: {
          position: "top",
          horizontalAlign: "left",
        },
      },
    };
  },
  async mounted() {
    await store.getTimeSeriesData();
  },
};
</script>
