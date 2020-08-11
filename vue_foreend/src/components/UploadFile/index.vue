<template>
<div>    
<input class="file" name="file" type="file" accept="image/png,image/gif,image/jpeg" @change="update" />
    <div style="position: absolute; width: 300px; height: 10px;">
            <img style="position: absolute; top: 0; left: 0; width: 300px;" :src="img" >
            <Timer style="position: absolute; top: 435px; left: 68px;"></Timer>

    </div>
</div>
</template>

<script>
import Timer from '@/components/Timer/Timer';
export default {
components: {
  Timer,
  },
  
data: () => ({
    img : ""
 }),

methods: {
      update(e){
        let file = e.target.files[0];
        let param = new FormData(); //创建form对象
        param.append('file',file);//通过append向form对象添加数据
        console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
        this.$axios.post('http://10.123.20.255:5000/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, {responseType:"arraybuffer"})
          .then(res=>{
                this.img = 'data:;base64,' +res.data
          })
          .catch(function (error) {
            console.log(error);
          })
      },
    }
}
</script>
