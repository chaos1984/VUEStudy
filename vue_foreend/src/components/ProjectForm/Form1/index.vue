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
        cols="12"
        md="4">
      <v-menu
        ref="menu1"
        v-model="menu1"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="date1"
            label="Picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>

        <v-date-picker v-model="date1" @input="menu1 = false" no-title>
        </v-date-picker>
      </v-menu>
      </v-col>

      <v-col           
        cols="12"
        md="4">
      <v-menu
        ref="menu2"
        v-model="menu2"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="date2"
            label="Picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            :rules="[v => !!v || 'Required']"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>

        <v-date-picker 
        v-model="date2" 
        :min='date1' 
        no-title>
        </v-date-picker>
      </v-menu>
      </v-col>


      </v-row>

    </v-container>
        <v-alert
      :value = "validate"
      :dense = false
      outlined
      type="error"
    >
       Information is not complete! Please check!
       </v-alert>
       <!-- <NextBackbtn></NextBackbtn> -->
       <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      
      @click="validate"
    >
      Next
    </v-btn>
  </v-form>
</template>

<script>
  export default {
    name : 'projectform1',
    components:{
        // NextBackbtn: () => import('../NextBackbtn'),
    },
    data: () => ({
      info : '',
      valid: true,
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
      ],
      date1: new Date().toISOString().substr(0, 10),
      // date2: new Date().toISOString().substr(0, 10),


      menu1: false,
      menu2: false,
    }),
    computed:{
      },

    methods:{
    validate () {
        this.$store.commit('nextStep')
      },
   }
  }
</script>