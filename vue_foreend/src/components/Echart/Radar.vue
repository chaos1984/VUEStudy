<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <!-- <div> -->
    <div style="width: 100%; height: 400px">
      <div style="width: 100%; height: 10%"></div>
    <v-spacer></v-spacer>
    <div id="Radar" ref="chart" style="width: 100%; height: 90%"></div>
    </div>
  <!-- </div> -->
</template>
<script>
//eslint disable next line
import echarts from "echarts";

export default {
  props: {
    getdata: [],
  },
  data() {
    return {
      itemLegend: [],
      itemData: [],
    };
  },

  //   created() {
  //   console.log('drawRadar')

  //     this.Itemlabel = this.itemList[4];
  //         selectedItem = this.getdata;
  //     this.drawDatafromDB();
  //   },

  mounted() {
    // selectedItem = this.getdata;
    this.drawRadar("Radar");
  },

  watch: {
    getdata(newval) {
      // console.log(newval);
      this.itemData=[]
      this.drawDatafromDB(newval);
    },
  },

  methods: {
    drawDatafromDB(selectedItem) {
      // console.log("object");
      for (var i = 0; i < selectedItem.length; i++) {
        this.itemLegend.push(selectedItem[i].PRJ);
        // console.log(selectedItem[i]);
        this.itemData.push(
          {
                    value: [selectedItem[i].Flappy_Mass, selectedItem[i].Hinge_Area, selectedItem[i].Hinge_HLratio, selectedItem[i].Hinge_Width,  selectedItem[i].CV_Height],
                    name: selectedItem[i].PRJ,
                    symbol: 'rect',
                    symbolSize: 12,
                    lineStyle: {
                        type: 'dashed'
                    },
                    label: {
                        show: true,
                        formatter: function (params) {
                            return params.value;
                        }
                    }
                },
         
        );
        // console.log(selectedItem[i].PRJ);
      }
      
      
      this.drawRadar();
    },

    drawRadar() {
      // console.log(this.itemData);
      var radar = this.$refs.chart;
      //   this.charts = echarts.init(document.getElementById(id));
      this.charts = echarts.init(radar);
      this.charts.setOption({
        // color: [  '#56A3F1', '#FF917C'],
        title: {
          text: "Project comparison",
        },
        legend: {
          data:this.itemLegend,
          // orient: "vertical",
          // left: "right",
          bottom: 0,
        },
        radar: [
          {
            indicator: [
              { text: "Flap Mass", max: 0.055 },
              { text: "Hinge Area", max: 300 },
              { text: "Hinge L/H", max: 0.22},
              { text: "Hinge Width", max: 25 },
              { text: "Cover Height", max: 40 },
              

            ],
            // center: ['75%', '50%'],
            radius: "65%",
            name: {
              textStyle: {
                color: "#666",
                // backgroundColor: '#666',
                borderRadius: 3,
                padding: [3, 5],
              },
            },
          },
        ],
        series: [
          {
            name: '雷达图',
            type: 'radar',
            emphasis: {
                lineStyle: {
                    width: 4
                }
            },
            data: this.itemData
            // [
            //     {
            //         value: [120, 118, 130, 100, 99, 70],
            //         name: 'Data C',
            //         symbol: 'rect',
            //         symbolSize: 12,
            //         lineStyle: {
            //             type: 'dashed'
            //         },
            //         label: {
            //             show: true,
            //             formatter: function (params) {
            //                 return params.value;
            //             }
            //         }
            //     },
                
            // ]
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