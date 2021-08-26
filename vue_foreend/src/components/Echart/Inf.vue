<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div>
    <el-row>
      <el-col :span="16">
        <div id="inflator" style="width: 100%; height: 600px"></div>
      </el-col>
    
      <!-- <el-divider></el-divider> -->
      <el-col :span="8">
        <el-row>
          <el-form :inline="true" :model="formInline" class="demo-form-inline" >
            <div v-for="(d, index) in user" :key="index" >
              <el-form-item :label="index + ' Time(ms)'" style="width:180px">
                <el-input
                  v-model="formInline.time[index]"
                  placeholder="0"
                ></el-input>
              </el-form-item>
              <el-form-item label="Pressure(kPa)" style="width:180px">
                <el-input
                  v-model="formInline.pressure[index]"
                  placeholder="0"
                ></el-input>
              </el-form-item>
              <el-form-item> </el-form-item>
            </div>
          </el-form>

          <i class="el-icon-circle-plus" @click="addItem"></i>
          <i class="el-icon-remove" @click="delItem"></i>
        </el-row>
        <el-button
          round
          style="font-size: 15px"
          type="primary"
          @click="plotUser"
          >Plot<i class="el-icon-data-line"></i
        ></el-button>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import echarts from "echarts";
export default {
  data() {
    return {
      user: [0],
      test: "",
      line: {},
      input: "",
      formInline: {
        time: [0],
        pressure: [0],
      },
    };
  },
  mounted() {
    // this.drawDatafromJson();
    this.drawDatafromJson();
    // this.extractdata()
  },

  methods: {
    plotUser() {
      var end = this.line.series.length;
      this.line.series[end - 1].data = [];
      for (var i = 0; i < this.user.length; i++) {
        this.line.series[end - 1].data.push([
          this.formInline.time[i],
          this.formInline.pressure[i],
        ]);
      }
      console.log(this.line.series[end - 1].data)
      this.draw("inflator");
    },
    addItem() {
      this.user.push({});
    },
    delItem() {
      this.user.pop({});
    },
    elInFile(f, fs) {
      this.staticFiles.push(f);
      this.mscUrl = URL.createObjectURL(fs[0].raw);
      this.mscName = fs[0].name;
    },
    getUserCurve() {
      this.$axios.get("/static/json/Inf.json").then(
        (response) => {
          this.line = JSON.parse(JSON.stringify(response.data));
          console.log(this.line.series);
          this.draw("inflator");
        },
        (error) => {
          console.log(error);
        }
      );
    },

    drawDatafromJson() {
      this.$axios.get("/static/json/Inf.json").then(
        (response) => {
          this.line = JSON.parse(JSON.stringify(response.data));
          // console.log(this.line.legend);
          this.draw("inflator");
        },
        (error) => {
          console.log(error);
        }
      );
    },
    draw(id) {
      this.charts = echarts.init(document.getElementById(id));
      this.charts.setOption({
        title: {
          text: "发生器压力曲线",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          type: "scroll",
          orient: "vertical",
          right: "right",
          bottom: "10%",
          data: this.line.legend,
          align: "auto",
          textStyle: {
            fontSize: 12,
            // color: '#F1F1F3'
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            dataView: {
              readOnly: false,
            },
            saveAsImage: {},
            restore: {},
            dataZoom: [
              {
                type: "slider", //显示拖拽功能
              },
            ],
          },
        },
        lineHeight: 56,
        xAxis: { type: "category" },
        yAxis: {
          type: "value",
          name: "Pressure(kPa)",
        },
        series: this.line.series,
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
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #125dc5;
}
.bg-purple {
  background: #2fd4f1;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>