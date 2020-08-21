<!-- ValidateForm -->
<template>
  <v-card dense>
   <v-card-title >
      CaseInfo
  </v-card-title>

  <v-card-text>
      <v-row > 
        <v-col 
          cols='12'
          md='4'
          >
          <v-checkbox v-model="CurrentForm.Case[0]" label="UL-HT" ></v-checkbox>
          <v-checkbox v-model="CurrentForm.Case[1]" label="UL-RT"></v-checkbox>
          <v-checkbox v-model="CurrentForm.Case[2]" label="UL-LT"></v-checkbox>
        </v-col>
        <v-col 
          cols='12'
          md='4'
          >
          <v-checkbox v-model="CurrentForm.Case[3]" label="NL-HT"></v-checkbox>
          <v-checkbox v-model="CurrentForm.Case[4]" label="NL-RT"></v-checkbox>
          <v-checkbox v-model="CurrentForm.Case[5]" label="NL-LT"></v-checkbox>
        </v-col>
        <v-col 
          cols='12'
          md='4'
          >
          <v-checkbox disabled v-model="CurrentForm.Case[6]" label="LL-HT"></v-checkbox>
          <v-checkbox disabled v-model="CurrentForm.Case[7]" label="LL-RT"></v-checkbox>
          <v-checkbox v-model="CurrentForm.Case[8]" label="LL-LT"></v-checkbox>
        </v-col>
      </v-row>

 

      
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
    }),
    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },
    methods:{
      aa(){
        console.log(this.CurrentForm.Case)
      }
   }
  }
</script>