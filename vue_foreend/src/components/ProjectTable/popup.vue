<template>
  <!-- 表单验证时：
1、<el-form>标签绑定内容必须通过 :model='form' 绑定，不能使用v-model="form"
2、<el-form-item prop="input">中prop后面的字符必须和<el-form-item>标签中需要验证的值的参数名一样
3、需要验证的值必须是包含在<el-form>标签：model绑定的值里面，比如  form.input是form的参数 -->
  <div>
    <el-form :model="form" ref="form">
      <el-row>
        <el-col :span="6">
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
              <el-option label="Geely" value="Geely"></el-option>
              <el-option label="GWM" value="GWM"></el-option>
              <el-option label="Cherry" value="Cherry"></el-option>
              <el-option label="VW" value="VW"></el-option>
              <el-option label="GM" value="GM"></el-option>
              <el-option label="Honda" value="Honda"></el-option>
              <el-option label="NIO" value="NIO"></el-option>
              <el-option label="BAOJUN" value="BAOJUN"></el-option>
              <el-option label="Changan" value="Changan"></el-option>
              <el-option label="Ford" value="Ford"></el-option>
              <el-option label="Daimler" value="Daimler"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Project"
            :label-width="formLabelWidth"
            prop="PRJ"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input v-model="form.PRJ"></el-input>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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

        <el-col :span="6">
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

        <el-col :span="6">
          <el-form-item
            label="PE"
            :label-width="formLabelWidth"
            prop="PE"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\ \A-z]/g, '')"
              v-model="form.PE"
              autocomplete="on"
            ></el-input>
          </el-form-item>
        </el-col>

        <!-- </el-row>
      <el-row> -->
        <el-col :span="6">
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
              <el-option label="ASW3" value="ASW3"></el-option>
              <el-option label="ASW5" value="ASW5"></el-option>
              <el-option label="ASW8" value="ASW8"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Covermat"
            :label-width="formLabelWidth"
            prop="CV_Mat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.CV_Mat"
              placeholder="Select Cover material"
              :style="selectwidth"
            >
              <el-option label="TT1081B" value="TT1081B"></el-option>
              <el-option label="TT990B" value="TT990B"></el-option>
              <el-option label="TA4003B" value="TA4003B"></el-option>
              <el-option label="WT515" value="WT515"></el-option>
              <el-option label="WT546" value="WT546"></el-option>
              <el-option label="TES2403" value="TES2403"></el-option>
              <el-option label="TPO10" value="TPO10"></el-option>
              <el-option label="TT991" value="TT991"></el-option>
              <el-option label="TOSI818" value="TOSI818"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
              <el-option label="PG8" value="PG8"></el-option>
              <el-option label="DX51D" value="DX51D"></el-option>
              <el-option label="DX53D" value="DX53D"></el-option>
              <el-option label="DX54D" value="DX54D"></el-option>
              <el-option label="SPCC" value="SPCC"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
              <el-option label="H" value="H"></el-option>
              <el-option label="I" value="I"></el-option>
              <el-option label="Petal" value="Petal"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
              <el-option label="T45" value="T45"></el-option>
              <el-option label="T65" value="T65"></el-option>
              <el-option label="Al" value="Al"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
                label="ADP 1.3B 210kPa MP"
                value="ADP 1.3B 210kPa MP"
              ></el-option>
              <el-option
                label="ADP 1.3B 210kPa HP"
                value="ADP 1.3B 210kPa HP"
              ></el-option>
              <el-option
                label="ADP 1.3B 200kPa MP"
                value="ADP 1.3B 200kPa MP"
              ></el-option>
              <el-option
                label="ADPS 1.5 210kPa 0ms"
                value="ADPS 1.5 210kPa 0ms"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
              <el-option label="470 dtex" value="470 dtex"></el-option>
              <el-option label="350 dtex" value="350 dtex"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
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
                label="6-12 roll 3-9 roll"
                value="6-12 roll 3-9 roll"
              ></el-option>
              <el-option
                label="3-9 roll 6-12 roll"
                value="3-9 roll 6-12 roll"
              ></el-option>
              <el-option
                label="6-12 roll 3-9 compress"
                value="6-12 roll 3-9 compress"
              ></el-option>
              <el-option
                label="3-9 roll 6-12 compress"
                value="3-9 roll 6-12 compress"
              ></el-option>
              <el-option
                label="12 roll 3-6-9 compress"
                value="12 roll 3-6-9 compress"
              ></el-option>
              <el-option label="compress" value="compress"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Cushion D/mm"
            :label-width="formLabelWidth"
            prop="C_Diam"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.C_Diam"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Tether Type"
            :label-width="formLabelWidth"
            prop="C_Tether"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.C_Tether"
              placeholder="Select emblem material"
              :style="selectwidth"
            >
              <el-option label="3 Invert Y" value="3 Invert Y"></el-option>
              <el-option label="3 Y" value="3 Y"></el-option>
              <el-option label="2 Symmetry" value="2 Symmetry"></el-option>
              <el-option label="2 Unsymmetry" value="2 Unsymmetry"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Hinge width/mm"
            :label-width="formLabelWidth"
            prop="H_Width"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.H_Width"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Flappy mass/kg"
            :label-width="formLabelWidth"
            prop="Flappy_Mass"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.Flappy_Mass"
              autocomplete="off"
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
            label="Daokou"
            :label-width="formLabelWidth"
            prop="Daokou"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.Daokou"></el-checkbox>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-form-item
            label="CushionDiffusor"
            :label-width="formLabelWidth"
            prop="C_Diffusor"
            :rules="[
              { required: true, message: 'Need confirm', trigger: 'change' },
            ]"
          >
            <el-checkbox v-model="form.C_Diffusor"></el-checkbox>
          </el-form-item>
        </el-col>
      </el-row>

      <div class="block">
        <span>Date range </span>
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
      </div>
      <el-divider></el-divider>

      <el-row>
        <el-col :span="6">
          <el-form-item label="Testing result" :label-width="formLabelWidth">
            <el-select
              v-model="form.Testing"
              placeholder="Select Testing result"
              :style="selectwidth"
            >
              <el-option label="No Failure" value="No Failure"></el-option>
              <el-option
                label="Hinge Overtear"
                value="Hinge Overtear"
              ></el-option>
              <el-option
                label="Hinge Breakage"
                value="Hinge Breakage"
              ></el-option>
              <el-option
                label="Cover Hooks Detach"
                value="Cover Hooks Detach"
              ></el-option>
              <el-option
                label="Omega Hooks Detach"
                value="Omega Hooks Detach"
              ></el-option>
              <el-option
                label="Element Breakage"
                value="Element Breakage"
              ></el-option>
              <el-option
                label="Other Failure Modes"
                value="Other Failure Modes"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item label="Simulation result" :label-width="formLabelWidth">
            <el-select
              v-model="form.Simulation"
              placeholder="Select Simulation result"
              :style="selectwidth"
            >
              <el-option label="No Failure" value="No Failure"></el-option>
              <el-option
                label="Hinge Overtear"
                value="Hinge Overtear"
              ></el-option>
              <el-option
                label="Hinge Breakage"
                value="Hinge Breakage"
              ></el-option>
              <el-option
                label="Cover Hooks Detach"
                value="Cover Hooks Detach"
              ></el-option>
              <el-option
                label="Omega Hooks Detach"
                value="Omega Hooks Detach"
              ></el-option>
              <el-option
                label="Element Breakage"
                value="Element Breakage"
              ></el-option>
              <el-option
                label="Other Failure Modes"
                value="Other Failure Modes"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <div slot="footer" class="dialog-footer">
      <!-- <el-button @click="resetForm('form')">RESET</el-button> -->
      <el-button type="primary" @click="submitForm('form')">DONE</el-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    form: { a: 1 },
  },
  data: () => ({
    dialogFormVisible: false,
    selectwidth: "width: 250px",
    formLabelWidth: "130px",
  }),

  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
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

    run() {
      // this.form.DateRange = this.form.DateRange.substring(2,29)
      console.log(this.form.DateRange)
      this.$axios
        .post("/api/dabinfo", {
          params: {
            
            Dabinfo: JSON.stringify(this.form),
          },
        })
        .then(
          (response) => {
            console.log(response.data);
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>

