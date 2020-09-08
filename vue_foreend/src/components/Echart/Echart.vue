<template>
  <div id="app">
    <h1>Common Cover Material Properties Comparison </h1>
    <v-divider/>
    <v-chart class="my-chart" :options="bar"/>
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
  data: function() {
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
            data: ['E', 'Ro', 'Toughness_LT','Toughness_RT','Toughness_RT'],
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
    series: [
        {
            name: 'TA4003BE',
            type: 'bar',
            barGap: 0,
  
            data: [1, 1, 1,1,1 ]
            //data: [1, 1, 1, 1]
            //data: [1, 1, 1, 1]
        },
        {
            name: 'TT1081',
            type: 'bar',

            data: [1, 0.99, 0.82,1.02,0.52]
            //data: [1, 1.1, 1.2,1.5 ]
            //data: [1, 1.1, 1.2,1.5 ]
        },
        {
            name: 'TT990',
            type: 'bar',

            data: [1, .99, 2.39,3.27,1.06]
           // data: [1, 1.1, 1.2,1.5 ]
           // data: [1, 1.1, 1.2,1.5 ]
        }
    ]
      }
    };
  }
};
</script>
<style>
.my-chart {
  width: 800px;
  height: 500px;
}
</style>
