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
                <ProjectForm1 />
            </v-main>

        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
  export default {
    components:{
        ProjectForm1: () => import('@/components/ProjectForm1'),
    },
    data () {
      return {
        e1: "",
        stepsNames:[{title:'项目录入'},{title:'分析内容'},{title:'特殊分析'},{title:'截至时间'}],
        steps:'',
      }
    },

    mounted(){
      this.getLength()
    },
    methods: {
      getLength(){
        this.steps = Object.keys(this.stepsNames).length
        this.$store.commit('getStepsNum',this.steps)
        console.log(this.$store.state.StepsNum)
      },
    },
  }
</script>