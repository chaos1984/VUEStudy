<template>
  <v-data-table
   :headers="headers" :items="desserts" :items-per-page="5" class="elevation-12 ma-1 ">
      <!-- <template v-slot:top> -->
      <!-- <v-switch v-model="singleSelect" label="Single select" class="pa-1"></v-switch> -->
    <!-- </template> -->
    <template v-slot:item.action="{ item }">
          <v-icon small  class="mr-2"  @click.native="editPlan(item,true)">
                  编辑
          </v-icon>
         <v-icon small  class="mr-2"  @click.native="editPlan(item,false)">
                  查看
         </v-icon>
         <v-icon  small  @click.native="deletePlan(item)" >
                  删除
        </v-icon>
</template>
  </v-data-table>
</template>




<script>
import axios from "axios";
export default {
  data() {
    return {
      headers: [
        {
          text: "Author",
          align: "start",
          sortable: false,
          value: "name"
        },
        { text: "Calories", value: "calories" },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" },
        { text: "Option",value:'action',sortable:false}
      ],
      desserts: []
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
        this.$axios
       .get("/api/writejson",{
            params:{
               data:this.desserts
            }
})
      .then(res =>{console.log(res.data)
            this.sum = res.data.result
//       .then(res.data =>{((a)
       })
       }
    }
  }
};
</script>