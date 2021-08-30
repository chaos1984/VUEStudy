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
      <div >
        <el-form
          :model="UserRegister"
          status-icon
          ref="UserRegister"
          label-width="0px"
          class="login-form-wrapper"
          :rules="rules"
        >

        <el-form-item prop="name" >
            <el-input
              v-model="UserRegister.name"
              auto-complete="off"
              placeholder="User name"
            ></el-input>
          </el-form-item>

          
        <el-form-item prop="email" >
            <el-input
              v-model="UserRegister.email"
              auto-complete="off"
              placeholder="Email"
            ></el-input>
          </el-form-item>

          <el-form-item prop="pass" >
            <el-input
              type="password"
              v-model="UserRegister.pass"
              auto-complete="off"
              placeholder="Password"
              show-password
            ></el-input>
          </el-form-item>

          <el-form-item prop="checkPass" >
            <el-input
              type="password"
              v-model="UserRegister.checkPass"
              auto-complete="off"
              placeholder="Password"
              show-password
            ></el-input>
          </el-form-item>
        <el-form-item>
          <el-row :gutter="20">
              <el-col :span="12">
          
            <el-button type="primary" @click="submitForm('UserRegister')" style="width: 100%"
              >Register</el-button
            >
            </el-col>
            
              <el-col :span="12">
                <el-button
                  type="primary"
                  @click="Login"
                  style="width: 100%"
                  >To Login</el-button
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
export default {
  data() {
     // <!--验证密码-->
     let validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("No empty"))
      } else if(value.length <6 )
      {
        callback(new Error("Password is too short"))
      } 
      else {
        if (this.UserRegister.checkPass !== "") {
          this.$refs.UserRegister.validateField("checkPass");
        }
        callback()
      }
    }
    // <!--二次验证密码-->
    let validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("No empty"));
      } else if (value !== this.UserRegister.pass) {
        callback(new Error("Two input password must be consistent!"));
      } else {
        callback();
      }
    };

     var checkEmail = (rule, value, callback) => {
    const mailReg = /^([a-zA-Z0-9_-])+.([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+.([a-zA-Z0-9_-])+/
    if (!value) {
      return callback(new Error('Autoliv E-mail adress'))
    }
    setTimeout(() => {
      if (mailReg.test(value)) {
        callback()
      } else {
        callback(new Error('Email is invalid or already taken'))
      }
    }, 100)
  }

     let validateName = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("No empty"));
      } else {
        callback();
      }
    };
    return {
      rules: {
        pass: [{ validator: validatePass, trigger: 'change' }],
        checkPass: [{ validator: validatePass2, trigger: 'change' }],
        email:[{validator:checkEmail, trigger: 'blur'}],
        name: [{ validator:validateName, trigger: 'change' }]
      },
      UserRegister:{
      name: "",
      email:"",
      pass: "",
      checkPass: "",
      }
    };
  },

  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Register(formName) 
          this.$message({
            showClose: true,
            message: "Done",
            type: "success",
          });
          this.run();
          this.$emit("closepopup", false);
        } else {
          this.$message({
            showClose: true,
            message: "Oops, this is a error message.",
            type: "error",
          });
        }
      });
    },

    Register(formName) {
      console.log(formName);
      
      this.$axios
        .post("/api/register", {
            name: this.UserRegister.name, email: this.UserRegister.email,pass: this.UserRegister.pass 
        })
        .then(
          (response) => {
            this.$message({
                showClose: true,
                message: response.data,
                type: "success",
          });
          },
          (error) => {
            console.log(error);
          }
        );
      // this.$router.push({
      //   path: "/Layout",
      // });
      
    },



    Login() {
      this.$router.push({
        path: "/UserLogin",
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
