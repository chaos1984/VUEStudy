<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BomInfo
  </v-card-title>

  <v-card-text>
      <v-file-input
        id = "BOMFile"
        label="Upload the BOM FILE"
        placeholder="Select a file"
        :rules="BOMFileRules"
        @change="uploadFile"
      ></v-file-input>  
      <v-file-input 
        id = "CADFile"
        label="Upload the CAD FILE"
        placeholder="Select a file"
        :rules="CADFileRules"
        @change="uploadFile"
      ></v-file-input> 
      <!-- <v-btn color="primary" text @click="uploadFile">test</v-btn> -->
    </v-card-text>

  </v-card>  
    

</template>

<script>
import {mapState} from 'vuex';
  export default {
    data: () => ({
      filedata: null,
      enabled: false,
      BOMFileRules:[
        v => !!v || 'Required',
      ],
      CADFileRules:[
        v => !!v || 'Required',
      ]  
    }),
    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    methods:{
      uploadFile(e){
        var clickedButtonDOM=event.target; //获取按钮的DOM元素
        var id = clickedButtonDOM.getAttribute('id');//获取指定的元素
        console.log(id);
        let param = new FormData(); //创建form对象
        param.append('file',e);//通过append向form对象添加数据
        // param.append('file',this.CurrentForm.CADFile)
        // console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
        
        this.filedata = param.get('file')
        this.CurrentForm[id] = this.filedata['name']
        // console.log(e)
        this.CurrentForm[e]= this.filedata['name']
        this.$axios.post('/api/upload',param,{headers:{'Content-Type':'application/x-www-form-urlencoded' }}, ) //请求头要为表单
          .then(response=>{
            console.log(response.data);
          })
          .catch(function (error) {
            console.log(error);
          })
      }
   }
  }
</script>