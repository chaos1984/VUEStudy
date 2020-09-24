<template>
      <v-card height = "430px">
        <v-card-title>
          Inflator
        </v-card-title>
        <v-card-text>
        <v-checkbox
          v-model="enabled"
          hide-details
          class="shrink ma-5 mt-0"
          label="New Inflator"
       ></v-checkbox>
        <v-card
        :disabled="!enabled">
          <uploadfile  @getFileName = "getFileName" :data = "InflatorFile"/>
       </v-card>
        <v-overflow-btn
            v-model="CurrentForm.Inflator"
            :disabled="!enabled"
            class="mt-8"
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
        InflatorFile : {
              name : "InflatorFile",
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
              Hint : "EX11_Inflator_V1.pdf",
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
      getFileName(uploadinfo){
          this._data[uploadinfo.name] =uploadinfo
          this.CurrentForm[uploadinfo.name] = uploadinfo.fileList[0].name
      },
      initialization(){
        if (this.CurrentForm.InflatorFile != ""){
          this.InflatorFile.fileList=[{name:this.CurrentForm.InflatorFile,url:''}];
        }
      }
   }
}
</script>