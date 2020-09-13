<template>
  <div id="app">
    <h1>Common Cover Material Properties Comparison </h1>
    <v-divider/>
    <v-chart  class="my-chart" :options="bar"/>
  </div>
</template>
<script>
import ECharts from "vue-echarts/components/ECharts";
import "echarts/lib/chart/bar";
import 'echarts/lib/component/tooltip'
export default {
  name: "App",
  components: {
    "v-chart": ECharts
  },
  data :
    function() {
    return {
      bar: {
        title: {
          text: "ECharts 入门示例"
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
        }
    },
     legend: {
        data: ['Forest', 'Steppe', 'Desert', 'Wetland'],
        show:true
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {show: false},
            data: ['E', 'Ro', 'Toughness_LT','Toughness_RT','Toughness_HT'],
            axisLabel: {
                textStyle: {
                fontSize :14
                }
            }
        }
    ],
    yAxis: [
        {
            type: 'value',
            axisLabel: {
                textStyle: {
                fontSize :14
                }
            }
        }
    ],
    series:[]
      }
    };
  },

    mounted(){
      this.getData()
    },
    methods: {
      getData() {
      this.$axios.get("/static/json/echart.json").then(
        response => {
          console.log(response.data);
          this.bar.series = JSON.parse(response.data);
          console.log(this.bar.series)
        },
        error => {  
          console.log(error);
        }
      );
    },
    }
  }
</script>
<style>
.my-chart {
  width: 800px;
  height: 500px;
}
</style>
