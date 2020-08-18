<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-container>
      <v-file-input  multiple label="Upload the BOM FILE1"></v-file-input>  
      <v-file-input  multiple label="Upload the CAD FILE"></v-file-input>  
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
</template>

<script>
  export default {
    name : 'BomCushion',
    components:{
       
    },
    data: () => ({
      valid:'true',
      includeFiles: true,
      enabled: false,
    }),
    methods:{
      validate () {
        this.$store.commit('nextStep')
      },
      onBackStep(){
          this.$store.commit('backStep')
      },
   }
  }
</script>