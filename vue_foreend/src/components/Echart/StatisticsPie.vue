<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div>
    <el-select v-model="Itemlabel" placeholder="Select one item to plot pie" @change='drawDatafromDB'>
      <el-option
        v-for="(item, index) in itemList"
        :key="index"
        :label="item"
        :value="item"
      >
      </el-option>
    </el-select>
    <div id="StatisticPie" style="width: 100%; height: 400px"></div>
    <!-- <el-divider/> -->
    <div></div>
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
      item: "",
      selectwidth: "width: 385px",
      formLabelWidth: "130px",
      itemList: "",
      Itemlabel: "",
    };
  },

  created() {
  console.log('DrawPie')

    this.Itemlabel = this.itemList[4];
        this.mydata = this.getdata;
    this.drawDatafromDB();
  },

  mounted() {
    this.mydata = this.getdata;
    this.drawDatafromDB();
  },

  watch: {
    getdata(newval) {
      console.log(newval);
      this.drawDatafromDB();
    },
  },

  methods: {
    drawDatafromDB() {
      this.mydata = this.getdata;
      this.itemList = Object.keys(this.mydata[0]);
      var obj = {};
      for (var i = 0; i < this.mydata.length; i++) {
        var item = this.mydata[i][this.Itemlabel];
        obj[item] = obj[item] + 1 || 1;
      }
      // console.log('aaa')
      // console.log(this.mydata)
      // console.log(Object.keys(obj).length)
      var drawdata = [];
      for (var j = 0; j<Object.keys(obj).length; j++) {
        drawdata.push({'name':Object.keys(obj)[j],'value':Object.values(obj)[j]})
        
        // drawdata.push({'value':Object.values(obj[j])})
      }
      this.drawPie("StatisticPie",drawdata);
    },

    drawPie(id,drawdata) {
      this.charts = echarts.init(document.getElementById(id));
      this.charts.setOption({
        title: {
          text: "Statistics of DAB ESR",
          subtext: "2021-05-14",
        },

        tooltip: {
          trigger: "item",
        },
        toolbox: {
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {}
          },
        },
        // brush: {},
        legend: {
          orient: "vertical",
          left: "right",
          bottom: 100,
        },
        textStyle: {
          frontFamily: "Microsoft YaHei",
          fontSize: 12,
        },
        color: [
          "#5470c6",
          "#91cc75",
          "#fac858",
          "#ee6666",
          "#73c0de",
          "#3ba272",
        ],
        series: [
          {
            type: "pie",
            radius: "80%",
            data:drawdata,
            emphasis: {
              itemStyle: {
                shadowBlur: 30,
                shadowOffsetX: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
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