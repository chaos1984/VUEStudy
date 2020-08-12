<template>
<span ><p>{{ date }}</p></span>
</template>
<script>
export default {
data(){
    return {
    time: '',
    date: '',
  };
  },
mounted(){
    this.Timer();
},
methods: {
    Timer(){
        var timerID = setInterval(this.updateTime, 1000);
        this.updateTime();
        return timerID
    },
    updateTime() {
        // var week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
        var cd = new Date();
        this.time = this.zeroPadding(cd.getHours(), 2) + ':' + this.zeroPadding(cd.getMinutes(), 2) + ':' + this.zeroPadding(cd.getSeconds(), 2);
        this.date = this.zeroPadding(cd.getFullYear(), 4) + '/' + this.zeroPadding(cd.getMonth()+1, 2) + '/' + this.zeroPadding(cd.getDate(), 2) + ' ' + this.time;
    },
    zeroPadding(num, digit) {
        var zero = '';
        for(var i = 0; i < digit; i++) {
          zero += '0';
        }
        return (zero + num).slice(-digit);
    }
       }
}
</script>

<style>
p {font-size:1.1em;}
</style>