<!-- ValidateForm -->
<template>
  <v-form v-model="valid">
    <v-row>
        <v-col mx="4">
          <BasicInfoCard/>
        </v-col>
    </v-row>
    <v-divider/>
    <v-row >
      <v-col
        cols="12"
        md="6"
      >
      <CushionCard/>
      </v-col>
      <v-col
          cols="12"
          md="6"
        >

      <InflatorCard/>
      </v-col>

      <v-col
          cols="12"
          md="6"
        >

          <BomCard/>
      </v-col>

      
      <v-col
          cols="12"
          md="6"
        >

          <CaseCard/>
      </v-col>
    </v-row>

        <!-- <v-alert
      :value = "validate"
      :dense = false
      outlined
      type="error"
    >
       Information is not complete! Please check!
       </v-alert> -->
       <!-- <NextBackbtn></NextBackbtn> -->
    <v-btn
      :disabled="valid"
      color="success"
      class="mr-4"
      
      @click="validate"
    >
      Next
    </v-btn>
    <v-btn class= "mx-5"
      color="primary"
      @click="onBackStep"
      >
      Back
    </v-btn>
  </v-form>
</template>

<script>

  // import {mapState} from 'vuex';
  export default {

    name : 'DABESR',
    components:{
        BasicInfoCard: () => import('./BasicInfoCard/BasicInfoCard'),
        CushionCard: () => import('./CushionCard/CushionCard'),
        InflatorCard: () => import('./InflatorCard/InflatorCard'),
        BomCard: () => import('./BomCard/BomCard'),
        CaseCard: () => import('./CaseCard/CaseCard')
    },
    data: () => ({

      info : '',
      valid: true,

      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      TeamnameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],

      ProjectCodeRules :[
        v => !!v || 'Name is required',
        v => v.length <= 50 || 'Name must be less than 50 characters',
      ],
      // date2: new Date().toISOString().substr(0, 10),
      Date1Rules:[
        v => !!v || 'Name is required',
      ],
      menu1: false,
      menu2: false,
    }),
    // computed:{
    //   ...mapState({
    //     CurrentForm : state => state.form,
    //     }),
    //   },

    methods:{
    validate () {
        this.update()
        this.$store.commit('nextStep')
      },
    onBackStep(){
          this.$store.commit('backStep')
      },
    update(){
        this.$axios.post('/api/RequestForm',JSON.stringify(this.$store.state.form),{headers:{'Content-Type':'application/x-www-form-urlencoded'}})
          .then(res=>{
                console.log(res.data)
          })
          .catch(function (error) {
            console.log(error);
          })
      },  
   }
  }
</script>