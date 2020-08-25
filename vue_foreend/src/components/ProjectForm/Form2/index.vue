<template>

<v-card>
  <v-card-title>
      Cushion
  </v-card-title>
  <v-card-text>
    <v-row align="center">
      <v-file-input 
        v-model="CurrentForm.CushiondwgFile" 
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
      ></v-file-input>
    </v-row>
    <v-text-field
      v-model="CurrentForm.OldCushion"
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
    name : 'DABESRInfo',
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
      }
   }
}
</script>