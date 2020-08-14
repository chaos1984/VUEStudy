<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-container>
      <v-card>
    <v-card-text>
      <v-row align="center">
        <v-checkbox
          v-model="includeFiles"
          hide-details
          class="shrink mr-2 mt-0"
        ></v-checkbox>
        <v-text-field label="Include files"></v-text-field>
      </v-row>
      <v-row align="center">
        <v-checkbox
          v-model="enabled"
          hide-details
          class="shrink mr-2 mt-0"
        ></v-checkbox>
        <v-text-field
          :disabled="!enabled"
          label="I only work if you check the box"
        ></v-text-field>
      </v-row>
    </v-card-text>
  </v-card>

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