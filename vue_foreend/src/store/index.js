import Vue from 'vue'
import Vuex from 'vuex'

//挂载Vuex
Vue.use(Vuex)

//创建VueX对象
const store = new Vuex.Store({
    state:{
        //存放的键值对就是所要管理的状态
        ESRInfo:'helloVueX',
        FormInfo:"",
        NextStepbtn: true,
        CurrentStep: 0,
        StepsNum: 0
    },
    getter:{
        combinFormInfo(state){
            return state.ESRInfo
        }
    },
    mutations:{
        edit(state,info){
            state.ESRInfo = state.ESRInfo + info
        },
        getStepsNum (state,val){
            state.StepsNum = val 
        },
        nextStep(state){
            if (state.CurrentStep < state.StepsNum-1){
            state.CurrentStep += 1
            } else {
                state.CurrentStep = state.StepsNum-1
            }
        },
        backStep(state){
            if (state.CurrentStep > 0){
                state.CurrentStep -= 1
            } else {
                state.CurrentSte = 0
            }
        },
        isNextStep(state){
             state.NextStepbtn = false
        },
        noNextStep(state){
             state.NextStepbtn = true
        }
    }
})

export default store