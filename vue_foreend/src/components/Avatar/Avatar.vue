<template>
  <v-container fluid style="height: 60px">
    <v-row justify="center">
      <v-menu bottom min-width="200px" rounded offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-avatar color="brown" size="48">
              <img
        src="/static/img/Head.png"
        alt="Bear"
      >
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar color="brown" size="48">
              <img
        src="/static/img/Head.png"
        alt="Bear"
      >
            </v-avatar>
              <h3>{{ User.Name }}</h3>
              <p class="text-caption mt-1">
                {{User.Email }}
              </p>
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
  mounted () {
    this.init();
  },
  computed: {
    ...mapState({ User: (state) => state.User }),
  },
  methods: {
    init() {
      // console.log("this.User.Email");
      // console.log(this.User);
      this.user.initials = this.User.Name
    }
  },
};
</script>

