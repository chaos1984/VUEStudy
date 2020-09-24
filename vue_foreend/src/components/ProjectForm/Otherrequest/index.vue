<template>
    <v-form>
      <uploadfile  @getFileName = "getFileName" :data = "uploadinfo1"/>
      <uploadfile  @getFileName = "getFileName" :data = "uploadinfo2"/>
        <stepperbtn :data = "btnsettings"/>
    </v-form>
</template>

<script>
    export default {
        data() {
            return {
                enabled :'false',
      info : '',
      valid: true,
            uploadinfo1 : {
              disabled:false,
              fileList : [],
              inputlabel: 'BOM FILE',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".xls",
              FileRules:[
              v => !!v || 'Required',
                  ],
              Hint : "EX11_BOM_V1.xls",
        },
        uploadinfo2 : {
              disabled:false,
              fileList : [],
              inputlabel: 'CATIA FILE',
              btnlabel : 'upload',
              action : 'api/upload',
              filenum : 1,
              accepttype : ".stp,.x_t,.CatiaPart",
              FileRules:[
                  v => !!v || 'Required',
                  ],
              Hint : "EX11_DABModule_V1.stp",
        },
        btnsettings : {
                ismkdir:false
        },
            }
        },
        methods:{
            getFileName(data){
                console.log("uploadfile:",data)
            return data
      }
   }
    }
</script>

<style lang="scss" scoped>

</style>