<template>
      <v-card height = "249px">
        <v-card-title>
          Inflator
        </v-card-title>
        <v-card-text>
        <v-checkbox
          v-model="enabled"
          hide-details
          class="shrink mr-2 mt-0"
          label="New Inflator"
        ></v-checkbox>
        <v-row align="center">
          <v-file-input v-model="CurrentForm.InflatorFile" accept=".pdf" :disabled="!enabled" multiple label="New inflator file"></v-file-input>
        </v-row>
        <v-overflow-btn
            v-model="CurrentForm.Inflator"
            dens
            :disabled="enabled"
            class="my-2"
            :items="dropdown_font"
            menu-props="bottom"
            label="Please select the inflator in your ESR"
            target="#dropdown-example-1"
          ></v-overflow-btn>
        </v-card-text>
      </v-card>  
</template>>

<script>
import {mapState} from 'vuex';
export default {
      data: () => ({
        enabled: false,
        dropdown_font: ["ADP1.3B_MP","ADP1.3B_HP","ADPS-1.5_210kPa_5ms"],
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