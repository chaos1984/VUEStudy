<template>
  <div>
    <el-row
      ><span class="Title">{{ Prj }}</span></el-row >

    <v-divider></v-divider>

    <el-row class="row-bg-light">
      <el-col :span="8"
        ><span>AFIS: </span><span class="Content">{{ AFIS }}</span></el-col
      >
      <el-col :span="8"
        ><span>ESR: </span><span class="Content">{{ ESR }}</span></el-col
      >
      <el-col :span="8"
        ><span>PE: </span> <span class="Content">{{ PE }}</span></el-col
      >

      <el-col :span="6"
        ><span>Interface: </span
        ><span class="Content">{{ Interface }}</span></el-col
      >
      <el-col :span="6"
        ><span>Cover mat.: </span
        ><span class="Content">{{ Covermat }}</span></el-col
      >
      <el-col :span="6"
        ><span>Housing mat.: </span
        ><span class="Content">{{ Housingmat }}</span></el-col
      >
      <el-col :span="6"
        ><span>Emblem mat.: </span
        ><span class="Content">{{ Emblemmat }}</span></el-col
      >
      <el-col :span="6"
        ><span>Inflator: </span
        ><span class="Content">{{ Inflator }}</span></el-col
      >
      <el-col :span="6"
        ><span>Cushion mat.: </span
        ><span class="Content">{{ Cushionmat }}</span></el-col
      >
      <el-col :span="6"
        ><span>Cushion Fold: </span
        ><span class="Content">{{ CushionFoldType }}</span></el-col
      >
      <el-col :span="6"
        ><span>Cushion Diameter: </span
        ><span class="Content">{{ CushionDiameter }} mm</span></el-col
      >
      <el-col :span="6"
        ><span>Tether: </span
        ><span class="Content">{{ TetherType }}</span></el-col
      >
      <el-col :span="6"
        ><span>Cushion Wrapper: </span
        ><span class="Content">{{ CushionWrapper }}</span></el-col
      >
      <el-col :span="6"
        ><span>TearlineType: </span
        ><span class="Content">{{ TearlineType }}</span></el-col
      >
      <el-col :span="6"
        ><span>Flappy Mass: </span
        ><span class="Content">{{ FlappyMass }} kg</span></el-col
      >
      <el-col :span="6"
        ><span>Hinge Width: </span
        ><span class="Content">{{ HingeWidth }} mm</span></el-col
      >
      <el-col :span="6"
        ><span>HingePlane: </span
        ><span class="Content">{{ HingePlane }}</span></el-col
      >
      <el-col :span="6"
        ><span>HingeNeck: </span
        ><span class="Content">{{ HingeNeck }}</span></el-col
      >
    </el-row>

    <el-row class="row-bg-dark">
      <el-col :span="12"
        ><span>Testing: </span
        ><span class="Content">{{ Testing }}</span></el-col
      >
      <el-col :span="12"
        ><span>Simulation: </span
        ><span class="Content">{{ Simulation }}</span></el-col
      >
    </el-row>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  props: {
    data: {},
  },
  data() {
    return {
      Prj: "1",
      AFIS: "1",
      ESR: "1",
      PE: "1",
      Interface: "",
      Covermat: "TT1081B",
      Housingmat: "DX51D",
      Emblemmat: "T45",
      Inflator: "ADPS 1.5 210kPa 0ms",
      Cushionmat: "470 dtex",
      CushionFoldType: "3-9 roll 6-12 roll",
      CushionDiameter: "660",
      TetherType: "2 Unsymmetry",
      CushionWrapper: false,
      TearlineType: "H",
      FlappyMass: "0.022",
      HingeWidth: "32",
      HingePlane: false,
      HingeNeck: false,
      Testing: "No Failure",
      Simulation: "No Failure",
      OEM: "[1,1]",
    };
  },
  computed: {
    ...mapState({
      CurrentForm: (state) => state.form,
    }),
  },
  
   mounted() {
    this.getData();
  },
methods: {
    getData() {
      // this.Prj = this.CurrentForm.hovercard.Prj;
      this.Prj = this.CurrentForm.hovercard.PRJ;
      console.log(this.data);
      console.log('DetailInfo');
      console.log(this.CurrentForm.hovercard);
    },
  },
};
</script>

<style scoped>
.Title {
  color: rgb(252, 0, 0);
}
.Content {
  color: rgb(0, 17, 252);
}
.row-bg-light {
  padding: 10px 0;
  background: #e5e9f2;
}
.row-bg-dark {
  padding: 10px 0;
  background: #99a9bf;
}
</style>