<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="ProjectName"
            :rules="nameRules"
            :counter="50"
            label="Project"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="PEName"
            :rules="nameRules"
            :counter="50"
            label="PE"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-col>
      </v-row>

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
      info : '',
      valid: false,
      ProjectName: '',
      PEName: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
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
           console.log(this.info)
           this.$store.commit('edit',this.info)
       } else {
          this.getalert()
       }
     },
   }
  }
</script>