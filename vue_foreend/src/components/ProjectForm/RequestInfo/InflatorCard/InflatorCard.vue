<template>
      <v-card height = "249px">
        <v-card-title>
          Inflator
        </v-card-title>
        <v-card-text>
        <v-checkbox
          v-model="enabled"
          hide-details
          class="shrink mr-2 mt-0"
          label="New Inflator"
        ></v-checkbox>
        <v-row align="center">
          <uploadfile  @getFileName = "getFileName" :data = "uploadinfo1"/>
        </v-row>
        <v-overflow-btn
            v-model="CurrentForm.Inflator"
            dens
            :disabled="enabled"
            class="my-2"
            :items="dropdown_font"
            menu-props="bottom"
            label="Please select the inflator in your ESR"
            target="#dropdown-example-1"
          ></v-overflow-btn>
        </v-card-text>
      </v-card>  
</template>>

<script>
import {mapState} from 'vuex';
export default {
      data: () => ({
        enabled: false,
        dropdown_font: ["ADP1.3B_MP","ADP1.3B_HP","ADPS-1.5_210kPa_5ms"],
        uploadinfo1 : {
              disabled:false,
              fileList : [],
              inputlabel: 'Inflator',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".pdf",
              FileRules:[
              v => !!v || 'Required',
                  ],
              Hint : "EX11_Cushion_V1.pdf",
        },
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