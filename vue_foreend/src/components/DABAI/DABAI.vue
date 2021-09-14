<template>
  <div>
    <el-alert   show-icon title=" AI model is under training, and it is not suitable for each project." type="error"> </el-alert>
    <el-alert   show-icon title=" So far, there are only five parameters for DAB cover hinge failure predIction, and only for TT1081B material." type="warning"> </el-alert>
    <el-form
      :model="DABAIForm"
      ref="DABAIForm"
      :rules="DABAIrules"
      label-width="120px"
      label-position="left"
    >
      <el-row>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Cushion Mat" prop="cushion.mat">
            <el-select
              v-model="DABAIForm.cushion.mat"
              placeholder="请选择气袋材料"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.cushion.matlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Cushion fold" prop="cushion.fold">
            <el-select
              v-model="DABAIForm.cushion.fold"
              placeholder="请选择气袋折叠形式"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.cushion.foldlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Cushion tether" prop="cushion.tether">
            <el-select
              v-model="DABAIForm.cushion.tether"
              placeholder="请选择气袋拉带"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.cushion.tetherlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Cushion Di." prop="cushion.di">
            <el-select
              v-model="DABAIForm.cushion.di"
              placeholder="请输入气袋直径mm"
            >
              <el-option
                v-for="item in DABAIForm.cushion.dilist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>

      <el-row>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Cover Mat" prop="cover.mat">
            <el-select
              v-model="DABAIForm.cover.mat"
              placeholder="请选择Cover材料"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.cover.matlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Housing Mat" prop="housing.mat">
            <el-select
              v-model="DABAIForm.housing.mat"
              placeholder="请选择Housing材料"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.housing.matlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Emblem Mat" prop="emblem.mat">
            <el-select
              v-model="DABAIForm.emblem.mat"
              placeholder="请选择Emblem材料"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.emblem.matlist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Inflator" prop="inflator.type">
            <el-select
              v-model="DABAIForm.inflator.type"
              placeholder="请选择Inflator类型"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.inflator.typelist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Tearline" prop="cover.tearline">
            <el-select
              v-model="DABAIForm.cover.tearline"
              placeholder="请选择Cover撕裂线形式"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.cover.tearlinelist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Interface" prop="interface.type">
            <el-select
              v-model="DABAIForm.interface.type"
              placeholder="请选择DAB模块接口类型"
              disabled
            >
              <el-option
                v-for="item in DABAIForm.interface.typelist"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>

      <el-row>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Hinge length" prop="cover.hingewidth">
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="DABAIForm.cover.hingewidth"
              placeholder="铰链的最小宽度mm"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
          <el-form-item label="Flappy mass" prop="cover.flappymass">
            <el-input
              onkeyup="value=value.replace(/[^\.\d]/g, '')"
              v-model="DABAIForm.cover.flappymass"
              placeholder="Cover翻开区域质量kg"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-form-item label="Other key option">
            <el-checkbox
              label="Wrapper"
              v-model="DABAIForm.cushion.wrapper"
              name="type"
            ></el-checkbox>
            <el-checkbox
              label="Hinge plane"
              v-model="DABAIForm.cover.hingeplane"
              name="type"
            ></el-checkbox>
            <el-checkbox
              label="Hinge neck"
              v-model="DABAIForm.cover.hingeneck"
              name="type"
            ></el-checkbox>
            <el-checkbox
              label="Hinge Undercut"
              v-model="DABAIForm.cover.daokou"
              name="type"
              disabled
            ></el-checkbox>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
        <el-button type="primary" @click="submitForm('DABAIForm')"
          >RUN</el-button
        >
        <el-button @click="resetForm('DABAIForm')">RESET</el-button>
      </el-form-item>
    </el-form>
    <el-alert :title="DABPrediction" :style="{color:fontcolor}"> </el-alert>
    <el-table
      :data="tableData"
      style="width: 100%"
      stripe
      fit
      highlight-current-row
    >
      <el-table-column prop="covermat" label="Cover mat" width="180" sortable />
      <el-table-column
        prop="hingewidth"
        label="Hinge width"
        width="180"
        sortable
      />
      <!-- <el-table-column prop="tearline" label="Cover tearline" width="180" sortable/> -->
      <el-table-column
        prop="cushiondiam"
        label="Cushion diameter"
        width="180"
        sortable
      />
      <!-- <el-table-column prop="foldtype" label="Cushion fold type" width="180" sortable/> -->
      <el-table-column
        prop="flappymass"
        label="Cover flappy mass"
        width="180"
        sortable
      />
      <el-table-column
        prop="hingeneck"
        label="Cover hinge neck"
        width="180"
        sortable
      />
      <el-table-column
        prop="wrapper"
        label="Cushion wrapper"
        width="180"
        sortable
      />
      <el-table-column
        prop="aiprediction"
        label="AI Prediction"
        width="180"
        sortable
      />
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fontcolor:"red",
      tableData: [],
      DABPrediction: "",
      DABAIForm: {
        interface: {
          type: "",
          typelist: [
            {
              value: 0,
              label: "ASW3",
            },
            {
              value: 1,
              label: "ASW5",
            },
            {
              value: 2,
              label: "ASW8",
            },
          ],
        },
        inflator: {
          type: "",
          typelist: [
            {
              value: 0,
              label: "ADP1.3B 200kPa",
            },
            {
              value: 1,
              label: "ADP1.3B 210kPa",
            },
            {
              value: 2,
              label: "ADPS 1.5 210kPa",
            },
          ],
        },
        cushion: {
          wrapper: true,
          mat: "",
          matlist: [
            {
              value: 0,
              label: "350dtex",
            },
            {
              value: 1,
              label: "470dtex",
            },
          ],
          fold: "",
          foldlist: [
            {
              value: 0,
              label: "DRR",
            },
            {
              value: 1,
              label: "LC3",
            },
            {
              value: 2,
              label: "RC1",
            },
            {
              value: 3,
              label: "RC2",
            },
          ],
          tether: "",
          tetherlist: [
            {
              value: 0,
              label: "None",
            },
            {
              value: 2,
              label: "2 tethers",
            },
            {
              value: 3,
              label: "3 tethers",
            },
          ],
          di: "",
          dilist: [
            {
              value: 650,
              label: "650",
            },
            {
              value: 660,
              label: "660",
            },
            {
              value: 670,
              label: "670",
            },
            {
              value: 680,
              label: "680",
            },
            {
              value: 690,
              label: "690",
            },
            {
              value: 700,
              label: "700",
            },
            {
              value: 710,
              label: "710",
            },
            {
              value: 720,
              label: "720",
            },
          ],
        },
        cover: {
          mat: "",
          hingewidth: "",
          hingeplane: true,
          daokou: true,
          hingeneck: true,
          flappymass: "",
          matlist: [
            {
              value: 1,
              label: "TA4003",
            },
            {
              value: 2,
              label: "TT1081",
            },
            {
              value: 3,
              label: "TT990",
            },
          ],
          tearline: "",
          tearlinelist: [
            {
              value: 0,
              label: "H",
            },
            {
              value: 1,
              label: "I",
            },
            {
              value: 2,
              label: "P",
            },
            {
              value: 3,
              label: "W",
            },
          ],
        },
        housing: {
          mat: "",
          matlist: [
            {
              value: 0,
              label: "PG8",
            },
            {
              value: 1,
              label: "Steel",
            },
          ],
        },
        emblem: {
          mat: "",
          matlist: [
            {
              value: 0,
              label: "Al",
            },
            {
              value: 1,
              label: "T-45M",
            },
            {
              value: 2,
              label: "T-65M",
            },
          ],
        },
      },
      DABAIrules: {
        cushion: {
          mat: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          fold: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          tether: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          di: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        cover: {
          mat: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          tearline: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          hingewidth: [
            { required: true, message: "请输入数字", trigger: "blur" },
          ],
          flappymass: [
            { required: true, message: "请输入数字", trigger: "blur" },
          ],
        },
        housing: {
          mat: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        emblem: {
          mat: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        inflator: {
          type: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        interface: {
          type: [
            {
              required: false,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this.DABAIForm);
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
    output() {
      console.log(this.DABAIForm.cover.mat);
    },
    run() {
      this.$axios
        .post("/api/dabai", {
          params: {
            TestData: JSON.stringify(this.DABAIForm),
          },
        })
        .then(
          (response) => {
            if (response.data < 0.5) {
              this.DABPrediction = "GOOD";
              this.fontcolor = "green"
            } else {
              this.DABPrediction = " Failure";
              this.fontcolor = "red"
            }
            // if (this.DABAIForm.cover.mat === this.DABAIForm.cover.matlist.value){
                
            // };
            // console.log("this.DABAIForm.cover.matlist.label")
            // console.log(this.DABAIForm.cover.matlist[2])
          this.$message({
                showClose: true,
                message: "AI prediction is under training, so maybe the AI score is not correct for each model!",
                type: 'error',
          });
            this.tableData.push({
              covermat: "TT1081",
              hingewidth: this.DABAIForm.cover.hingewidth,
              cushiondiam: this.DABAIForm.cushion.di,
              flappymass: this.DABAIForm.cover.flappymass,
              hingeneck: this.DABAIForm.cover.hingeneck.toString(),
              wrapper: this.DABAIForm.cushion.wrapper.toString(),
              aiprediction: response.data,
            });
            console.log(response);
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>

<style scoped>
#ai {
  background-image: linear-gradient(#e66465, #9198e5);
}
</style>