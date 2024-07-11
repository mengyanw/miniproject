import { reactive } from "vue";
import axios from "axios";

const URL = "http://127.0.0.1:8000/api/";

export const store = reactive({
  postType: "stadium",
  truncBy: "week",
  topNPosts: [],
  timeSeriesData: [],
  totalEngagement: [],
  postCount: [],

  async setPostType(newPostType) {
    this.postType = newPostType;
    await this.getTimeSeriesData();
    await this.getTopNPosts();
    await this.getTotalEngagement();
    await this.getPostCount();
  },
  async setTruncBy(newTruncBy) {
    this.truncBy = newTruncBy;
    console.log(newTruncBy);
    await this.getTimeSeriesData(newTruncBy);
  },
  async getTimeSeriesData(newTruncBy) {
    const truncBy = newTruncBy ? newTruncBy : this.truncBy;
    const response = await axios.get(
      URL + `posts/time_series/?trunc_by=${truncBy}&post_type=${this.postType}`
    );
    this.timeSeriesData = await response.data;
  },
  async getTopNPosts() {
    const response = await axios.get(
      URL + `posts/topN/?post_type=${this.postType}`
    );
    this.topNPosts = await response.data;
  },
  async getTotalEngagement() {
    const response = await axios.get(
      URL + `posts/total_engagement/?post_type=${this.postType}`
    );
    this.totalEngagement = [{ data: await response.data }];
  },
  async getPostCount() {
    const response = await axios.get(
      URL + `posts/post_count/?post_type=${this.postType}`
    );
    this.postCount = [{ data: await response.data }];
  },
});
