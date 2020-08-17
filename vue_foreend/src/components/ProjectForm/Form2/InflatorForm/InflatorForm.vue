<template>

  <v-card height="250px">
    <v-card-title>
    Inflator Information
    </v-card-title>
    <v-card-text>
      <v-checkbox
      v-model="enabled"
      hide-details
      class="shrink mr-2 mt-0"
      label="New Inflator"
      ></v-checkbox>
      <v-row align="center">
        <v-file-input :disabled="!enabled" multiple label="New inflator file"></v-file-input>
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
    </v-card-text>
  </v-card>
  
</template>>

<script>
export default {
      data: () => ({
      includeFiles: true,
      enabled: false,
      dropdown_font: ["ADP1.3B_MP","ADP1.3B_HP","ADPS-1.5_210kPa_5ms"],
    }),
}
</script>