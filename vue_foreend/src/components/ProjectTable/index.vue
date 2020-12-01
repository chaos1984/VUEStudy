<template>


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
          label="Search (UPPER CASE ONLY)"
          class="mx-4"
        ></v-text-field>
        <!-- <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider> -->
        
        <!-- <v-spacer></v-spacer>
        <v-btn  class="mb-2" width="100px" @click.native="SaveData()">Save</v-btn> -->
        
        <v-dialog v-model="dialog" max-width="500px">
        
          <!-- <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >New Item</v-btn>
            
          </template> -->
          
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.name" label="Dessert name"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.calories" label="Calories"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.fat" label="Fat (g)"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.carbs" label="Carbs (g)"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.protein" label="Protein (g)"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>

        </v-dialog>



      </v-toolbar>
      
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
      
    </template>
    
    <template v-slot:no-data>
      <v-btn color="primary">Reset</v-btn>
    </template>
    
  </v-data-table>

  
</template>

<script>

// import qs from 'qs'
  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      search: '',
      ESRheaders: [
        {
          text: 'Prj',
          align: 'start',
          sortable: false,
          value: 'PRJ',
        },
        {text:  'ESR',value: 'ESR'},
        { text: 'PE', value: 'PE' },
        { text: 'Interface', value: 'Interface' },
        { text: 'C_Mat.', value: 'CV_Mat' },
        { text: 'H_Mat', value: 'H_Mat' },
        { text: 'E_Mat', value: 'E_Mat' },
        { text: 'Inflator', value: 'Inflator' },
        { text: 'C_Mat', value: 'C_Mat' },
        { text: 'C_type', value: 'C_Type' },
        { text: 'C_Diam', value: 'C_Diam' },
        { text: 'Tearline', value: 'Tearline' },
        { text: 'Flappy Mass', value: 'Flappy_Mass' },
        { text: 'H_width', value: 'H_Width' },
        { text: 'H_Plane', value: 'H_Plane' },
        { text: 'H_Neck', value: 'H_Neck' },
        { text: 'Option', value: 'actions', sortable: false },
      ],
      ESRTable: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      filter: value => {
              if (!this.ESR) return true

              return value < parseInt(this.ESR)
            },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    mounted() {
      this.getData();
     },
    methods: {
      filterOnlyCapsText (value, search) {
        return value != null &&
          search != null &&
          typeof value === 'string' &&
          value.toString().indexOf(search) !== -1
      },
      getData() {
        this.$axios.get("/api/getdatabase").then(
        response => {
          // console.log(response.data);
          // this.ESRTable.data = JSON.parse(response.data);
          this.ESRTable = response.data;
          console.log(this.ESRTable)
          // console.log('look')
          // console.log(this.ESRTable.data)
        },
        error => {  
          console.log(error);
        }
      );
    },

      editItem (item) {
        this.editedIndex = this.ESRTable.data.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = item.id
        console.log(item.id)
        console.log(this.ESRTable)
        // console.log(this.ESRTable.data)
        confirm('Are you sure you want to delete this item?') && this.$axios.post('/api/delitem',index,{headers:{'Content-Type':'application/x-www-form-urlencoded'}})
        
        this.ESRTable.splice(item.id-1, 1)
        // this.getData()
        // this.closeDelete()
        // this.dialogDelete = true
      },


     close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

    //   closeDelete () {
    //     this.dialogDelete = false
    //     this.$nextTick(() => {
    //       this.editedItem = Object.assign({}, this.defaultItem)
    //       this.editedIndex = -1
    //     })
    //   },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.ESRTable.data[this.editedIndex], this.editedItem)
        } else {
          this.ESRTable.data.push(this.editedItem)
        }
        console.log(this.ESRTable.data)
        this.close()
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
  }
</script>

<style scoped>

</style>