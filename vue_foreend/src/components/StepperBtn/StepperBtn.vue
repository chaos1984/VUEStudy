<template>
    <v-container>
        <v-btn
        :disabled="!valid"
        color="success"
        class="ma-4"
        
        @click="validate"
        >
        Next
        </v-btn>
        <v-btn class= "ma-4"
        color="primary"
        @click="onBackStep"
        >
        Back
        </v-btn>
    </v-container>
</template>
<script>

export default {
    props: {
      data: {
        default () {
          return []
        },
        type: Object
      },

    },
    data: () => ({
        valid: true,
        filename :'',
        settings : {
          ismkdir:false,     
        }
    }),
    

    methods:{
      makedir(){
        this.$axios.post('/api/makedir',JSON.stringify(this.$store.state.form),{headers:{'Content-Type':'application/x-www-form-urlencoded'}})
          .then(res=>{
                console.log(res.data)
          })
          .catch(function (error) {
            console.log(error);
          })
      },
      validate () {
          if (this.settings.ismkdir === true){
          this.makedir()
          }
          this.$store.commit('nextStep')

        },
      onBackStep(){
          this.$store.commit('backStep')
        },
   }
  }
</script>