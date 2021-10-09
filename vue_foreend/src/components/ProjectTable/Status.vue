<template>
  <div style="margin: 20px">
    <v-stepper value="3">
      <v-stepper-header>
              
        <v-stepper-step step="1" :complete="steplist[0]" > Create </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="2" :complete="steplist[1]"> Meshing </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3" :complete="steplist[2]"> Simulation </v-stepper-step>
        <v-divider></v-divider>

        <v-stepper-step step="4" :complete="steplist[3]"> Close </v-stepper-step>
      </v-stepper-header>
    </v-stepper>
  </div>
</template>
<script>
export default {
  name: "status",
  components: {},
  data: () => {
    return {
        steplist : [true,true,true,false]
    };
  },
  mounted() {},
  methods: {},
};
</script>
<style>
</style>