<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-container>
    

    </v-container>
        <v-alert
      :value = "isError"
      :dense =false
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
    name : 'projectform1',
    components:{
        NextBackbtn: () => import('../NextBackbtn'),
    },
    data: () => ({
      includeFiles: true,
      enabled: false,
    }),
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
    methods:{
     inforemit(){
       this.info = ''
       if (this.ProjectName != '' && this.PEName != '' && this.email != ''){
           this.info =  this.ProjectName + this.PEName + this.email
           this.$store.commit('edit',this.info)
       } else {
          this.getalert()
       }
     },
   }
  }
</script>