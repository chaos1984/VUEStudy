<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      left
    >
      <v-list dense>
        <v-list-item @click='DAB'>
          <v-list-item-action>
            <v-icon >mdi-home</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>DAB</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click='PAB'>
          <v-list-item-action>
            <v-icon>mdi-email</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>PAB</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    
<!-- bar设置 -->
    <v-app-bar
      app
      color="cyan"
      dark
    >
      <v-toolbar-title>Autoliv ESR Submit</v-toolbar-title>

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
<!-- 操作区域 -->
    <v-main fluid>
    <!-- <appmain/> -->
    <component :is="currentvue"></component>
    </v-main>
<!-- footer设置 -->
    <v-footer
    color="cyan"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="cyan lighten-1 py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-row>
  </v-footer>
  </v-app>
</template>

<script>
  export default {
    name: 'Layout',

    components:{
        Stepper: () => import('@/components/Stepper'),
        ProjectTable: () => import('@/components/ProjectTable'),
    },
    props: {
      source: String,
    },
    data: () => ({
      currentvue:'',
      drawer: null,
      links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Contact Us',
      ],
    }),
    methods:{
      DAB(){
         this.currentvue = 'Stepper';
         },
      PAB(){
         this.currentvue = 'ProjectTable';
      }
    }
  }
</script>
