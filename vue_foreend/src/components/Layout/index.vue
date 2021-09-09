<!-- Layout -->
<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app left color="cyan" dark>
      <v-list dense>
        <v-row justify="space-around">
          <Avatar />
          <h3>{{ User.Name }}</h3>
          
        </v-row>
        <v-divider class="my-3"></v-divider>
        <template v-for="item in ListTerm">
          <v-row v-if="item.heading" :key="item.id" align="center">
            <v-col cols="6">
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
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
            @click="callEvent(item.action)"
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
    <v-app-bar app color="cyan" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Autoliv Lin & AI</v-toolbar-title>
    </v-app-bar>
    <!-- 操作区域 -->
    <v-main class="d-flex pa-2">
      <!-- <appmain/> -->
      <component :is="currentvue" v-if="hackReset"> </component>

      <!-- <v-banner >
          <p >
          Beta Version
          </p>
      </v-banner> -->
    </v-main>
    <!-- footer设置 -->
    <v-footer color="cyan" padless>
      <v-row justify="center" no-gutters>
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
        <v-col class="cyan lighten-1 py-4 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} — <strong>Autoliv CTC</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Layout",
  beforeRouteEnter(to, from, next) {
    // ...
    // console.log(this.User)
    const tokenStr = window.sessionStorage.getItem("token");

    if (!tokenStr) {
      // console.log("/UserLogin")
      alert("Please login first");
      next("/UserLogin");
    } else {
      console.log("/Layout");
      next();
    }
  },
  components: {
    // Stepper: () => import("@/components/Stepper"),
    ProjectTable: () => import("@/components/ProjectTable"),
    SlideShow: () => import("@/components/SlideShow/SlideShow"),
    Mat: () => import("@/components/Echart/Mat"),
    Inf: () => import("@/components/Echart/Inf"),
    MatPage: () => import("@/components/MatPage/MatPage"),

    test: () => import("@/components/TestData/TestData"),
    DABAI: () => import("@/components/DABAI/DABAI"),
    Avatar: () => import("@/components/Avatar/Avatar"),
    // DABSVM: () => import("@/components/DABSVM/DABSVM"),
  },

  data: () => ({
    Username: "",
    infor: "No infor",
    currentvue: "",
    drawer: null,
    hackReset: true,
    links: ["Home", "About Us", "Team", "Services", "Contact Us"],
    ListTerm: [
      
      {
        id: 1,
        title: "DAB",
        action: "onESRinfo",
        icon: "mdi-steering",
      },
      { id: 2, title: "PAB", action: "onPAB", icon: "iconfont icon-qinang" },
      { id: 3, title: "Mat", action: "onCoverMat", icon: "iconfont icon-shouyetubiao-09" },
      // {
      //   id: 4,
      //   title: "Cover Material",
      //   action: "",
      //   icon: "iconfont icon-shouyetubiao-09",
      //   model: false,
      //   children: [
      //     { title: "TA4003BE", action: "onMatPage" },
      //     { title: "TT1081B", action: "onMatPage" },
      //     { title: "TT990", action: "onMatPage" },
      //     { title: "CAE_capability", action: "onMatPage" },
      //     { title: "Common material comparison", action: "onCoverMat" },
      //   ],
      // },
      { id: 4, title: "Inflator", action: "onInf", icon: "mdi-bomb" },

      { id: 5, title: "Post View", action: "onTest", icon: "el-icon-video-camera-solid" },
      {
        id: 6,
        title: "AI Predction",
        action: "onDABAI",
        icon: "mdi-robot",
      },
      { id: 7, title: "Lin & AI Help", action: "FrontPage", icon: "mdi-book" },
    ],
  }),

  computed: {
    ...mapState({ CurrentForm: (state) => state.form }),
    ...mapState({ User: (state) => state.User }),
  },
  created() {
    this.currentvue = "ProjectTable";
  },
  methods: {
    FrontPage() {
      this.currentvue = "SlideShow";
    },
    onDAB() {
      this.currentvue = "Stepper";
    },
    onPAB() {
     this.$message({
            showClose: true,
            message: "The web site is still under construction, please try later. ",
            type: "error",
          });
    },
    onESRinfo() {
      this.currentvue = "ProjectTable";
    },
    onCoverMat() {
      this.currentvue = "Mat";
      // router.push({'Echart'})
    },
    onInf() {
      this.currentvue = "Inf";
      // router.push({'Echart'})
    },

    onTest() {
      this.currentvue = "test";
    },
    onMatPage() {
      this.CurrentForm.CurrentMatPage = event.currentTarget.innerText;
      console.log(this.CurrentForm.CurrentMatPage);
      this.hackReset = false;
      this.$nextTick(() => {
        this.hackReset = true;
      });
      this.currentvue = "MatPage";
    },
    onDABAI() {
      this.currentvue = "DABAI";
    },
    // onDABSVM() {
    //   this.currentvue = "DABSVM";
    // },
    callEvent(e) {
      this[e]();
    },
  },
};
</script>
