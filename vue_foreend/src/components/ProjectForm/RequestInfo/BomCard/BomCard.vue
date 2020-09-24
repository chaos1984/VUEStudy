<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BOM Info
  </v-card-title>

  <v-card-text>

      <uploadfile @getFileName = "getFileName" :data = "BOMFile"/>
      <uploadfile @getFileName = "getFileName" :data = "CADFile"/>
      
      <!-- <v-btn color="primary" text @click="uploadFile">test</v-btn> -->
    </v-card-text>

  </v-card>


</template>

<script>
import {mapState} from 'vuex';
  export default {
    data: () => ({
        BOMFile : {
              name : "BOMFile",
              disabled:false,
              fileList : [],
              inputlabel: 'BOM FILE',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".xls",
              FileRules:[
              v => !!v || 'Required',
                  ],
              Hint : "EX11_BOM_V1.xls",
        },
        CADFile : {
              name : "CADFile",
              disabled:false,
              fileList : [],
              inputlabel: 'CATIA FILE',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".stp,.x_t,.CATPart",
              FileRules:[
                  v => !!v || 'Required',
                  ],
              Hint : "EX11_DABModule_V1.stp",
        },
    }),

    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    mounted () {
      this.initialization()
    },
    methods:{
      emitalert(){
           console.log(this.CurrentForm.BOMFile)
         },
      getFileName(uploadinfo){
          this._data[uploadinfo.name] =uploadinfo
          this.CurrentForm[uploadinfo.name] = uploadinfo.fileList[0].name
      },
      initialization(){
        if (this.CurrentForm.BOMFile != ""){
          this.BOMFile.fileList=[{name:this.CurrentForm.BOMFile,url:''}];
        }
        if (this.CurrentForm.CADFile != ""){
          this.CADFile.fileList=[{name:this.CurrentForm.CADFile,url:''}];
        }
      }
   }
  }
</script>