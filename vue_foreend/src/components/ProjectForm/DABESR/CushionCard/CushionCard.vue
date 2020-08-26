<template>

<v-card>
  <v-card-title>
      Cushion
  </v-card-title>
  <v-card-text>
    <v-checkbox
      v-model="enabled"
      hide-details
      class="shrink mr-2 mt-0"
      label="New Cushion"
      ></v-checkbox>
    <v-row align="center">
      <v-file-input 
        id = 'CushiondwgFile'
        type = 'file'
        accept=".dwg" 
        :disabled="!enabled"  
        label="Cushion dwg file"
      >
      </v-file-input>
      <v-file-input 
        v-model = "CurrentForm.CushionFoldFile" 
        type = 'file'
        accept=".pdf" 
        :disabled="!enabled" 
        label="New cushion folding file"
        @change="uploadFile"
      ></v-file-input>
    </v-row>
    <v-text-field
      id = 'CushionFoldFile'
      type = 'text'
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      @change="uploadFile"
    >
    </v-text-field>
      </v-card-text>
  </v-card>  

  
</template>>

<script>
import {mapState} from 'vuex';
export default {
    data: () => ({
      enabled: false,
    }),
    computed:{
      isError:function(){
        if ((this.CurrentForm.CushiondwgFile != '' && this.CurrentForm.CushionFoldFile != '') || this.CurrentForm.OldCushion != ''){
            return false
        } else {
            return true
            }
         },
      ...mapState({
        CurrentForm : state => state.form,
        })
    },

    methods:{
      validate () {
        this.$store.commit('nextStep')
      },
      onBackStep(){
          this.$store.commit('backStep')
      },
      onClearData(){
        this.CurrentForm.CushiondwgFile = [],
        this.CurrentForm.CushionFoldFile= [],
        this.CurrentForm.OldCushion = []
      },
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