<template>

<v-card mx >
  <v-card-title>
      Cushion
  </v-card-title>
  <keep-alive>
  <v-card-text>
    <v-checkbox
      v-model="CurrentForm.CushionCarryoverflag"
      hide-details
      class="shrink ma-5 mt-0"
      label="New Cushion"
      @change = "validenable"
      ></v-checkbox>
    <v-card
    :disabled="!CurrentForm.CushionCarryoverflag"
    dens>
      <uploadfile  ref="child1" @getFileName = "getFileName" :data = "CushiondwgFile"/>
      <uploadfile ref="child2" @getFileName = "getFileName" :data = "CushionFoldFile"/>
    </v-card >

    <v-text-field
      v-model = "CurrentForm.CarryoverText"
      type = 'text'
      :disabled="CurrentForm.CushionCarryoverflag"
      label= 'Please input your carryover cushion'
      :rules = "InputRules"
    >
    </v-text-field>
    <v-row>
      <v-col mx="3px">
      <p>Cushion Mat.</p>
      <v-overflow-btn 
        :items="Cushionmat"
        label="*Select cushion mat"

        item-value="text"
        :rules="overflowbtnrules"
      >
      </v-overflow-btn>
      </v-col>
      <v-col mx="3px">
      <p>Cushion fold type</p>
      <v-overflow-btn 
        :items="Cushionfold"
        label="*Select cushion fold"

        item-value="text"
        :rules="overflowbtnrules"
      >
      </v-overflow-btn>
      </v-col>
    </v-row>
      </v-card-text>
      </keep-alive>
  </v-card>  

  
</template>>

<script>
import {mapState} from 'vuex';
export default {
    data: () => ({
        Cushionmat: ['470dtex','350dtex'],
        Cushionfold: ['DRR(Double Reverse Roll)','LC3(Compression Fold ALL Sides)','RC1(Roll Reverse fold foe the 6 and 12H Sides','RC2(Roll Reverse Fold for Only 12H Side'],
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
              v => !!v  || 'Required',
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
                  
                  ],
              Hint : "EX11_CushionFold_V1.pdf",
        },
      InputRules:[
                  
                  ],
      overflowbtnrules:[
                  
                  ],
      enabled: true,
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
        console.log(this.CurrentForm.CushionCarryover)
      },
      validenable(){
        if (this.CurrentForm.CushionCarryoverflag == false) {
            this.$refs.child1.getenable([])
            this.$refs.child2.getenable([])
            this.InputRules = [
              v => !!v || 'Required'
                ]
        } else if (this.CurrentForm.CushionCarryoverflag  == true) {
            this.$refs.child1.getenable([
                v => !!v || 'Required',
                // v => v.length <= 50 || 'Name must be less than 20 characters',
                // v => /[A-z]+$/.test(v)|| 'Must be a string',
                  ])
            this.$refs.child2.getenable([
                v => !!v || 'Required',
                // v => v.length <= 50 || 'Name must be less than 20 characters',
                // v => /[A-z]+$/.test(v)|| 'Must be a string',
                  ])
            this.InputRules = []
        
        }
      }
   }
}
</script>