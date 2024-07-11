import { reactive } from "vue";
import axios from "axios";

export const store = reactive({
  postType: "stadium",
  truncBy: "week",
  topNPosts: [],
  timeSeriesData: [],

  async setPostType(newPostType) {
    this.postType = newPostType;
    await this.getTimeSeriesData();
    await this.getTopNPosts();
  },
  async setTruncBy(newTruncBy) {
    this.truncBy = newTruncBy;
    await this.getTimeSeriesData();
  },
  async getTimeSeriesData() {
    const response = await axios.get(
      import.meta.env.VITE_API_URL +
        `posts/time_series/?trunc_by=${this.truncBy}&post_type=${this.postType}`
    );
    this.timeSeriesData = response.data;
  },
  async getTopNPosts() {
    const response = await axios.get(
      import.meta.env.VITE_API_URL + `posts/topN/?post_type=${this.postType}`
    );
    this.topNPosts = await response.data;
  },
});
