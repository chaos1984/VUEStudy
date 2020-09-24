<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BOM Info
  </v-card-title>

  <v-card-text>

      <uploadfile @getFileName = "getFileName" :data = "uploadinfo1"/>
      <uploadfile @getFileName = "getFileName" :data = "uploadinfo2"/>
      
      <!-- <v-btn color="primary" text @click="uploadFile">test</v-btn> -->
    </v-card-text>

  </v-card>


</template>

<script>
import {mapState} from 'vuex';
  export default {
    data: () => ({
        uploadinfo1 : {
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
        uploadinfo2 : {
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
    methods:{
      emitalert(){
           console.log(this.CurrentForm.BOMFile)
         },
      getFileName(data){
            
            console.log("uploadfile:",data)
          return data
      }
   }
  }
</script>