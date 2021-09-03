<template>
  <!-- 表单验证时：
1、<el-form>标签绑定内容必须通过 :model='form' 绑定，不能使用v-model="form"
2、<el-form-item prop="input">中prop后面的字符必须和<el-form-item>标签中需要验证的值的参数名一样
3、需要验证的值必须是包含在<el-form>标签：model绑定的值里面，比如  form.input是form的参数 -->
  <div>
    <el-form :model="form" ref="form">
      <el-row>
        <el-col :lg="6" :xs="12">
          <el-form-item
            label="OEM"
            :label-width="formLabelWidth"
            prop="OEM"
            :rules="[{ required: true, trigger: 'change' }]"
          >
            <el-select
              v-model="form.OEM"
              placeholder="Select OEM"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.OEM"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Project"
            :label-width="formLabelWidth"
            prop="PRJ"
            :rules="PRJ"
          >
            <el-input v-model="form.PRJ"></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="AFIS"
            :label-width="formLabelWidth"
            prop="AFIS"
            :rules="[
              { required: true, trigger: 'blur' },
              { max: 5, min: 5, message: '5-char', trigger: 'blur' },
            ]"
          >
            <el-input v-model="form.AFIS" autocomplete="off"></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="ESR"
            :label-width="formLabelWidth"
            prop="ESR"
            :rules="[
              { required: true, trigger: 'blur' },
              { max: 6, min: 6, message: '6-digit', trigger: 'blur' },
            ]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\d]/g, '')"
              v-model="form.ESR"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="PE"
            :label-width="formLabelWidth"
            prop="PE"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-select
              v-model="form.PE"
              placeholder="Select DAB Interface"
              :style="selectwidth"
              filterable
              allow-create
            >
              <el-option
                v-for="(item, index) in formItem.PE"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <!-- </el-row>
      <el-row> -->
        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Interface"
            :label-width="formLabelWidth"
            prop="Interface"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Interface"
              placeholder="Select DAB Interface"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.Interface"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cover mat"
            :label-width="formLabelWidth"
            prop="CV_Mat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.CV_Mat"
              placeholder="Select Cover material"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.CoverMat"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Housing mat"
            :label-width="formLabelWidth"
            prop="H_Mat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.H_Mat"
              placeholder="Select housing material"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.HousingMat"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Tearling Type"
            :label-width="formLabelWidth"
            prop="Tearline"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Tearline"
              placeholder="Select Tearline Type"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.TearlineType"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Emblem mat"
            :label-width="formLabelWidth"
            prop="E_Mat"
            :rules="[
              { required: true, message: 'Select one item', trigger: 'change' },
            ]"
          >
            <el-select
              v-model="form.E_Mat"
              placeholder="Select emblem material"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.EmblemMat"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Inflator"
            :label-width="formLabelWidth"
            prop="Inflator"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Inflator"
              placeholder="Select inflator"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.Inflator"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cushion Mat."
            :label-width="formLabelWidth"
            prop="C_Mat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.C_Mat"
              placeholder="Select emblem material"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.CushionMat"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cushion Fold "
            :label-width="formLabelWidth"
            prop="C_Type"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.C_Type"
              placeholder="Select Fold Type"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.CushionFold"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cushion Diam"
            :label-width="formLabelWidth"
            prop="C_Diam"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.C_Diam"
              autocomplete="off"
              placeholder="mm"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Tether Type"
            :label-width="formLabelWidth"
            prop="C_Tether"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.C_Tether"
              placeholder="Select tether type"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.TetherType"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cover Leather"
            :label-width="formLabelWidth"
            prop="CV_Leather"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.CV_Leather"
              placeholder="Select tether type"
              :style="selectwidth"
            >
              <el-option
                v-for="(item, index) in formItem.CV_Leather"
                :key="index"
                :label="item"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Hinge Length"
            :label-width="formLabelWidth"
            prop="H_Width"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.H_Width"
              autocomplete="off"
              placeholder="mm"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Flap mass"
            :label-width="formLabelWidth"
            prop="Flappy_Mass"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.Flappy_Mass"
              autocomplete="off"
              placeholder="kg"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="4">
          <el-form-item
            label="Wrapper"
            :label-width="formLabelWidth"
            prop="Wrapper"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.Wrapper"></el-checkbox>
          </el-form-item>
        </el-col>

        <el-col :span="4">
          <el-form-item
            label="Hinge plane"
            :label-width="formLabelWidth"
            prop="H_Plane"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.H_Plane"></el-checkbox>
          </el-form-item>
        </el-col>

        <el-col :span="4">
          <el-form-item
            label="Hinge Neck"
            :label-width="formLabelWidth"
            prop="H_Neck"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.H_Neck"></el-checkbox>
          </el-form-item>
        </el-col>

        <el-col :span="4">
          <el-form-item
            label="Under Cut"
            :label-width="formLabelWidth"
            prop="UnderCut"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.UnderCut"></el-checkbox>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-form-item
            label="Cushion Diffusor"
            :label-width="formLabelWidth"
            prop="C_Diffusor"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.C_Diffusor"></el-checkbox>
          </el-form-item>
        </el-col>
        <el-col :lg="6" :xs="12">
        
            
            <el-form-item label="Date select" :label-width="formLabelWidth" prop="DateRange" :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]">
              <el-date-picker
                v-model="form.DateRange"
                type="daterange"
                align="right"
                start-placeholder="Start Date"
                end-placeholder="End Date"
                value-format="yyyy-MM-dd"
              >
                >
              </el-date-picker>
            </el-form-item>
          
        </el-col>
        
      </el-row>
      <el-form-item label="Remarks">
        <el-input
          type="textarea"
          :rows="10"
          placeholder="Remarks"
          v-model="form.Remarks"
        >
        </el-input>
      </el-form-item>
      <el-divider />
      <el-row>
        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Hinge width"
            :label-width="formLabelWidth"
            prop="Hinge_Width"
            :rules= "userrules"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.Hinge_Width"
              autocomplete="off"
              placeholder="mm"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Cov-Inf Height"
            :label-width="formLabelWidth"
            prop="CV_Height"
            :rules= "userrules"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.CV_Height"
              autocomplete="off"
              placeholder="mm"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Hinge Area"
            :label-width="formLabelWidth"
            prop="Hinge_Area"
            :rules= "userrules"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.Hinge_Area"
              autocomplete="off"
              placeholder="mm2"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :lg="6" :xs="12">
          <el-form-item
            label="Hinge Radius"
            :label-width="formLabelWidth"
            prop="Hinge_Radius"
            :rules= "userrules"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.Hinge_Radius"
              autocomplete="off"
              placeholder="mm"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>


      <el-row :gutter="10">
        <el-col :lg="12" :xs="12">
          <el-form-item
            label="PPT dir."
            :label-width="formLabelWidth"
            prop="PPT"
          
            :rules="userrules"
          >
            <el-input 
              v-model="form.PPT"
              autocomplete ="off"
              :placeholder = "pptfile"
              :disabled = "userpiority"
              clearable
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>

      
      <el-divider></el-divider>

      <el-row>
        <el-col :span="12">
          <el-form-item label="Testing result" :label-width="formLabelWidth">
            <el-checkbox-group v-model="form.Testing">
              <el-checkbox-button
                v-for="item in formItem.FailureMode"
                :label="item"
                :key="item"
                >{{ item }}</el-checkbox-button
              >
            </el-checkbox-group>

          </el-form-item>
        </el-col>

        <el-col :span="12">
          <el-form-item label="Simulation result" :label-width="formLabelWidth">
            <el-checkbox-group v-model="form.Simulation">
              <el-checkbox-button
                v-for="item in formItem.FailureMode"
                :label="item"
                :key="item"
                >{{ item }}</el-checkbox-button
              >
            </el-checkbox-group>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-row>
      <el-col :span="3">
        <!-- <el-button @click="resetForm('form')">RESET</el-button> -->
        <el-button type="primary" @click="submitForm('form')" style="width: 80%"
          >Confirm</el-button
        >
      </el-col>
      <el-col :span="3">
        <!-- <el-button @click="resetForm('form')">RESET</el-button> -->
        <el-button
          type="primary"
          @click="submitForm('form', 'true')"
          style="width: 80%"
          >Copy</el-button
        >
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  props: {
    form: {},
  },
  data() {
    let checkprj = (rule, value, callback) => {
      const prjReg = /^([a-zA-Z0-9_-])+(_V[0-9_-])+/;
      if (!value) {
        return callback(new Error("Autoliv E-mail adress"));
      }
      setTimeout(() => {
        if (prjReg.test(value)) {
          callback();
        } else {
          callback(new Error("Please input XXX_VX"));
        }
      }, 100);
    };
    return {
      userrules: [],
      pptfile: "None",
      PRJ: [{ required: true, validator: checkprj, trigger: "change" }],
      checkedList: [],
      dialogFormVisible: false,
      selectwidth: "width: 100%",
      formLabelWidth: "130px",
      formItem: { },
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    ...mapState({
      CurrentForm: (state) => state.form,
      User: (state) => state.User,
    }),
  },

  watch: {
    form(newval) {
      if (newval.length != 0) {
        this.form = newval;
      }
    },
  },
  mounted() {
    this.getDatafromJson();
    this.Permission();
  },
  methods: {
    Permission() {
      // console.log("this.User");
      // console.log(this.User);
      if (this.User.Priority != "1") {
        this.userpiority = true;
        
      } else {
        this.userpiority = false;
        this.userrules = [{ required: true }]
      }
    },
    getDatafromJson() {
      this.$axios.get("/static/json/formItem.json").then(
        (response) => {
          this.Permission()
          this.formItem = JSON.parse(JSON.stringify(response.data));
          // this.Permission()
        },
        (error) => {
          console.log(error);
        }
      );
    },

    submitForm(formName, copy = false) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.run(copy);
          // this.$emit("closepopup", false);
        } else {
          this.$message({
            showClose: true,
            message: "Oops, this is a error message.",
            type: "error",
          });
        }
      });
    },

    run(copy) {
      if (this.form.Log == "") {
        this.form.Log = [];
      }
      this.$axios
        .post("/api/dabinfo", {
          params: {
            Dabinfo: JSON.stringify(this.form).replace(/'/g, '"'),
            Copy: copy,
          },
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
    },
  },
};
</script>

