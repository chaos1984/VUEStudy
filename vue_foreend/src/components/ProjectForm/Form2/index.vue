<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-container fluid="true">
      <v-row>
        <v-col
          flex
          cols="12"
          md="6"
        >
        
        <CushionForm/>
        </v-col>

        <v-col
          flex
          cols="12"
          md="6"
        >
        <InflatorForm/>
        
        </v-col>
      </v-row>
    </v-container>
        <v-alert
      :value = "isError"
      :dense = false
      outlined
      type="error"
    >
       Information is not complete! Please check!
       </v-alert>
       <NextBackbtn></NextBackbtn>
  </v-form>
</template>

<script>
  export default {
    name : 'projectform',
    components:{
        NextBackbtn: () => import('../NextBackbtn'),
        CushionForm: () => import('./CushionForm/CushionForm'),
        InflatorForm: () => import('./InflatorForm/InflatorForm')
    },

    computed:{
        isError:function(){
        if (this.ProjectName != '' && this.PEName != '' && this.email != ''){
            this.$store.commit('isNextStep')
            return false
        } else {
            this.$store.commit('noNextStep')
            return true
            }
         }
    },
     mounted() {
      this.$store.commit('noNextStep');
  },
    methods:{
     
   }
  }
</script>