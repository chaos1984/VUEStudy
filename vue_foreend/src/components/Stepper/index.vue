<!-- Stepper -->
<template>
  <div>

    <v-stepper v-model="$store.state.CurrentStep">
      <v-stepper-header>
        <template v-for="(title,n) in stepsNames">
          <v-stepper-step
            :key="`${n}-step`"
            :complete="e1 > n"
            :step="n"
          >
            {{title.title}}
          </v-stepper-step>

          <v-divider
            v-if="n !== steps"
            :key="n"
          ></v-divider>
        </template>
      </v-stepper-header>
    
      <v-stepper-items>
        <v-stepper-content
          v-for="(title,n) in stepsNames"
          :key="`${n}-content`"
          :step="n"
        >
           <v-main  class="d-flex pa-2">
                <component :is="getCurrentForm" ></component>
            </v-main>

        </v-stepper-content>
      </v-stepper-items>
      
    </v-stepper>
  </div>
</template>

<script>
  export default {
    components:{
        ProjectForm: () => import('@/components/ProjectForm/BasicInfo'),
        RequestInfo: () => import('@/components/ProjectForm/RequestInfo'),
        Otherrequest:() => import('@/components/ProjectForm/Otherrequest'),
        RequestForm: () => import('@/components/ProjectForm/RequestForm'),
    },
    data () {
      return {
        e1: "",
        stepsNames:[{title:'Basic Information'},{title:'Request Information'},{title:'Other Request'},{title:'Request Form'}],
        steps:'',
        Forms: ['ProjectForm','RequestInfo','Otherrequest','RequestForm'],
        CurrentForm:""
      }
    },
    computed:{
       getCurrentForm:function(){
            return this.Forms[this.$store.state.CurrentStep]
        }
    },
    mounted(){
      this.getLength()
    },
    methods: {
      getLength(){
        this.steps = Object.keys(this.stepsNames).length
        this.$store.commit('getStepsNum',this.steps)
      },

    },
  }
</script>