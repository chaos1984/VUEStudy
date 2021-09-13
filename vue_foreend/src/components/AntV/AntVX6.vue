<template>
  <div id="app"></div>
</template>

<script>
import { Graph } from "@antv/x6";
import "@antv/x6-vue-shape";
// import ChangeSize from "./ChangeSize";
import Count from "./Count";

export default {
  name: "App",
  data() {
    return {
      nodeData: {
        num: 0,
      },
    };
  },
  components: {
    // ChangeSize,
  },
  mounted() {
    const self = this;
    const graph = new Graph({
      container: document.getElementById("app"),
      width: 600,
      height: 400,
      grid: true,
    });

    Graph.registerVueComponent(
      "count-component",
      {
        template: `<count :num="num" @add="add"></count>`,
        data() {
          return self.nodeData;
        },
        methods: {
          add(step) {
            self.nodeData.num += step;
          },
        },
        components: {
          Count,
        },
      },
      true
    );

    // graph.addNode({
    //   shape: "vue-shape",
    //   x: 300,
    //   y: 100,
    //   width: 150,
    //   height: 100,
    //   attrs: {
    //     body: {
    //       stroke: "#ebebeb",
    //     },
    //   },
    //   component: {
    //     template: `<change-size></change-size>`,
    //     data() {
    //       return {};
    //     },
    //     components: {
    //       ChangeSize,
    //     },
    //   },
    // });

    graph.addNode({
      shape: "vue-shape",
      x: 300,
      y: 250,
      width: 150,
      height: 100,
      component: "count-component",
    });
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
