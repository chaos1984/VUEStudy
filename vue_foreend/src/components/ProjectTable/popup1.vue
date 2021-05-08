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
              <el-option label="Geely" value="[1,1]"></el-option>
              <el-option label="GWM" value="[2,1]"></el-option>
              <el-option label="Cherry" value="[3,1]"></el-option>
              <el-option label="VW" value="[1,0]"></el-option>
              <el-option label="GM" value="[2,0]"></el-option>
              <el-option label="Honda" value="[3,0]"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Project"
            :label-width="formLabelWidth"
            prop="Prj"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input v-model="form.Prj"></el-input>
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
              <el-option label="ASW3" value="1"></el-option>
              <el-option label="ASW5" value="2"></el-option>
              <el-option label="ASW8" value="3"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Covermat"
            :label-width="formLabelWidth"
            prop="Covermat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Covermat"
              placeholder="Select Cover material"
              :style="selectwidth"
            >
              <el-option label="TT1081B" value="TT1081B"></el-option>
              <el-option label="TT990B" value="TT990B"></el-option>
              <el-option label="TA4003B" value="TA4003B"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Housing mat"
            :label-width="formLabelWidth"
            prop="Housingmat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Housingmat"
              placeholder="Select housing material"
              :style="selectwidth"
            >
              <el-option label="DX51D" value="DX51D"></el-option>
              <el-option label="DX53D" value="DX53D"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Tearling Type"
            :label-width="formLabelWidth"
            prop="TearlineType"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.TearlineType"
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
            prop="Emblemmat"
            :rules="[
              { required: true, message: 'Select one item', trigger: 'change' },
            ]"
          >
            <el-select
              v-model="form.Emblemmat"
              placeholder="Select emblem material"
              :style="selectwidth"
            >
              <el-option label="T45" value="T45"></el-option>
              <el-option label="T65" value="T65"></el-option>
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
            prop="Cushionmat"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.Cushionmat"
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
            prop="CushionFoldType"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.CushionFoldType"
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
              <el-option label="compress" value="compress"></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Cushion D/mm"
            :label-width="formLabelWidth"
            prop="CushionDiameter"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.CushionDiameter"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Tether Type"
            :label-width="formLabelWidth"
            prop="TetherType"
            :rules="[{ required: true, message: 'Select one item' }]"
          >
            <el-select
              v-model="form.TetherType"
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
            prop="HingeWidth"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.HingeWidth"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :span="6">
          <el-form-item
            label="Flappy mass/kg"
            :label-width="formLabelWidth"
            prop="FlappyMass"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="form.FlappyMass"
              autocomplete="off"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="2">
          <el-form-item
            label="Wrapper"
            :label-width="formLabelWidth"
            prop="CushionWrapper"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-checkbox v-model="form.CushionWrapper"></el-checkbox>
          </el-form-item>
        </el-col>

        <el-col :span="2">
          <el-form-item
            label="Hinge plane"
            :label-width="formLabelWidth"
            prop="HingePlane"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-checkbox v-model="form.HingePlane"></el-checkbox>
          </el-form-item>
        </el-col>

        <el-col :span="2">
          <el-form-item
            label="Hinge Neck"
            :label-width="formLabelWidth"
            prop="HingeNeck"
            :rules="[{ required: true, trigger: 'blur' }]"
          >
            <el-checkbox v-model="form.HingeNeck"></el-checkbox>
          </el-form-item>
        </el-col>
      </el-row>
      <el-divider></el-divider>

      <el-row>
        <el-col :span="6">
          <el-form-item label="Testing result" :label-width="formLabelWidth">
            <el-select
              v-model="form.Testing"
              placeholder="Select Testing result"
              :style="selectwidth"
            >
              <el-option label="No Failure" value="0"></el-option>
              <el-option label="Hinge Overtear" value="1"></el-option>
              <el-option label="Hinge Breakage" value="2"></el-option>
              <el-option label="Cover Hooks Detach" value="3"></el-option>
              <el-option label="Omega Hooks Detach" value="4"></el-option>
              <el-option label="Element Breakage" value="5"></el-option>
              <el-option label="Other failure Modes" value="6"></el-option>
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
              <el-option label="No Failure" value="0"></el-option>
              <el-option label="Hinge Overtear" value="1"></el-option>
              <el-option label="Hinge Breakage" value="2"></el-option>
              <el-option label="Cover Hooks Detach" value="3"></el-option>
              <el-option label="Omega Hooks Detach" value="4"></el-option>
              <el-option label="Element Breakage" value="5"></el-option>
              <el-option label="Other Failure Modes" value="6"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <div slot="footer" class="dialog-footer">
      <el-button @click="resetForm('form')">RESET</el-button>
      <el-button type="primary" @click="submitForm('form')">DONE</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogFormVisible: false,
      form: {
        Prj: "P05",
        AFIS: "12345",
        ESR: "123456",
        PE: "Haiming Chen",
        Interface: "1",
        Covermat: "TT1081B",
        Housingmat: "DX51D",
        Emblemmat: "T45",
        Inflator: "ADPS 1.5 210kPa 0ms",
        Cushionmat: "470 dtex",
        CushionFoldType: "3-9 roll 6-12 roll",
        CushionDiameter: "660",
        TetherType:"2 Unsymmetry",
        CushionWrapper: false,
        TearlineType: "H",
        FlappyMass: "0.022",
        HingeWidth: "32",
        HingePlane: false,
        HingeNeck: false,
        Testing: "No Failure",
        Simulation: "No Failure",
        OEM: "[1,1]",
      },
      selectwidth: "width: 385px",
      formLabelWidth: "130px",
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this.form);
          this.run();
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    run() {
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

<style>
</style>