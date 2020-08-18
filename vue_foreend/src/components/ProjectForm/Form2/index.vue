<template>

  <v-form v-model="valid">
    <v-container>
      <v-checkbox
      v-model="enabled"
      hide-details
      class="shrink mr-2 mt-0"
      label="New Cushion"
      ></v-checkbox>
      <v-row align="center">
        <v-file-input v-model = "CushiondwgFile" accept=".dwg" :disabled="!enabled" multiple label="Cushion dwg file"></v-file-input>
        <v-file-input v-model = "CushionFoldFile" accept=".pdf" :disabled="!enabled" multiple label="New cushion folding file"></v-file-input>
      </v-row>
      <v-text-field
      v-model="OldCushion"
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      >
      </v-text-field>
    </v-container> 
    <v-btn
      :disabled="!valid"
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
export default {
    data: () => ({
      valid:'false',
      includeFiles: true,
      enabled: false,
      OldCushion:'',
      CushiondwgFile:'',
      CushionFoldFile:''
    }),
    methods:{
      validate () {
        this.$store.commit('nextStep')
      },
      onBackStep(){
          this.$store.commit('backStep')
      },
   }
// computed:{
//     isError:function(){
//       if (this.enabled  === false && this.OldCushion != ''){
//         this.$store.commit('isNextStep')
//         return true
//     } else if (this.enabled === true &&  this.CushiondwgFile != '' && this.CushionFoldFile !=''){
//         this.$store.commit('isNextStep')
//         return true
//         } else {
//           return 0
//         }
//       },
// }
}
</script>