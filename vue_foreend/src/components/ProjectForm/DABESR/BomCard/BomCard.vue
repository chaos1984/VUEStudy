<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BomInfo
  </v-card-title>

  <v-card-text>
      <v-file-input  multiple label="Upload the BOM FILE1"></v-file-input>  
      <v-file-input  multiple label="Upload the CAD FILE"></v-file-input>  
    </v-card-text>

  </v-card>  
    

</template>

<script>
  export default {
    name : 'BomInfo',
    components:{
       
    },
    data: () => ({
      enabled: false,
    }),
    methods:{
   }
  }
</script>