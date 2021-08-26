<template>
    <v-container fluid >
      <h1>Common Cover Material Properties Comparison </h1>
      <v-divider/>        
        <v-row>
      <v-col cols="12">
        <v-row
          align="stretch"
          justify="center"
          class="grey lighten-5"
          style="height: 400px;"
        >
          <v-chart   :options="bar"/>
          <v-chart   :options="bar"/>
        </v-row>
      </v-col>
    </v-row>
      </v-container>


</template>
<script>
import ECharts from "vue-echarts/components/ECharts";
import "echarts/lib/chart/bar";
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/toolbox'
export default {
  name: "App",
  components: {
    "v-chart": ECharts
  },
  data :
    function() {
    return {
      bar: {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
        }
    },
    // color: ['#003366', '#006699', '#4cabce', '#e5323e','#003366'],
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            // mark: {show: true},
            // dataView: {show: true, readOnly: false},
            // magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            // restore: {show: true},
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
                fontSize :10
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
    title: {
          left: 'center',
          text: '应变率 100/s',
        },
    legend: {
        show:true,
        bottom: 10
    },
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
          console.log('3333')
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
  width: 400px;
  height: 500px;
}
</style>
