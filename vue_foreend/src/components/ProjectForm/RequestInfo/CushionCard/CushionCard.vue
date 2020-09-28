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
      @change = "validenable"
      ></v-checkbox>
    <v-card
    :disabled="!enabled">
      <uploadfile  ref="child1" @getFileName = "getFileName" :data = "CushiondwgFile"/>
      <uploadfile ref="child2" @getFileName = "getFileName" :data = "CushionFoldFile"/>
    </v-card >

    <v-text-field
      type = 'text'
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      :rules = "InputRules"
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
                  v => !!v || 'Required',
                  ],
              Hint : "EX11_CushionFold_V1.pdf",
        },
      InputRules:[
                  v => !!v || 'Required',
                  ],
      enabled: true
    }),
    // watch: {
    //   enable(newValue, oldValue) {
    //     if (newValue == false) {
    //         this.$res.child1.getenable("")
    //         this.$res.child2.getenable("")
    //         this.InputRules = [
    //             v => !!v || 'Required',
    //             v => v.length <= 50 || 'Name must be less than 20 characters',
    //             v => /[A-z]+$/.test(v)|| 'Must be a string',
    //             ]
    //     } else if (newValue == true) {
    //         this.$res.child1.getenable([
    //               v => !!v || 'Required',
    //               ])
    //         this.$res.child1.getenable([
    //               v => !!v || 'Required',
    //               ])
    //         this.InputRules = ""
    //     console.log(oldValue)
    //     }
    //   }
    // },
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
      },
      validenable(){
        if (this.enabled == false) {
            this.$refs.child1.getenable("")
            this.$refs.child2.getenable("")
            this.InputRules = [
                v => !!v || 'Required',
                v => v.length <= 50 || 'Name must be less than 20 characters',
                v => /[A-z]+$/.test(v)|| 'Must be a string',
                ]
        } else if (this.enabled  == true) {
            this.$refs.child1.getenable([
                  v => !!v || 'Required',
                  ])
            this.$refs.child1.getenable([
                  v => !!v || 'Required',
                  ])
            this.InputRules = ""
        
        }
      }
   }
}
</script>