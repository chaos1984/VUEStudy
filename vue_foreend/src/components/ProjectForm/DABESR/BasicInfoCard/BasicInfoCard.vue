<template>
    <v-card >
  <v-card-title >
      BasicInfo
  </v-card-title>
  <v-card-text>
      <v-row>
          <v-text-field
            v-model="CurrentForm.ESRNumber"
            :rules="nameRules"
            :counter="50"
            label="ESR"
            required
          ></v-text-field>
  

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
 
   }
  }
</script>