<template>
   <v-app>
    <v-main>

       <UploadFile/>


    </v-main>
  </v-app>
</template>

<script>

import UploadFile from './components/UploadFile/index';



export default {
  name: 'App',

  components: {


    UploadFile,
  },

  data: () => ({
    //
  }),
};
</script>
