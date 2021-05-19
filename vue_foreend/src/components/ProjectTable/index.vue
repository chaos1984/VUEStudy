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

          <v-btn class="mb-2" width="100px" @click.native="SaveData()"
            >Save</v-btn
          >

          <v-btn class="mb-2" width="100px" @click="dialogFormVisible = true"
            >New</v-btn
          >
        </v-toolbar>
      </template>

      <template v-slot:item.actions="{ item }">
        <el-popover placement="right" width="800" trigger="click">
          
          <v-icon small class="mr-2" slot="reference" 
            >mdi-eye</v-icon
          >
          <!-- <DetailInfo :data='item' ></DetailInfo> -->

          <div>
    <el-row
      ><span class="Title">{{ item.PRJ }}</span></el-row >

    <v-divider></v-divider>

    <el-row class="row-bg-light">
      <el-col :span="8"
        ><span>AFIS: </span><span class="Content">{{ item.AFIS }}</span></el-col
      >
      <el-col :span="8"
        ><span>ESR: </span><span class="Content">{{ item.ESR }}</span></el-col
      >
      <el-col :span="8"
        ><span>PE: </span> <span class="Content">{{ item.PE }}</span></el-col
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
      <el-col :span="6"
        ><span>HingeNeck: </span
        ><span class="Content">{{ item.H_Neck }}</span></el-col
      >
    </el-row>

    <el-row class="row-bg-dark">
      <el-col :span="12"
        ><span>Testing: </span
        ><span class="Content">{{ item.Test}}</span></el-col
      >
      <el-col :span="12"
        ><span>Simulation: </span
        ><span class="Content">{{ item.Simulation }}</span></el-col
      >
    </el-row>
  </div>



        </el-popover>
        <!-- <v-icon small class="mr-2" @click="view(item)"> mdi-eye </v-icon> -->
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small class="mr-2" @click="deleteItem(item)">mdi-delete</v-icon>
      </template>

      <template v-slot:no-data>
        <v-btn color="primary">Reset</v-btn>
      </template>
    </v-data-table>

    <DABSVM></DABSVM>

    <el-dialog
      title="New project"
      :visible.sync="dialogFormVisible"
      width="100%"
    >
      <POPUP />
    </el-dialog>

    <!-- <v-overlay :value="overlay">
      <DetailInfo :data="detailInfo"></DetailInfo>
      <v-btn class="white--text" color="teal" @click="overlay = false">
        Close
      </v-btn>
    </v-overlay> -->
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  components: {
    DABSVM: () => import("@/components/DABSVM/DABSVM"),
    POPUP: () => import("@/components/ProjectTable/popup1"),
    // DetailInfo: () => import("@/components/ProjectTable/DetailInfo"),
  },
  data: () => ({
    // data4fig: { failure: [], nofailure: [] },
    overlay: false,
    detailInfo: {},
    dialogFormVisible: false,
    dialog: false,
    dialogDelete: false,
    search: "",
    ESRheaders: [
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
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  mounted() {
    this.getData();
  },
  methods: {
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
          this.CurrentForm["data4fig"] = this.ESRTable;
        },
        (error) => {
          console.log(error);
        }
        // this.data4fig = this.ESRTable
      );
    },

    // view(item) {
    //   // console.log(item);
    //   this.CurrentForm.hovercard = item;
    //   console.log('index');
    //   console.log(this.CurrentForm.hovercard)
    //   // this.overlay = !this.overlay;
    //   // console.log(this.overlay);
    // },

    editItem(item) {
      this.editedIndex = this.ESRTable.data.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = item.id;
      console.log(item.id);
      // console.log(this.ESRTable.data)
      confirm("Are you sure you want to delete this item?") &&
        this.$axios.post("/api/delitem", index, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        });

      this.ESRTable.splice(item.id - 1, 1);
      // this.getData()
      // this.closeDelete()
      // this.dialogDelete = true
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    //   closeDelete () {
    //     this.dialogDelete = false
    //     this.$nextTick(() => {
    //       this.editedItem = Object.assign({}, this.defaultItem)
    //       this.editedIndex = -1
    //     })
    //   },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.ESRTable.data[this.editedIndex], this.editedItem);
      } else {
        this.ESRTable.data.push(this.editedItem);
      }
      console.log(this.ESRTable.data);
      this.close();
    },
    //   SaveData() {
    //       this.$axios.get("/api/ProjectTable",{
    //       params:{
    //         ProjectTableData : JSON.stringify(this.ESRTable.data)
    //       }
    //       })
    //       .then(
    //         response => {
    //           console.log(response);
    //         },
    //         error => {
    //           console.log(error);
    //         }
    //       );
    // },
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