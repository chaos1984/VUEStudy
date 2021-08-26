<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div id="main" style="width: 1200px; height: 800px"></div>
</template>
<script>
import echarts from "echarts";
export default {
 
  data() {
    return {
     bar:{}
    };
  },
  mounted() {
  this.drawDatafromJson();
 
  },

  methods: {
    drawDatafromJson() {
      this.$axios.get("/static/json/Mat.json").then(
        (response) => {
          this.bar = JSON.parse(JSON.stringify(response.data));
          console.log(this.bar)
          this.draw("main")
        },
        (error) => {
          console.log(error);
        }
      );

    },

    draw(id) {
           
      this.charts = echarts.init(document.getElementById(id));
      this.charts.setOption({
    tooltip: {
        trigger: 'axis'
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    textStyle:{
      fontSize:22,
    }, 
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            saveAsImage: {show: true}
        }
    },
    lineHeight: 56,
    xAxis: [
        {
            type: 'category',
            axisTick: {show: false},
            data: ['E', 'Ro', 'Toughness_LT','Toughness_RT','Toughness_HT'],
            
            axisLabel: {
                textStyle: {
                fontSize :20,
                lineHeight:50
                }
            }
        }
    ],
     yAxis: [
        {
            type: 'value',
            axisLabel: {
                textStyle: {
                fontSize :20
                }
            }
        }
    ],
    title: {
          left: 'center',
          text: '应变率 100/s',
          fontSize:100
        },
    legend: {
        show:true,
        bottom: "bottom",
        lineHeight:10
    },
    series: this.bar
      
      });
    },
  },
  //调用

};
</script>