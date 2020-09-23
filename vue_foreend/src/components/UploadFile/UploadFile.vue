<template>

    <v-container fluid>
      <v-row>
        <v-col
          cols="12"
          md="8"
        >
          <v-text-field
            :value = "filename"
            :label = "uploadinfo.inputlabel"
            :rules = "uploadinfo.FileRules"
            :hint = "uploadinfo.Hint"
            persistent-hint
            outlined
            filled
            readonly
            dense
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
    <el-upload
    :disabled = "uploadinfo.disabled"
    :label = "uploadinfo.btnlabel"
    :action = "uploadinfo.action"
    :on-preview = "handlePreview"
    :on-remove = "handleRemove"
    :on-success = "emitfilename"
    :before-remove = "beforeRemove"
    :before-upload = "beforeUpload"
    multiple
    :accept = "uploadinfo.accepttype"
    :limit= "uploadinfo.filenum"
    :on-exceed = "handleExceed"
    :file-list = "uploadinfo.fileList"
    >
    <el-button size="small" type="primary">UPLOAD</el-button>
   <!-- <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div> -->
    <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
    </el-upload>  
    </v-col>
          </v-row>
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
    data() {
      return {
        valid: true,
        filename :'',
        uploadinfo : {
          disabled: true,
          fileList : [],
          inputlabel:'',
          btnlabel : '',
          action : '',
          filenum : 1,
          accepttype : "",
          FileRules:[],
          Hint:'',
        },

 
      }
    },

    methods: {
      handleRemove(file) {
        this.filename = ""

        this.$axios.post('/api/delete',file.name ) //请求头要为表单
          .then(response=>{
            console.log(response.data);
          })
          .catch(function (error) {
            console.log(error);
          })
      },
      handlePreview(file) {
        console.log(file);
      },
      handleExceed(files, fileList) {
        this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
      },
      beforeRemove(file) {
        return this.$confirm(`确定移除 ${ file.name }？`);
      },
      beforeUpload(file) {
        this.filename = file.name
        return this.$confirm(`确定上传 ${ file.name }？`);
      },
      printuploadinfo(){
        console.log(this.uploadinfo)
      },
      emitfilename(){
        this.$emit('getFileName',this.filename)
      },
      
    },
    mounted () {
      this.uploadinfo = this.data
      this.printuploadinfo;

    },
    created () {
      this.printuploadinfo;
    },
  }
</script>