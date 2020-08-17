<template>

  <v-card height="250px">
    <v-card-title>
    Cushion Information
    </v-card-title>
    <v-card-text>
      <v-checkbox
      v-model="enabled"
      hide-details
      class="shrink mr-2 mt-0"
      label="New Cushion"
      ></v-checkbox>
      <v-row align="center">
        <v-file-input :disabled="!enabled" multiple label="New cushion dwg file"></v-file-input>
        <v-file-input :disabled="!enabled" multiple label="New cushion folding file"></v-file-input>
      </v-row>
      <v-text-field
      :disabled="enabled"
      label= 'Please input your carryover cushion'
      >
      </v-text-field>
    </v-card-text>
  </v-card>
  
</template>>

<script>
export default {
      data: () => ({
      includeFiles: true,
      enabled: false,
    }),
}
</script>