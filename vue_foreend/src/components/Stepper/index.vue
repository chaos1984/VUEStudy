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
        ProjectForm1: () => import('@/components/ProjectForm/Form1'),
        ProjectForm2: () => import('@/components/ProjectForm/Form2'),
        ProjectForm3: () => import('@/components/ProjectForm/Form3'),
        ProjectForm4: () => import('@/components/ProjectForm/Form4'),
    },
    data () {
      return {
        e1: "",
        stepsNames:[{title:'项目录入'},{title:'分析内容'},{title:'特殊分析'},{title:'截至时间'}],
        steps:'',
        Forms: ['ProjectForm1','ProjectForm2','ProjectForm3','ProjectForm4'],
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