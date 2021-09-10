<template>
  <v-container fluid style="height: 60px">
    <v-row justify="center">
      <v-menu bottom min-width="200px" rounded offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-avatar color="brown" size="48">
              <img src="/static/img/Head.png" alt="Bear" />
            </v-avatar>
          </v-btn>
        </template>

        <v-card width="280">
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar color="brown" size="48">
                <img src="/static/img/Head.png" alt="Bear" />
              </v-avatar>
              <h3>{{ User.Name }}</h3>
              <p class="text-caption mt-1">
                {{ User.Email }}
              </p>
              <el-row>
                <el-col :span="12">
                  <el-badge :value="200" :max="99">
                    <el-button size="small" @click="getProject"
                      >Project</el-button
                    >
                  </el-badge>
                </el-col>
                <el-col :span="12">
                  <el-badge :value="100" :max="10">
                    <el-button size="small" @click="getMessage"
                      >Message</el-button
                    >
                  </el-badge>
                </el-col>
              </el-row>
              <el-row>
                <el-col :span="24">
                  <el-button size="small" type="danger" @click="relogin" style="width:70%"
                    >Relogin</el-button
                  >
                </el-col>
              </el-row>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    user: {
      initials: "",
      fullName: "",
      email: "",
    },
  }),
  mounted() {
    this.init();
  },
  computed: {
    ...mapState({ User: (state) => state.User }),
  },
  methods: {
    init() {
      // console.log("this.User.Email");
      // console.log(this.User);
      this.user.initials = this.User.Name;
    },
    getProject() {
      console.log("getProject");
    },
    getMessage() {
      console.log("getMessage");
    },
    relogin() {
      this.$router.push({
        path: "/UserLogin",
      });
      location.reload();
    },
  },
};
</script>
