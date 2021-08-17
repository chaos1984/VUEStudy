import Vue from 'vue'
import Vuex from 'vuex'

//挂载Vuex
Vue.use(Vuex)

//创建VueX对象
const store = new Vuex.Store({
    state:{
        //存放的键值对就是所要管理的状态
        User:{
          Name:'',
          PassWord:'',  
          Priority:'',
        },
        FormInfo:"",
        NextStepbtn: true,
        CurrentStep: 0,
        StepsNum: 0,
        CurrentMatPage:'',
        form :{
            ESRNumber: '',
            PEName: '',
            TeamName: '',
            ProjectCode:"",
            date1: new Date().toISOString().substr(0, 10),
            date2:"",
            CADFile:"",
            BOMFile:"",
            CushionCarryoverflag:true,
            CushiondwgFile:"",
            CushionFoldFile:"",
            CushionCarryover:"",
            OldCushion:"",
            InflatorCarryoverflag:true,
            InflatorFile:"",
            Inflator:"",
            Case:[true,true,true,false,false,false,false,false,false]
        },
        data4fig:{},
        hovercard:{}
    },
    
    getter:{
        combinFormInfo(state){
            return state.ESRInfo
        }
    },
    mutations:{
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