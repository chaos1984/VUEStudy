<!-- Layout -->
<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      left
    >
      <v-list dense>
        <v-list-item 
          v-for="term in ListTerm"
          :key=term.id
          @click= callEvent(term.action)>
        <v-list-item-action>
            <v-icon >{{term.icon}}</v-icon>
        </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>{{term.action}}</v-list-item-title>
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
      

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Autoliv ESR Request</v-toolbar-title>
    </v-app-bar>
<!-- 操作区域 -->
    <v-main  class="d-flex pa-2">
    <!-- <appmain/> -->
    <component :is="currentvue" ></component>
    
      <v-banner >
          <p >
          Beta Version
          </p>
      </v-banner>
  
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
        {{ new Date().getFullYear() }} — <strong>Autoliv CTC</strong>
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
        SlideShow: () => import('@/components/SlideShow/SlideShow'),
    },
 

    data: () => ({
      infor:'No infor',      
      currentvue:'',
      drawer: null,
      links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Contact Us',
      ],
      ListTerm:[
        {id:1,name:'DAB',action:'onDAB',icon:"mdi-home"},
        {id:2,name:'PAB',action:'onPAB',icon:"mdi-cake"},
        {id:3,name:'Cover Material',action:'onESRinfo',icon:"mdi-handyman"},
        {id:4,name:'Inflator',action:'onESRinfo',icon:""}
      ],
    }),
    mounted(){
      this.FrontPage()
    },
    methods:{
      FrontPage(){
        this.currentvue = 'SlideShow';
      },
      onDAB(){
         this.currentvue = 'Stepper';
         },
      onPAB(){
         console.log("PAB")
      },
      onESRinfo(){
         this.currentvue = 'ProjectTable';
         },
      callEvent(e){
        this[e]()
      }
      
    }
  }
</script>
