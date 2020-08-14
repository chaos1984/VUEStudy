<template>
<div>
<v-btn class= "mx-5"
    :disabled = "$store.state.NextStepbtn"
    color="primary"
    @click="onNextStep"
>
Next
</v-btn>

<v-btn class= "mx-5"
    color="primary"
    @click="onBackStep"
    >
    Back
</v-btn>

</div>
</template>

<script>
  export default {
    methods:{
      onNextStep(){
          this.$store.commit('nextStep')
      },
     onBackStep(){
          this.$store.commit('backStep')
      },
    }
  }
</script>
