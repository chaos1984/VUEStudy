<template>
	<div>
		<pdfviewer :data="PDFSettings"/>
	</div>
</template>

<script>
	import {mapState} from 'vuex';
	export default {
		data() {
			return {
				PDFSettings:{
					url:"./static/",
					downlenable:false
				}
			}
		},
	computed:{
		...mapState({CurrentForm : state => state.form,})
	},
	created: function() {
			this.getPDFurl()
		},
	methods: {
		getPDFurl(){
			this.PDFSettings.url = this.PDFSettings.url + this.CurrentForm.CurrentMatPage  + '.pdf'
			console.log(this.PDFSettings.url )
		},
	},
	}
</script>

<style lang="scss" scoped>

</style>