<template>

<v-card mx >
  <v-card-title>
      Cushion
  </v-card-title>
  <v-card-text>
    <v-checkbox
      
      v-model="enabled"
      hide-details
      class="shrink ma-5 mt-0"
      label="New Cushion"
      ></v-checkbox>
    <v-card
    dens
    :disabled="!enabled">
 
      <uploadfile @emitfilename = "getFileName" :data = "uploadinfo1"/>
    
      <uploadfile @emitfilename = "getFileName" :data = "uploadinfo2"/>


    </v-card >

    <v-text-field
      type = 'text'
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      
    >
    </v-text-field>
      </v-card-text>
  </v-card>  

  
</template>>

<script>
import {mapState} from 'vuex';
export default {
    data: () => ({
      uploadinfo1 : {
              disabled:false,
              fileList : [],
              btnlabel: 'Cushion part',
              label : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".pdf",
              FileRules:[
              v => !!v || 'Required',
                  ],
              Hint : "EX11_Cushion_V1.pdf",
        },
        uploadinfo2 : {
              disabled:false,
              fileList : [],
              btnlabel: 'Cushion Foled',
              label : 'upload',
              action : 'api/upload',
              filenum : 1,
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
        })
    },

    methods:{
      getFileName(data){
        console.log(data)
      }
   }
}
</script>