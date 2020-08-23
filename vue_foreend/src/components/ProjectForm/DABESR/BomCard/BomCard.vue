<!-- ValidateForm -->
<template>
  <v-card height = "302px">
   <v-card-title >
      BomInfo
  </v-card-title>

  <v-card-text>
      <v-file-input 
        label="Upload the BOM FILE1"
        placeholder="Select a file"
        :rules="BomFileRules"
      ></v-file-input>  
      <v-file-input 
        label="Upload the CAD FILE"
        placeholder="Select a file"
        :rules="CADFileRules"
      ></v-file-input>  
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
      BomFileRules:[
        v => !!v || 'Required',
      ],
      CADFileRules:[
        v => !!v || 'Required',
      ]  
    }),
    methods:{
   }
  }
</script>