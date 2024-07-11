<template>
  <div>
    <div class="chart">
      <label for="truncBy">Truncate by:</label>
      <select v-model="truncBy" @change="getAnalysisData">
        <option value="day">Day</option>
        <option value="week">Week</option>
        <option value="month">Month</option>
      </select>
    </div>
    <apexchart type="line" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import axios from "axios";
import ApexCharts from "vue3-apexcharts";

export default {
  components: {
    apexchart: ApexCharts,
  },
  data() {
    return {
      analysisData: [],
      truncBy: "week", // Default value
      series: [],
      chartOptions: {
        chart: {
          type: "area",
          stacked: "true",
        },
        xaxis: {
          type: "datetime",
        },
        yaxis: {
          title: {
            text: "Avg Engagement",
          },
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
  methods: {
    async getAnalysisData() {
      const response = await axios.get(
        import.meta.env.VITE_API_URL +
          `posts/time_series/?trunc_by=${this.truncBy}`,
      );
      console.log(response.data);
      this.analysisData = response.data;
      this.updateChart();
    },
    updateChart() {
      this.series = this.analysisData;
    },
  },
  mounted() {
    this.getAnalysisData();
  },
};
</script>

<style scoped>
.chart {
  width: 500px;
}
/* Add any necessary styles here */
</style>
