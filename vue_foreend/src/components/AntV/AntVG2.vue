<template>
  <div id="roomTypeCheckIn"></div>
</template>

<script>
import { Radar } from "@antv/g2plot";
export default {
  name: "",
  //数据部分
  data() {
    return {
      mydata: [
        { item: "Design", score: 70 },
        { item: "Development", score: 60 },
        { item: "Marketing", score: 40 },
        { item: "Technology", score: 30 },
      ],
    };
  },
  //初始加载
  mounted() {
    this.initComponent();
  },
  methods: {
    initComponent() {
      const radarPlot = new Radar("roomTypeCheckIn", {
        data: this.mydata,
        xField: "item",
        yField: "score",
        meta: {
          score: {
            alias: "分数",
          },
        },
        yAxis: {
          grid: {
            alternateColor: ["rgba(0, 0, 0, 0.04)", null],
          },
        },
        point: {},
      });
      radarPlot.render();
    },
  },
};
</script>