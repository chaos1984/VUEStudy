<template>

<v-card mx >
  <v-card-title>
      Cushion
  </v-card-title>
  <keep-alive>
  <v-card-text>
    <v-checkbox
      
      v-model="enabled"
      hide-details
      class="shrink ma-5 mt-0"
      label="New Cushion"
      ></v-checkbox>
    <v-card
    :disabled="!enabled">
      <uploadfile  @getFileName = "getFileName" :data = "CushiondwgFile"/>
      <uploadfile  @getFileName = "getFileName" :data = "CushionFoldFile"/>
    </v-card >

    <v-text-field
      type = 'text'
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      
    >
    </v-text-field>
      </v-card-text>
      </keep-alive>
  </v-card>  

  
</template>>

<script>
import {mapState} from 'vuex';
export default {
    data: () => ({
        CushiondwgFile : {
              name :'CushiondwgFile',
              disabled:false,
              fileList : [],
              inputlabel: 'Cushion part',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".pdf",
              FileRules:[
              v => !!v || 'Required',
                  ],
              Hint : "EX11_Cushion_V1.pdf",
        },
        CushionFoldFile : {
              name :'CushionFoldFile',
              disabled:false,
              fileList : [],
              inputlabel: 'Cushion Foled',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 2,
              accepttype : ".stp,.x_t,.CatiaPart",
              FileRules:[
                  v => !!v || 'Required',
                  ],
              Hint : "EX11_CushionFold_V1.pdf",
        },
      enabled: false,
    }),
    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        }),

    },
    mounted () {
      this.initialization()
    },
    methods:{
      getFileName(uploadinfo){
          this._data[uploadinfo.name] =uploadinfo
          this.CurrentForm[uploadinfo.name] = uploadinfo.fileList[0].name
      },
      initialization(){
        if (this.CurrentForm.CushiondwgFile != ""){
          this.CushiondwgFile.fileList=[{name:this.CurrentForm.CushiondwgFile,url:''}];
        }
        if (this.CurrentForm.CushionFoldFile != ""){
          this.CushionFoldFile.fileList=[{name:this.CurrentForm.CushionFoldFile,url:''}];
        }
      }
   }
}
</script>