<template>
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
            placeholder="请输入气袋直径"
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
        <el-form-item label="Hinge width" prop="cover.hingewidth">
          <el-input
          onkeyup="value=value.replace(/[^\.\d]/g, '')"

            v-model="DABAIForm.cover.hingewidth"
            @click="output"
            placeholder="铰链的最小宽度"
          ></el-input>
        </el-form-item>
      </el-col>
      <el-col :xs="24" :sm="6" :md="6" :lg="6" :xl="6">
        <el-form-item label="Flappy mass" prop="cover.flappymass">
          <el-input
    
          onkeyup="value=value.replace(/[^\.\d]/g, '')"
            v-model="DABAIForm.cover.flappymass"
            @click="output"
            placeholder="Cover翻开区域质量"
          ></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-form-item label="Key option" prop="type">
          <el-checkbox-group v-model="DABAIForm.keyoption">
            <el-checkbox label="Hinge plane" name="type"></el-checkbox>
            <el-checkbox label="Wrapper" name="type"></el-checkbox>
            <el-checkbox label="Hinge neck" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
      </el-col>
    </el-row>
    <el-form-item>
      <el-button type="primary"  @click="submitForm('DABAIForm')"
        >RUN</el-button
      >
      <el-button @click="resetForm('DABAIForm')">RESET</el-button>
    </el-form-item>
    <!-- <el-form-item label="活动区域" prop="region">
    <el-select v-model="DABAIForm.region" placeholder="请选择活动区域">
      <el-option label="区域一" value="shanghai"></el-option>
      <el-option label="区域二" value="beijing"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="活动时间" required>
    <el-col :span="11">
      <el-form-item prop="date1">
        <el-date-picker type="date" placeholder="选择日期" v-model="DABAIForm.date1" style="width: 100%;"></el-date-picker>
      </el-form-item>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-form-item prop="date2">
        <el-time-picker placeholder="选择时间" v-model="DABAIForm.date2" style="width: 100%;"></el-time-picker>
      </el-form-item>
    </el-col>
  </el-form-item>
  <el-form-item label="即时配送" prop="delivery">
    <el-switch v-model="DABAIForm.delivery"></el-switch>
  </el-form-item>
  <el-form-item label="活动性质" prop="type">
    <el-checkbox-group v-model="DABAIForm.type">
      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
      <el-checkbox label="地推活动" name="type"></el-checkbox>
      <el-checkbox label="线下主题活动" name="type"></el-checkbox>
      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源" prop="resource">
    <el-radio-group v-model="DABAIForm.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="活动形式" prop="desc">
    <el-input type="textarea" v-model="DABAIForm.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('DABAIForm')">立即创建</el-button>
    <el-button @click="resetForm('DABAIForm')">重置</el-button>
  </el-form-item> -->
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      DABAIForm: {
        keyoption: [],
        interface: {
          type: "",
          typelist: [
            {
              value: "1",
              label: "ASW3",
            },
            {
              value: "2",
              label: "ASW5",
            },
            {
              value: "3",
              label: "ASW8",
            },
          ],
        },
        inflator: {
          type: "",
          typelist: [
            {
              value: "1",
              label: "ADP1.3B 210kPa",
            },
            {
              value: "2",
              label: "ADP1.3B 200kPa",
            },
            {
              value: "3",
              label: "ADPS 1.5 210kPa",
            },
          ],
        },

        cushion: {
          mat: "",
          matlist: [
            {
              value: "1",
              label: "350dtex",
            },
            {
              value: "2",
              label: "470dtex",
            },
          ],
          fold: "",
          foldlist: [
            {
              value: "1",
              label: "DRR",
            },
            {
              value: "2",
              label: "LC3",
            },
            {
              value: "3",
              label: "RC1",
            },
            {
              value: "4",
              label: "RC2",
            },
          ],
          tether: "",
          tetherlist: [
            {
              value: "1",
              label: "None",
            },
            {
              value: "2",
              label: "2 tethers",
            },
            {
              value: "3",
              label: "3 tethers",
            },
          ],
          di: "",
          dilist: [
            {
              value: "650",
              label: "650",
            },
            {
              value: "660",
              label: "660",
            },
            {
              value: "670",
              label: "670",
            },
            {
              value: "680",
              label: "680",
            },
            {
              value: "690",
              label: "690",
            },
            {
              value: "700",
              label: "700",
            },
            {
              value: "710",
              label: "710",
            },
          ],
        },
        cover: {
          mat: "",
          hingewidth: "",
          flappymass: "",
          matlist: [
            {
              value: "1",
              label: "TA4003",
            },
            {
              value: "2",
              label: "TT1081",
            },
            {
              value: "3",
              label: "TT990",
            },
          ],
          matrule: [
            {
              required: true,
              message: "Select one item",
              trigger: "change",
            },
          ],
          tearline: "",
          tearlinelist: [
            {
              value: "1",
              label: "H",
            },
            {
              value: "2",
              label: "I",
            },
            {
              value: "3",
              label: "P",
            },
          ],
        },
        housing: {
          mat: "",
          hingewidth: "",
          matlist: [
            {
              value: "1",
              label: "Steel",
            },
            {
              value: "2",
              label: "PG8",
            },
          ],
        },
        emblem: {
          mat: "",
          matlist: [
            {
              value: "1",
              label: "Al",
            },
            {
              value: "2",
              label: "T-45M",
            },
            {
              value: "3",
              label: "T-65",
            },
          ],
        },
      },
      DABAIrules: {
        cushion: {
          mat: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          fold: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          tether: [
            {
              required: true,
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
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          tearline: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
          hingewidth:[
            {required: true,  message: "请输入数字", trigger: "blur"},
          ],
          flappymass:[
            {required: true,  message: "请输入数字", trigger: "blur"}
          ],
        },
        housing: {
          mat: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        emblem: {
          mat: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        inflator: {
          type: [
            {
              required: true,
              message: "Please select one item",
              trigger: "change",
            },
          ],
        },
        interface: {
          type: [
            {
              required: true,
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
          console.log(this.DABAIForm)
          this.run()
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
          this.$axios.get("/api/dabai",{
          params:{
            ProjectTableData : JSON.stringify(this.DABAIForm)
          }
          })
          .then(
            response => {
              console.log(response);
            },
            error => {  
              console.log(error);
            }
          );
          this.saveDB()
    },
  },
};
</script>
