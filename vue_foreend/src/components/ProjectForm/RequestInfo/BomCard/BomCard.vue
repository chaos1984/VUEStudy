<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BOM Info
  </v-card-title>

  <v-card-text>
      <uploadfile :data = "uploadinfo"/>
      <uploadfile :data = "uploadinfo"/>
      <!-- <v-btn color="primary" text @click="uploadFile">test</v-btn> -->
    </v-card-text>

  </v-card>


</template>

<script>
import {mapState} from 'vuex';
  export default {
    data: () => ({
        uploadinfo : {
              disabled:false,
              fileList : [],
              label : 'upload',
              action : 'http://127.0.0.1:5000/upload',
              filenum : 1,
              accepttype : ".jpg,.jpeg,.png,.gif,.bmp,.pdf,.JPG,.JPEG,.PBG,.GIF,.BMP,.PDF"
        },
      filedata: null,
      enabled: false,
      BOMFileRules:[
        v => !!v || 'Required',
      ],
      CADFileRules:[
        v => !!v || 'Required',
      ],
      displayText : 'Select a file'
    }),

    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    methods:{
      emitalert(){
           console.log(this.CurrentForm.BOMFile)
         },
      uploadFile(e){
        var clickedButtonDOM=event.target; //获取按钮的DOM元素
        var id = clickedButtonDOM.getAttribute('id');//获取指定的元素
        let param = new FormData(); //创建form对象
        param.append('file',e);//通过append向form对象添加数据
        // param.append('file',this.CurrentForm.CADFile)
        // console.log(param.get('file')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去

        this.filedata = param.get('file')
        this.CurrentForm[id] = this.filedata['name']
        
        let a = this.CurrentForm[id].split("-")
        console.log(a.length)
        if (a.length != 2 && id == 'BOMFile' ){
          console.log("1")
          param = []
          this.$refs.BOMFile.value = ''
          this.displayText = 'Select a file'
          // alert("Please check the file format!")
        } else if (a.length != 2 && id == 'CADFile' ){
          console.log(a)
          param = []
          this.$refs.CADFile.value = ''
          this.displayText = 'Select a file'
          // alert("Please check the file format!")
        } else if (a == 2) {
        // console.log(e)
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
  }
</script>