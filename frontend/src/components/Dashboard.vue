<script setup>
import Top3Posts from "./Top3Posts.vue";
import TimeSeriesChart from "./TimeSeriesChart.vue";
import TotalEngagement from "./TotalEngagement.vue";
import PostCount from "./PostCount.vue";
import { store } from "../store.js";
</script>

<template>
  <a-row style="height: 50px">
    <div>
      Filter by Post Type:
      <a-radio-group
        v-model:value="store.postType"
        @change="store.setPostType($event.target.value)"
      >
        <a-radio-button value="fan">Fan posts using a hashtag</a-radio-button>
        <a-radio-button value="stadium"
          >Fan posts near the stadium</a-radio-button
        >
        <a-radio-button value="branded_without_fans"
          >Branded posts</a-radio-button
        >
      </a-radio-group>
    </div>
  </a-row>
  <a-row></a-row>
  <div style="background-color: #ececec; padding: 20px">
    <a-row :gutter="16">
      <a-col :span="16">
        <a-row :gutter="16">
          <a-col :span="12" :gutter="16">
            <a-card title="Total Engagement by sentiment" :bordered="false">
              <TotalEngagement />
            </a-card>
          </a-col>
          <a-col :span="12" :gutter="16">
            <a-card title="Post count by sentiment" :bordered="false">
              <PostCount />
            </a-card>
          </a-col>
        </a-row>
        <a-row style="height: 20px"></a-row>
        <a-row :gutter="16">
          <a-col :span="24">
            <a-card
              title="Average Engagement by sentiment and time"
              :bordered="false"
            >
              <TimeSeriesChart />
            </a-card>
          </a-col>
        </a-row>
      </a-col>
      <a-col :span="8" :gutter="16">
        <a-card title="Top 3 posts by engagement" :bordered="false">
          <Top3Posts />
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>
