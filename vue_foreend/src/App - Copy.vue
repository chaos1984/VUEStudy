<template>
   <v-app>
    <v-main>
       <ProjectTable/>
       <UploadFile/>
      <!-- <Toolbar/> -->
      <Calc/>
    </v-main>
  </v-app>
</template>

<script>
import ProjectTable from './components/ProjectTable/ProjectTable';
import UploadFile from './components/UploadFile/index';
// import Toolbar from './components/Toolbar';
import Calc from './components/Calc';


export default {
  name: 'App',

  components: {
   ProjectTable,
   // Toolbar,
    Calc,
    UploadFile,
  },

  data: () => ({
    //
  }),
};
</script>
