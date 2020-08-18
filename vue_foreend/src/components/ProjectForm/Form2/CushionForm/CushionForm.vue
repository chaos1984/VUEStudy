<template>

  <v-card height="250px">

    <v-card-title>
    Cushion Information
    </v-card-title>
    <v-card-text>
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
    </v-card-text>
  </v-card>
  
</template>>

<script>
export default {
    data: () => ({
      includeFiles: true,
      enabled: false,
      OldCushion:'',
      CushiondwgFile:'',
      CushionFoldFile:''
    }),
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