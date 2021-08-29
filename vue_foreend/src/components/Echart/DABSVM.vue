<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div style="width: 100%; height:400px">
    <div style="width: 100%; height:10%">
    <el-row :gutter="5">
      <el-col :span="8">
        <el-select
          v-model="TestorSim"
          placeholder="Select Test or Simulation"
          @change="drawDatafromDB"
        >
          <el-option label="Testing" value="1"></el-option>
          <el-option label="Simulation" value="0"></el-option>
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select
          v-model="FailureMode"
          placeholder="Select Failure mode"
          @change="drawDatafromDB"
        >
          <el-option
            v-for="(item, index) in formItem.FailureMode"
            :key="index"
            :label="item"
            :value="item"
          >
          </el-option>
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select
          v-model="Item"
          clearable
          placeholder="Select Feature"
          @change="drawDatafromDB"
        >
          <el-option-group
            v-for="group in ItemGroup"
            :key="group.label"
            :label="group.label"
          >
            <el-option
              v-for="item in group.options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-option-group>
        </el-select>
      </el-col>
    </el-row>
    </div>
    <div id="DAB" ref="chart" style="width: 100%; height:80%"></div>
  </div>
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
      failurelist: {},
      formItem: {},
      TestorSim: "Simulation",
      FailureMode: "Hinge Overtear",
      Item: "",
      ItemList: [],
      ItemGroup: [],
    };
  },

  created: function () {
    this.getDatafromJson();
  },

  mounted() {
    this.drawDatafromDB();
  },

  watch: {
    getdata(newval) {
      console.log(newval);
      this.drawDatafromDB();
    },
  },

  methods: {
    getDatafromJson() {
      this.$axios.get("/static/json/formItem.json").then(
        (response) => {
          this.formItem = JSON.parse(JSON.stringify(response.data));

          this.ItemList = Object.getOwnPropertyNames(this.formItem);
          this.ItemList.pop();
          this.ItemList.pop();
          var temp = [];
          for (var i = 0; i < this.ItemList.length; i++) {
            temp = this.formItem[this.ItemList[i]];
            var optionlist = [];
            for (var j = 0; j < temp.length; j++) {
              optionlist.push({ value: temp[j], label: temp[j] });
            }
            this.ItemGroup.push({
              label: this.ItemList[i],
              options: optionlist,
            });
          }
          // console.log(this.ItemGroup[0].options);
        },
        (error) => {
          console.log(error);
        }
      );
    },

    drawDatafromDB() {
      this.mydata = this.getdata;
      // this.failurelist = this.mydata.
      this.DAB.failure = [];
      this.DAB.nofailure = [];
      for (var i = 0; i < this.mydata.length; i++) {
        var strData = JSON.stringify(this.mydata[i]);

        // console.log(strData.search(this.Item) != -1)
        if (strData.search(this.Item) != -1) {
          if (this.TestorSim === "1") {
            console.log("Testing");
            if (this.mydata[i].Testing.indexOf(this.FailureMode) === -1) {
              this.DAB.nofailure.push([
                parseFloat(this.mydata[i].H_Width),
                parseFloat(this.mydata[i].Flappy_Mass),
                this.mydata[i].PRJ,
              ]);
            } else {
              this.DAB.failure.push([
                parseFloat(this.mydata[i].H_Width),
                parseFloat(this.mydata[i].Flappy_Mass),
                this.mydata[i].PRJ,
              ]);
            }
          } else {
            // console.log("Simulation");
            if (this.mydata[i].Simulation.indexOf(this.FailureMode) === -1) {
              // console.log(typeof(this.DAB.failure))
              this.DAB.nofailure.push([
                parseFloat(this.mydata[i].H_Width),
                parseFloat(this.mydata[i].Flappy_Mass),
                this.mydata[i].PRJ,
              ]);
            } else {
              this.DAB.failure.push([
                parseFloat(this.mydata[i].H_Width),
                parseFloat(this.mydata[i].Flappy_Mass),
                this.mydata[i].PRJ,
              ]);
            }
          }
        }
      }
      this.drawScatter("DAB");
    },

    drawScatter() {
      var charts = this.$refs.chart;
      //   this.charts = echarts.init(document.getElementById(id));
      this.charts = echarts.init(charts);
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
            saveAsImage: {},
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
            itemStyle: {
              color: "#5470c6",
            },
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
            itemStyle: {
              color: "#ee6666",
            },

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