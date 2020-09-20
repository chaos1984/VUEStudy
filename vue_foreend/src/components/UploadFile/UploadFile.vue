<template>
    <el-upload
    :disabled = "uploadinfo.disabled"
    :label="uploadinfo.label"
    :action="uploadinfo.action"
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :before-remove="beforeRemove"
    :before-upload = "beforeUpload"
    multiple
    :accept = "uploadinfo.accepttype"
    :limit= "uploadinfo.filenum"
    :on-exceed="handleExceed"
    :file-list="uploadinfo.fileList">
    <el-button size="small" type="primary">UPLOAD</el-button>
   <!-- <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div> -->
    <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
    </el-upload>   
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

        uploadinfo : {
          disabled: true,
          fileList : [],
          label : '',
          action : '',
          filenum : 1,
          accepttype : ""
        },
      }
    },
    methods: {
      handleRemove(file, fileList) {
        console.log(file.name, fileList);
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
        return this.$confirm(`确定上传 ${ file.name }？`);
      },
      printuploadinfo(){
        console.log(this.uploadinfo)
      }
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