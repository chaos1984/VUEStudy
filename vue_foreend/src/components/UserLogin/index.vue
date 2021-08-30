<template>
  <div>
    <div
      class="login-wrapper"
      :style="{
        background:
          'url(' +
          require('../../../public/static/img/bg1.jpg') +
          ') no-repeat center center',
        'background-size': '100% 100%',
      }"
    >
      <div id="">
        <!-- <p class="title">Sign In</p> -->
        <el-form
          :model="User"
          status-icon
          ref="User"
          label-width="0px"
          class="login-form-wrapper"
        >
          <el-form-item prop="User">
            <el-autocomplete
              v-model="userlogin.name"
              :fetch-suggestions="querySearch"
              placeholder="User name"
              @select="handleSelect"
              style="width: 100%"
              clearable
            ></el-autocomplete>
          </el-form-item>

          <el-form-item prop="Password">
            <el-input
              type="password"
              v-model="userlogin.password"
              auto-complete="off"
              placeholder="Password"
              show-password
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-row :gutter="20">
              <el-col :span="12">
                <el-button type="primary" @click="login('User')" style="width: 100%"
                  >Login</el-button
                >
              </el-col>
              <el-col :span="12">
                <el-button type="primary" @click="Register" style="width: 100%">
                  To Register</el-button
                >
              </el-col>
            </el-row>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "Login",

  data() {
    return {
      user_value: [],
      userlogin:{
        name :"",
        password:""
      },
      userinfo:{}
    };
  },
  computed: {
    ...mapState({ User: (state) => state.User }),
  },
  mounted() {
    this.getDatafromDB();
  },
  methods: {
    getDatafromDB() {
      this.$axios.get("/api/getusers").then(
        (response) => {
          var user_list = response.data;
          // console.log( user_list.length )
          for (var i = 0; i < user_list.length; i++) {
            // console.log(user_list[i].Name)
            this.user_value.push({ value: String(user_list[i].Name),Email: String(user_list[i].Email),Priority: String(user_list[i].Priority)});
            // this.user_value.push({ value: String(user_list[i].Name),priority: String(user_list[i].Priority)});
          }
        },
        (error) => {
          console.log(error);
        }
        // this.data4fig = this.ESRTable
      );
    },
    handleSelect(item) {
      // console.log("item")
      this.User.Name = item.value
      this.User.Email = item.Email
      this.User.Priority = item.Priority
      // console.log(item);
    },
    querySearch(queryString, cb) {
      var users = this.user_value;
      var results = queryString ? users.filter(this.createFilter(queryString)) : users;

      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (user) => {
        return user.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0;
      };
    },


    login(formName) {
      console.log(formName);
      this.$axios
        .post("/api/login", {
          name: this.userlogin.name,
          password: this.userlogin.password,
        })
        .then(
          (response) => {
            // console.log(response.data.token);
            if (response.data.token) {
              window.sessionStorage.setItem("token", response.data.token);
              // this.User.Name = response.data.name
              // this.User = response.data
              this.User = this.user_value
              this.$router.push("/Layout");

            } else {
              this.$message({
                showClose: true,
                message: response.data.msg,
                type: "error",
          });
            }
            // console.log(response.data[1])
            //       this.$router.push({
            //   path: response.data[0],
            // });
          },
          (error) => {
            console.log(error);
          }
        );
    },
    // <!--进入登录页-->
    Register() {
      this.$router.push({
        path: "/Register",
      });
    },
  },
};
</script>

<style scoped>
.login-wrapper {
  width: 100%;
  height: 1000px;

  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.login-form-wrapper {
  background: rgba(126, 127, 128, 0.267);
  background-size: cover;
  border-radius: 10px;
  width: 400px;
  height: 3d20px;
  overflow: hidden;
  padding-top: 40px;
  padding-left: 40px;
  padding-right: 40px;
  line-height: 1500px;
}
</style>
