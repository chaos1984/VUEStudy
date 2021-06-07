<template>
  <div>
    <v-data-table
      :headers="ESRheaders"
      :items="ESRTable"
      class="elevation-1"
      multi-sort
      :search="search"
      :custom-filter="filterOnlyCapsText"
    >
      <template v-slot:top>
        <v-toolbar flat color="white">
          <v-toolbar-title>ESR Table</v-toolbar-title>
          <v-text-field
            v-model="search"
            label="Search"
            class="mx-4"
          ></v-text-field>

          <v-divider class="mx-4" inset vertical></v-divider>

          <v-spacer></v-spacer>

          <!-- <v-btn class="mb-2" width="100px" @click.native="SaveData()"
            >Save</v-btn
          > -->

          <v-btn class="mb-2" width="100px" @click="addItem()">New</v-btn>
        </v-toolbar>
      </template>

      <template v-slot:item.actions="{ item }">
        <el-popover placement="right" width="800" trigger="click">
          <v-icon small class="mr-2" slot="reference">mdi-eye</v-icon>
          <div>
            <el-row
              ><span class="Title">{{ item.PRJ }}</span></el-row
            >

            <v-divider></v-divider>

            <el-row class="row-bg-light">
              <el-col :span="6"
                ><span>AFIS: </span
                ><span class="Content">{{ item.AFIS }}</span></el-col
              >
              <el-col :span="6"
                ><span>ESR: </span
                ><span class="Content">{{ item.ESR }}</span></el-col
              >
              <el-col :span="6"
                ><span>PE: </span>
                <span class="Content">{{ item.PE }}</span></el-col
              >

              <el-col :span="6"
                ><span>CAE: </span>
                <span class="Content">{{ item.CAE }}</span></el-col
              >

              <el-col :span="6"
                ><span>Interface: </span
                ><span class="Content">{{ item.Interface }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cover mat.: </span
                ><span class="Content">{{ item.CV_Mat }}</span></el-col
              >
              <el-col :span="6"
                ><span>Housing mat.: </span
                ><span class="Content">{{ item.H_Mat }}</span></el-col
              >
              <el-col :span="6"
                ><span>Emblem mat.: </span
                ><span class="Content">{{ item.E_Mat }}</span></el-col
              >
              <el-col :span="6"
                ><span>Inflator: </span
                ><span class="Content">{{ item.Inflator }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cushion mat.: </span
                ><span class="Content">{{ item.C_Mat }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cushion Fold: </span
                ><span class="Content">{{ item.C_Type }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cushion Diameter: </span
                ><span class="Content">{{ item.C_Diam }} mm</span></el-col
              >
              <el-col :span="6"
                ><span>Tether: </span
                ><span class="Content">{{ item.C_Tether }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cushion Wrapper: </span
                ><span class="Content">{{ item.Wrapper }}</span></el-col
              >
              <el-col :span="6"
                ><span>TearlineType: </span
                ><span class="Content">{{ item.Tearline }}</span></el-col
              >
              <el-col :span="6"
                ><span>Flappy Mass: </span
                ><span class="Content">{{ item.Flappy_Mass }} kg</span></el-col
              >
              <el-col :span="6"
                ><span>Hinge Width: </span
                ><span class="Content">{{ item.H_Width }} mm</span></el-col
              >
              <el-col :span="6"
                ><span>HingePlane: </span
                ><span class="Content">{{ item.H_Plane }}</span></el-col
              >
              <el-col :span="5"
                ><span>HingeNeck: </span
                ><span class="Content">{{ item.H_Neck }}</span></el-col
              >
              <el-col :span="6"
                ><span>Cushion Diffusor: </span
                ><span class="Content">{{ item.C_Diffusor }}</span></el-col
              >
         

            <el-col :span="12"
                ><span>DateRange: </span
                ><span class="Content">{{ item.DateRange}}</span></el-col
              >
            </el-row>

            <el-row class="row-bg-dark">
              <el-col :span="12"
                ><span>Testing: </span
                ><span class="Content">{{ item.Testing }}</span></el-col
              >
              <el-col :span="12"
                ><span>Simulation: </span
                ><span class="Content">{{ item.Simulation }}</span></el-col
              >
            </el-row>
          </div>
        </el-popover>

        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small class="mr-2" @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
    </v-data-table>

    <el-dialog
      :title="Operation"
      :visible.sync="dialogFormVisible"
      width="100%"
    >
      <POPUP :form="popupdata"></POPUP>
    </el-dialog>

    <el-divider />
    <el-row>
      <el-col :span="12"><DABSVM :getdata="ESRTable"></DABSVM></el-col>
      <el-col :span="12"><StatisticsPie :getdata="ESRTable"></StatisticsPie
      ></el-col>
    </el-row>
    <el-divider />
    <ESRCalendars :getdata="ESRTable"/>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  components: {
    DABSVM: () => import("@/components/Echart/DABSVM"),
    StatisticsPie: () => import("@/components/Echart/StatisticsPie"),
    POPUP: () => import("@/components/ProjectTable/popup"),
    ESRCalendars: () => import("@/components/ProjectTable/ESRCalendars"),
  },
  data: () => ({
    Operation: "Project",
    popupdata: {},
    overlay: false,
    detailInfo: {},
    dialogFormVisible: false,
    dialog: false,
    dialogDelete: false,
    search: "",
    ESRheaders: [
      {
        text: "ID",
        value: "ID",
      },
      {
        text: "Prj",
        align: "start",
        sortable: false,
        value: "PRJ",
      },
      // { text: "ESR", value: "ESR" },
      // { text: "PE", value: "PE" },
      // { text: "Interface", value: "Interface" },
      { text: "C_Mat.", value: "CV_Mat" },
      { text: "H_Mat", value: "H_Mat" },
      { text: "E_Mat", value: "E_Mat" },
      { text: "Inflator", value: "Inflator" },
      { text: "C_Mat", value: "C_Mat" },
      { text: "C_type", value: "C_Type" },
      { text: "C_Diam", value: "C_Diam" },
      { text: "Tearline", value: "Tearline" },
      { text: "Flappy Mass", value: "Flappy_Mass" },
      { text: "H_width", value: "H_Width" },
      { text: "H_Plane", value: "H_Plane" },
      { text: "H_Neck", value: "H_Neck" },
      { text: "Option", value: "actions", sortable: false },
    ],
    ESRTable: [],
    editedIndex: -1,
    filter: (value) => {
      if (!this.ESR) return true;

      return value < parseInt(this.ESR);
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    ...mapState({
      CurrentForm: (state) => state.form,
    }),
  },

  watch: {
    dialog(val) {
      val || this.getData();
    },
    dialogDelete(val) {
      val || this.getData();
    },
    dialogFormVisible(val) {
      val || this.getData();
    },
  },

  mounted() {
    this.getData();
  },
  methods: {
    closepopup(val){
      this.dialogFormVisible = val
    },
    filterOnlyCapsText(value, search) {
      return (
        value != null &&
        search != null &&
        typeof value === "string" &&
        value.toString().indexOf(search) !== -1
      );
    },

    getData() {
      this.$axios.get("/api/getdatabase").then(
        (response) => {
          this.ESRTable = response.data;
          console.log(this.ESRTable)
        },
        (error) => {
          console.log(error);
        }
        // this.data4fig = this.ESRTable
      );
    },
    addItem() {
      this.popupdata = {};
      this.dialogFormVisible = true;
      this.Operation = "Add new project";
    },

    deleteItem(item) {
      // console.log(this.ESRTable.data)
      confirm("Are you sure you want to delete this item?") &&
        this.$axios.post("/api/delitem", item.ID, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        });

      this.ESRTable.splice(item.id - 1, 1);
      this.getData();
      this.dialogDelete = true;
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    editItem(item) {
      this.popupdata = item;
      eval('this.popupdata.DateRange ='+ this.popupdata.DateRange)
      this.dialogFormVisible = true;
      this.Operation = "Edit project";
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