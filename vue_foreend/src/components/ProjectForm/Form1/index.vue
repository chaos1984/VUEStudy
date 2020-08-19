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
            v-model="CurrentForm.ESRNumber"
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
            v-model="CurrentForm.PEName"
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
            v-model="CurrentForm.TeamName"
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
            v-model="CurrentForm.ProjectCode"
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
            v-model="CurrentForm.date1"
            label="Picker in menu"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>

        <v-date-picker 
        v-model="CurrentForm.date1" 
        @input="menu1 = false" 
        no-title>
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
            v-model="CurrentForm.date2"
            prepend-icon="mdi-calendar"
            readonly
            :rules =  "Date1Rules"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>

        <v-date-picker 
        v-model="CurrentForm.date2" 
        @input="menu2 = false" 
        :min='CurrentForm.date1' 
        no-title>
        </v-date-picker>
      </v-menu>
      </v-col>


      </v-row>

    </v-container>
        <!-- <v-alert
      :value = "validate"
      :dense = false
      outlined
      type="error"
    >
       Information is not complete! Please check!
       </v-alert> -->
       <!-- <NextBackbtn></NextBackbtn> -->
       <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      
      @click="validate"
    >
      Next
    </v-btn>
    <v-btn class= "mx-5"
      color="primary"
      @click="onBackStep"
      >
      Back
    </v-btn>
  </v-form>
</template>

<script>
import {mapState} from 'vuex';
  export default {
    name : 'projectform1',
    components:{
        // NextBackbtn: () => import('../NextBackbtn'),
    },
    data: () => ({
      
      info : '',
      valid: true,

      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      TeamnameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],

      ProjectCodeRules :[
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      // date2: new Date().toISOString().substr(0, 10),
      Date1Rules:[
        v => !!v || 'Name is required',
      ],
      menu1: false,
      menu2: false,
    }),
    computed:{
      ...mapState({
        CurrentForm : state => state.form,
        })
      },

    methods:{
    validate () {
        this.$store.commit('nextStep')
      },
    onBackStep(){
          this.$store.commit('backStep')
      },  
   }
  }
</script>