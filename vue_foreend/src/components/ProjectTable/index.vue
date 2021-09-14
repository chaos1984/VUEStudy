<template>
  <div>
    <v-data-table
      v-model="selectedItem"
      :headers="ESRheaders"
      :items="ESRTable"
      :items-per-page="5"
      class="elevation-1"
      multi-sort
      :search="search"
      item-key="PRJ"
      show-select
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

          <div class = "row-bg-light">
            <el-row
              ><span class="Title">{{ item.PRJ }}</span></el-row
            >

            <!-- <v-divider class= 'divider'></v-divider> -->

            <el-row >
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
                ><span>Hinge Length: </span
                ><span class="Content">{{ item.Hinge_Width }} mm</span></el-col
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
                ><span class="Content">{{ item.DateRange }}</span></el-col
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

        <el-tooltip
          class="item"
          effect="dark"
          content="Modify"
          placement="top-end"
        >
          <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
            :disabled="Permission(item.PE)"
          >
            mdi-pencil
          </v-icon>
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="Delete"
          placement="top-end"
        >
          <v-icon
            small
            class="mr-2"
            @click="deleteItem(item)"
            :disabled="Permission(item.PE)"
            >mdi-delete</v-icon
          >
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="Log"
          placement="top-end"
        >
          <v-icon small class="mr-2" @click="logItem(item)"
            >el-icon-notebook-1</v-icon
          >
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="ESR Requirest"
          placement="top-end"
        >
          <v-icon small class="mr-2" @click="postRequest(item)"
            >el-icon-tickets</v-icon
          >
        </el-tooltip>

        <el-tooltip
          class="item"
          effect="dark"
          content="CAE Report"
          placement="top-end"
        >
          <v-icon small class="mr-2" @click="CAEReport(item)"
            >el-icon-data-analysis</v-icon
          >
        </el-tooltip>
      </template>
    </v-data-table>

    <el-drawer   :visible.sync="drawerVisable" :with-header="false" size="50%" class= "el-drawer">
      <!-- <span>{{test}}</span> -->
      <LOG :getdata="itemdata" ></LOG>
    </el-drawer>

    <el-dialog
      :title="Operation"
      :visible.sync="dialogFormVisible"
      width="100%"
    >
      <POPUP :form="popupdata"></POPUP>
    </el-dialog>



    <el-divider />
    <div>
      <el-row :gutter="0">
        <el-col :lg="8" :xs="24"><DABSVM :getdata="ESRTable" /></el-col>
        <el-col :lg="8" :xs="24"><Radar :getdata="selectedItem" /></el-col>
        <el-col :lg="8" :xs="24"><StatisticsPie :getdata="ESRTable" /></el-col>
      </el-row>
    </div>
    <el-divider />
    <ESRCalendars :getdata="ESRTable" />
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  components: {
    DABSVM: () => import("@/components/Echart/DABSVM"),
    StatisticsPie: () => import("@/components/Echart/StatisticsPie"),
    POPUP: () => import("@/components/ProjectTable/popup"),
    LOG: () => import("@/components/ProjectTable/log"),
    ESRCalendars: () => import("@/components/ProjectTable/ESRCalendars"),
    Radar: () => import("@/components/Echart/Radar.vue"),
    // CAEReportpopup:() => import("@/components/Echart/CAEReportpopup"),
  },
  data: () => ({
    pptfiledir: "",
    singleSelect: false,
    selectedItem: [],
    itemdata: "",
    PDFfile: "",
    forminital: {
     OEM: "",
     PRJ: "",
     AFIS: "",
     ESR: "",
     PE: "",
     Interface: "",
     CV_Mat: "",
     H_Mat: "",
     HousingMat: "",
     Tearline: "",
     E_Mat: "",
     Inflator: "",
     C_Mat: "",
     C_Type: "",
     C_Diam: "",
     C_Tether: "",
     H_Width: "",
     Flappy_Mass: "",
     Wrapper: "",
     H_Plane: "",
     H_Neck: "",
     Daokou: "",
     C_Diffusor: "",
     DateRange: "",
     Remarks:"None",
     Testing: ["Hinge Overtear", "Emblem Breakage"],
     Simulation: ["Hinge Overtear", "Emblem Breakage"],
     CV_Leather: "",
     CV_Height: "",
     Originator:"",
     Log: [],
   },
    Operation: "Project",
    popupdata: {},
    overlay: false,
    detailInfo: {},
    dialogFormVisible: false,
    CAEReportVisible: false,
    drawerVisable: false,
    dialog: false,
    dialogDelete: false,
    search: "",
    ESRheaders: [
      // {
      //   text: "ID",
      //   value: "ID",
      // },
      {
        text: "Prj",
        align: "start",
        sortable: false,
        value: "PRJ",
      },
      { text: "ESR", value: "ESR" },
      { text: "PE", value: "PE" },
      // { text: "CAE", value: "CAE" },
      // { text: "Interface", value: "Interface" },
      { text: "Cover Mat.", value: "CV_Mat" },
      // { text: "H_Mat", value: "H_Mat" },
      // { text: "E_Mat", value: "E_Mat" },
      // { text: "Inflator", value: "Inflator" },
      // { text: "C_Mat", value: "C_Mat" },
      // { text: "C_type", value: "C_Type" },
      { text: "Cushion Diam", value: "C_Diam" },
      // { text: "Tearline", value: "Tearline" },
      { text: "Flap Mass", value: "Flappy_Mass" },
      { text: "Hinge Width", value: "Hinge_Width" },
      // { text: "H_width", value: "H_Width" },
      { text: "Cover-Inflator Height", value: "CV_Height" },
      { text: "Hinge Area", value: "Hinge_Area" },
      { text: "Hinge H/L", value: "Hinge_HLratio" },
      // { text: "H_Plane", value: "H_Plane" },
      // { text: "H_Neck", value: "H_Neck" },
      { text: "Option", value: "actions", sortable: false },
      
    ],
    ESRTable: [],
    editedIndex: -1,
  }),

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
    Permission(name) {
      // console.log( name)
      if (this.User.Priority != 1) {
        return this.User.Name === name ? false : true;
      } else {
        return false;
      }
    },
    cleardrawer() {
      this.itemdata = {};
    },
    closepopup(val) {
      this.dialogFormVisible = val;
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
          // console.log("this.ESRTable")
          // console.log(typeof(this.ESRTable.Simulation))
        },
        (error) => {
          console.log(error);
        }
        // this.data4fig = this.ESRTable
      );
    },
    addItem() {
      this.popupdata = this.forminital;

      this.dialogFormVisible = true;
      this.Operation = "Add new project";
    },

    editItem(item) {
      this.popupdata = item;
      eval("this.popupdata.Simulation =" + this.popupdata.Simulation);
      eval("this.popupdata.Testing =" + this.popupdata.Testing);
      eval("this.popupdata.DateRange =" + this.popupdata.DateRange);
      this.dialogFormVisible = true;
      this.Operation = "Edit project";
    },

    deleteItem(item) {
      // console.log(this.ESRTable.data)
      confirm("Are you sure you want to delete this item?") &&
        this.$axios.post("/api/delitem", item.ID, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        });
      
      this.ESRTable.splice(item.id - 1, 1);
      this.dialogDelete = true;
      this.getData();
    },

    logItem(item) {
      // console.log(this.ESRTable.data)
      this.drawerVisable = true;
      this.itemdata = item;
    },

    CAEReport(item) {
      window.open(item.PPT, "_blank");
    },
    
  



    postRequest(item) {
      // console.log(item.PE)
      this.$axios
        .post("/api/RequestForm", JSON.stringify(item), {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        })
        .then((res) => {
          let blob = this.base64ToBlob(res.data, "application/pdf");
          this.PDFfile = window.URL.createObjectURL(blob);
          window.open(this.PDFfile, "_blank");
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    base64ToBlob(b64Data, contentType = "", sliceSize = 512) {
      const byteCharacters = atob(b64Data);
      const byteArrays = [];

      for (
        let offset = 0;
        offset < byteCharacters.length;
        offset += sliceSize
      ) {
        const slice = byteCharacters.slice(offset, offset + sliceSize);

        const byteNumbers = new Array(slice.length);
        for (let i = 0; i < slice.length; i++) {
          byteNumbers[i] = slice.charCodeAt(i);
        }

        const byteArray = new Uint8Array(byteNumbers);
        byteArrays.push(byteArray);
      }

      const blob = new Blob(byteArrays, { type: contentType });
      return blob;
    },
  },
};
</script>

<style lang="scss" >
.el-row {
  margin-bottom: 20px;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
}
.el-drawer{
    overflow: scroll;
    }
.row-bg-light
    {
  color:rgb(255, 255, 255);
  background:#74a4e7;
  padding: 10px;
}
.Title{
  color:rgb(0, 0, 0);
  font-size: 20px; 
}
.divider{
  $divider-inset-margin:72px;
}
</style>