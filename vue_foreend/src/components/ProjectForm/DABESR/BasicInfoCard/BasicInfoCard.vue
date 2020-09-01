<template>
    <v-card >
  <v-card-title >
      BasicInfo
  </v-card-title>
  <v-card-text>
      <v-row>
         <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="CurrentForm.ESRNumber"
            :rules="ESRRules"
            :counter="6"
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
            :counter="20"
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
            :counter="20"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            validate-on-blur
            v-model="CurrentForm.ProjectCode"
            :rules="ProjectCodeRules"
            label="ProjectCode(AFIS)"
            :counter="5"
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
            label="ESR created date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>

        <v-date-picker 
        v-model="CurrentForm.date1" 
        @input="menu1 = false" 
        :min='today'
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
            placeholder="Please select a  delivery date"
            label="Preferred delivery date"
            v-model="CurrentForm.date2"
            prepend-icon="mdi-calendar"
            readonly
            :rules =  "Date2Rules"
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
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
      </v-col >
    </v-row>
    </v-card-text>
  </v-card>  
</template>
<script>
import {mapState} from 'vuex';
export default {
    name : 'BasicInfo',
    data: () => ({
      today: new Date().toISOString().substr(0, 10),
      info : '',
      valid: true,

      ESRRules: [
        v => !!v || 'Required',
        v => v.length == 6 || 'ESR No. must be six-digit',
        v => /[0-9]+$/.test(v)|| 'Must be a number'
      ],

      nameRules: [
        v => !!v || 'Required',
        v => v.length <= 20 || 'Name must be less than 20 characters',
        v => /[A-z]+$/.test(v)|| 'Must be a string'
      ],
      TeamnameRules: [
        v => !!v || 'Required',
        v => v.length <= 20 || 'Name must be less than 20 characters',
        v => /[A-z]+$/.test(v)|| 'Must be a string'
      ],

      ProjectCodeRules :[
        v => !!v || 'Required',
        v => v.length == 5 || 'AFIS No. must be five-digit',
        v => /[0-9]+$/.test(v)|| 'Must be a number'
      ],
      Date2Rules:[
        v => !!v || 'Date is required',
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
 
   }
  }
</script>