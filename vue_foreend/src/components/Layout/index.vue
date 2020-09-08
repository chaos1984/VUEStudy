<!-- Layout -->
<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      left
    >
    
      <v-list dense>
          <template v-for="item in ListTerm">
            <v-row
              v-if="item.heading"
              :key="item.id"
              align="center"
            >
              <v-col cols="6">
                <v-subheader v-if="item.heading">
                  {{ item.heading }}
                </v-subheader>
              </v-col>
              <v-col
                cols="6"
                class="text-center"
              >
                <a
                  href="#!"
                  class="body-2 black--text"
                >EDIT</a>
              </v-col>
            </v-row>
            <v-list-group
              v-else-if="item.children"
              :key="item.title"
              v-model="item.model"
              :prepend-icon="item.model ? item.icon : item.icon"
              append-icon=""
            >
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ item.title }}
                  </v-list-item-title>
                </v-list-item-content>
              </template>
              <v-list-item
                v-for="(child, i) in item.children"
                :key="i"
                link
                @click="callEvent(child.action)"
              >
                <v-list-item-action v-if="child.icon">
                  <v-icon>{{ child.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>
                    {{ child.title }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
            <v-list-item
              v-else
              :key="item.id"
              link
              @click =  callEvent(item.action)
            >
              <v-list-item-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  {{ item.title }}
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
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
        Echart: () => import('@/components/Echart/Echart'),
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
        {id:1,title:'HOME',action:'FrontPage',icon:"iconfont icon-home"},
        {id:2,title:'DAB',action:'onDAB',icon:"iconfont icon-fangxiangpan"},
        {id:3,title:'PAB',action:'onPAB',icon:"iconfont icon-qinang"},
        {id:4,title:'Cover Material',action:'',icon:"iconfont icon-shouyetubiao-09",model: false,
        children: [
          { title: 'TA4003BE',action:'' },
          { title: 'TT1081B',action:''  },
          { title: 'TT990',action:'' },
          { title: 'Common material comparison',action:'onCoverMat' },
        ],},
        {id:5,title:'Inflator',action:'onESRinfo',icon:"iconfont icon-kaifangshengtai-icon256"}
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
      onCoverMat(){
          this.currentvue = 'Echart';
      },
      callEvent(e){
        this[e]()
      }
      
    }
  }
</script>
