<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div id="DAB" style="width: 100%; height: 400px"></div>
</template>
<script>
//eslint disable next line
import echarts from "echarts";

export default {
  props: {
    getdata: {},
  },
  data() {
    return {
      DAB: { failure: [], nofailure: [] },
      mydata: {},
    };
  },
  mounted() {
    this.drawDatafromDB();
  },



  watch: {
    getdata(newval) {
      console.log(newval)
      this.drawDatafromDB()
    },
  },

  methods: {
    drawDatafromJson() {
      this.$axios.get("/static/json/DAB.json").then(
        (response) => {
          this.DAB = JSON.parse(JSON.stringify(response.data));
          this.drawPie("DAB");
        },
        (error) => {
          console.log(error);
        }
      );
    },

    drawDatafromDB() {
      this.mydata = this.getdata;
      this.DAB.failure = [];
      this.DAB.nofailure = [];
      for (var i = 0; i < this.mydata.length; i++) {
        if (this.mydata[i].Simulation == "1") {
          // console.log(typeof(this.DAB.failure))
          this.DAB.failure.push([
            parseFloat(this.mydata[i].H_Width),
            parseFloat(this.mydata[i].Flappy_Mass),
            this.mydata[i].PRJ,
          ]);
        } else {
          // console.log(typeof(this.DAB.nofailure))
          this.DAB.nofailure.push([
            parseFloat(this.mydata[i].H_Width),
            parseFloat(this.mydata[i].Flappy_Mass),
            this.mydata[i].PRJ,
          ]);
        }
      }
      // console.log(this.DAB)
      this.drawPie("DAB");
    },

    // drawDatafromDB() {
    //   this.DAB.failure = [];
    //   this.DAB.nofailure = [];
    //   for (var i = 0; i < this.CurrentForm.data4fig.length; i++) {
    //     if (this.CurrentForm.data4fig[i].Simulation == "1") {
    //       // console.log(typeof(this.DAB.failure))
    //       this.DAB.failure.push([
    //         parseFloat(this.CurrentForm.data4fig[i].H_Width),
    //         parseFloat(this.CurrentForm.data4fig[i].Flappy_Mass),
    //         this.CurrentForm.data4fig[i].PRJ,
    //       ]);
    //     } else {
    //       // console.log(typeof(this.DAB.nofailure))
    //       this.DAB.nofailure.push([
    //         parseFloat(this.CurrentForm.data4fig[i].H_Width),
    //         parseFloat(this.CurrentForm.data4fig[i].Flappy_Mass),
    //         this.CurrentForm.data4fig[i].PRJ,
    //       ]);
    //     }
    //   }
    //   // console.log(this.DAB)
    //   this.drawPie("DAB");
    // },

    drawPie(id) {
      this.charts = echarts.init(document.getElementById(id));
      this.charts.setOption({
        title: {
          text: "DAB Cover ESR",
          subtext: "Data from: 2021-04-14",
        },
        grid: {
          left: "3%",
          right: "7%",
          bottom: "7%",
          containLabel: true,
        },
        tooltip: {
          // trigger: 'axis',
          showDelay: 1,
          formatter: function (params) {
            if (params.value.length > 1) {
              return (
                params.value[2] +
                " :<br/>" +
                params.value[0] +
                "mm " +
                params.value[1] +
                "kg "
              );
            } else {
              return (
                params.value[2] +
                " :<br/>" +
                params.name +
                " : " +
                params.value +
                "kg "
              );
            }
          },
          axisPointer: {
            show: true,
            type: "cross",
            lineStyle: {
              type: "dashed",
              width: 1,
            },
          },
        },
        toolbox: {
          feature: {
            dataZoom: {},
            dataView: { readOnly: false },
            restore: {},
          },
        },
        // brush: {},
        legend: {
          data: ["No failure", "Failure"],
          left: "center",
          bottom: 0,
        },
        xAxis: [
          {
            type: "value",
            scale: true,
            axisLabel: {
              formatter: "{value} mm",
            },
            splitLine: {
              show: false,
            },
          },
        ],
        yAxis: [
          {
            type: "value",
            scale: true,
            axisLabel: {
              formatter: "{value} kg",
            },
            splitLine: {
              show: false,
            },
          },
        ],
        series: [
          {
            name: "No failure",
            type: "scatter",
            emphasis: {
              focus: "series",
            },
            data: this.DAB.nofailure,
            markArea: {
              silent: true,
              itemStyle: {
                color: "transparent",
                borderWidth: 1,
                borderType: "dashed",
              },
              data: [
                [
                  {
                    name: "No failure Data Range",
                    xAxis: "min",
                    yAxis: "min",
                  },
                  {
                    xAxis: "max",
                    yAxis: "max",
                  },
                ],
              ],
            },
            markPoint: {
              data: [
                { type: "max", name: "Max" },
                { type: "min", name: "Min" },
              ],
            },
            // markLine: {
            //   lineStyle: {
            //     type: "solid",
            //   },
            //   data: [{ type: "average", name: "average line" }],
            // },
          },
          {
            name: "Failure",
            type: "scatter",
            emphasis: {
              focus: "series",
            },
            data: this.DAB.failure,
            markArea: {
              silent: true,
              itemStyle: {
                color: "transparent",
                borderWidth: 1,
                borderType: "dashed",
              },
              data: [
                [
                  {
                    name: "Failure Data Range",
                    xAxis: "min",
                    yAxis: "min",
                  },
                  {
                    xAxis: "max",
                    yAxis: "max",
                  },
                ],
              ],
            },
            markPoint: {
              data: [
                { type: "max", name: "Max" },
                { type: "min", name: "Min" },
              ],
            },
            // markLine: {
            //   lineStyle: {
            //     type: "solid",
            //   },
            //   data: [{ type: "average", name: "平均值" }, { xAxis: 170 }],
            // },
          },
        ],
      });
    },
  },
  //调用
};
</script>
<style scoped>
* {
  margin: 10;
  padding: 0;
  list-style: none;
}
</style>