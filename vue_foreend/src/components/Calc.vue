<template>
  <v-form>
    <v-container>
      <v-row>

        <v-col cols="12" sm="6" md="3">
          <v-text-field v-model="a"
            label="Regular"
          ></v-text-field>
        </v-col>

        <v-col cols="12" sm="6" md="3">
          <v-text-field v-model= "b"
            label="Regular"
            placeholder="Placeholder"
          ></v-text-field>
        </v-col>

      <div class="my-2">
        <v-btn small color="primary" @click.native="onadd()">Primary</v-btn>
		<h2>sum:{{sum}}</h2>

      </div>


      </v-row>
    </v-container>
  </v-form>
</template>

<script>

export default {

   data() {
       return {
        sum:'',
       };
     },


    methods:{
     onadd() {
        this.$axios
       .get("/api/addnumber",{
            params:{
                a:this.a,
                b:this.b
            }
})
      .then(res =>{console.log(res.data)
            this.sum = res.data.result
//       .then(res.data =>{((a)
       })
       }
  }

};
</script>

