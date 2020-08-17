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
            v-model="ESRNumber"
            :rules="nameRules"
            :counter="50"
            label="ESR"
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
            label="Requester name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="TeamName"
            :rules="TeamnameRules"
            label="Team name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="ProjectCode"
            :rules="ProjectCodeRules"
            label="ProjectCode"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="24"
          md="8"
        >
          <Datepick/>
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
        Datepick: () => import('../../DatePick'),
    },
    data: () => ({
      info : '',
      valid: false,
      ESRNumber: 'ESR-',
      PEName: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      TeamName: '',
      TeamnameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      ProjectCode:"",
      ProjectCodeRules :[
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ]
    }),
    computed:{
        isError:function(){
        if (this.ESRNumber != '' && this.PEName != '' && this.TeamName != ''){
            this.$store.commit('isNextStep')
            return false
        } else {
            this.$store.commit('noNextStep')
            return true
            }
         }
    },
    methods:{
    
   }
  }
</script>