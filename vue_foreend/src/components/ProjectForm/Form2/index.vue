<!-- ValidateForm -->

<template>
  <v-container id="dropdown-example">
    <v-row>
      <v-col cols="12" sm="4">
        <p>Overflow</p>

        <v-overflow-btn
          class="my-2"
          :items="dropdown_font"
          label="Overflow Btn"
          target="#dropdown-example"
        ></v-overflow-btn>
      </v-col>

      <v-col cols="12" sm="4">
        <p>Segmented</p>

        <v-overflow-btn
          class="my-2"
          :items="dropdown_icon"
          label="Segmented Btn"
          segmented
          target="#dropdown-example"
        ></v-overflow-btn>
      </v-col>

      <v-col cols="12" sm="4">
        <p>Editable</p>

        <v-overflow-btn
          class="my-2"
          :items="dropdown_edit"
          label="Editable Btn"
          editable
          item-value="text"
        ></v-overflow-btn>
      </v-col>
    </v-row>

    <v-alert
      :value = "isError"
      :dense =false
      outlined
      type="error"
    >
       Information is not complete! Please check!
       </v-alert>
       <NextBackbtn></NextBackbtn>
         </v-container>
</template>


<script>
  export default {
    name : 'projectform1',
    components:{
        NextBackbtn: () => import('../NextBackbtn'),
    },
    data: () => ({
      dropdown_font: ['Arial', 'Calibri', 'Courier', 'Verdana'],
      dropdown_icon: [
        { text: 'list', callback: () => console.log('list') },
        { text: 'favorite', callback: () => console.log('favorite') },
        { text: 'delete', callback: () => console.log('delete') },
      ],
      dropdown_edit: [
        { text: '100%' },
        { text: '75%' },
        { text: '50%' },
        { text: '25%' },
        { text: '0%' },
      ],
    }),
    computed:{
        isError:function(){
        if (this.ProjectName != '' && this.PEName != '' && this.email != ''){
            this.$store.commit('isNextStep')
            return false
        } else {
            this.$store.commit('noNextStep')
            return true
            }
         }
    },
    methods:{

   }
  }
</script>