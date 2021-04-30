<template>
  <div>


      <v-card>
        <v-card-title>
          <span>New DAB Project</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="3" >
                <v-text-field
                  v-model="editedItem.name"
                  label="Prj. name"
                ></v-text-field>
              </v-col>
              <v-col cols="3" >
                <v-text-field
                  v-model="editedItem.ESR"
                  label="ESR"
                ></v-text-field>
              </v-col>
              <v-col cols="3" >
                <v-text-field v-model="editedItem.PE" label="PE"></v-text-field>
              </v-col>
              <v-col cols="3" >
                <v-text-field
                  v-model="editedItem.covermat"
                  label="Cover Mat."
                ></v-text-field>
              </v-col>
              <v-col cols="3" >
                <v-text-field
                  v-model="editedItem.hingewidth"
                  label="Hinge width"
                ></v-text-field>
              </v-col>
              <v-col cols="3" >
                <v-text-field
                  v-model="editedItem.hingewidth"
                  label="Hinge width"
                ></v-text-field>
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
  </div>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
    },
  }),
  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  methods: {
    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
    save() {
      this.close();
    },
  },
};
</script>

<style lang="scss">
</style>