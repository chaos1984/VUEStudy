<template>
  <v-form v-model="valid">
    <v-container>
      <v-checkbox
      v-model="enabled"
      hide-details
      class="shrink mr-2 mt-0"
      label="New Inflator"
      ></v-checkbox>
      <v-row align="center">
        <v-file-input accept=".pdf" :disabled="!enabled" multiple label="New inflator file"></v-file-input>
      </v-row>
      <v-overflow-btn
          dens
          :disabled="enabled"
          class="my-2"
          :items="dropdown_font"
          menu-props="bottom"
          label="Please select the inflator in your ESR"
          target="#dropdown-example-1"
        ></v-overflow-btn>
    </v-container>
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
</template>>

<script>
export default {
      data: () => ({
      valid:'false',
      includeFiles: true,
      enabled: false,
      dropdown_font: ["ADP1.3B_MP","ADP1.3B_HP","ADPS-1.5_210kPa_5ms"],
    }),
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