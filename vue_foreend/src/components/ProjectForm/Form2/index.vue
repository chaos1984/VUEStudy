<template>

<v-form >
  <v-container>
    <v-checkbox
        v-model="enabled"
        hide-details
        class="shrink mr-2 mt-0"
        label="New Cushion"
        @change="onClearData"
    ></v-checkbox>
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
    </v-container> 
    <v-btn
      :disabled="isError"
      color="success"
      class="mr-4"
      
      @click="validate"
    >
      Next
    </v-btn>
    <v-btn class= "mx-5"
      color="primary"
      @click="onBackStep"
      >
      Back
    </v-btn>
</v-form>
  
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
      }
   }
}
</script>