<!-- ValidateForm -->
<template>
  <v-card>
   <v-card-title >
      CaseInfo1
  </v-card-title>

  <v-card-text>
 
 
    <row>

      <v-col
      cols="12"
      md="6"
      >
      
      <v-checkbox v-model="CurrentForm.Case[1]" label="UL-HT"></v-checkbox>
 
      </v-col>
    </row>

      
  </v-card-text>

  </v-card>  
    

</template>

<script>
import {mapState} from 'vuex';
  export default {
    name : 'BomInfo',
    components:{
       
    },
    data: () => ({
      enabled: false,
      case : ['UL_HT','UL_LT']
    }),
    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    methods:{
   }
  }
</script>