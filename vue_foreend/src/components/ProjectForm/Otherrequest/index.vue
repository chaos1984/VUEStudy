<template>
    <div>
        <uploadfile :data = "uploadinfo"/>
        <uploadfile :data = "uploadinfo"/>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                uploadinfo : {
                    disabled:false,
                    fileList : [],
                    label : 'upload',
                    action : 'http://127.0.0.1:5000/upload',
                    filenum : 1,
                    accepttype : ".doc",
                    drag : true
        },
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>