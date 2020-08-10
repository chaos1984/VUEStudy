<template>
  <v-container class="grey lighten-5">
    <v-row
      v-for="n in 1"
      :key="n"
      :class="n === 1 ? 'mb-6' : ''"
      no-gutters
    >
      <v-col
        v-for="k in n + 1"
        :key="k"
      >
        <v-card
          class="pa-2"
          outlined
          tile
        >
          <HelloWorld1/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HelloWorld1 from '../components/HelloWorld1';
import Echart from '../components/Echart';

  export default {
    name: 'app',
    components: {
    HelloWorld1,
	Echart,
  },
    data: () => ({
      drawer: null,
    }),
  }
</script>