<template>
  <div>

    <v-stepper v-model="e1">
      <v-stepper-header>
        <template v-for="(title,n) in stepsNames">
          <v-stepper-step
            :key="`${n}-step`"
            :complete="e1 > n"
            :step="n"
            editable
          >
            {{title.title}}{{kk}}
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
            <!-- <appmain/> -->
                <ValidateForm />
            </v-main>

          <v-btn
            color="primary"
            @click="nextStep(n)"
          >
            Continue
          </v-btn>

          <v-btn text>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
  export default {
    components:{
        ValidateForm: () => import('@/components/ValidateForm'),
    },
    data () {
      return {
        kk :'',
        e1: 1,
        stepsNames:[{title:'项目录入'},{title:'分析内容'},{title:'特殊分析'},{title:'截至时间'}],
        steps:''
      }
    },

    watch: {
      steps (val) {
        if (this.e1 > val) {
          this.e1 = val
        }
      },
    },
mounted(){
  this.getLength()
},
    methods: {
      getLength(){
      this.steps = Object.keys(this.stepsNames).length
      console.log(this.steps)
      },
      nextStep (n) {
        if (n === this.steps) {
          this.e1 = 1
        } else {
          this.e1 = n + 1
        }
      },
    },
  }
</script>