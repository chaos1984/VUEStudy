<template>
    <div>
	<el-button :disabled="false" size='mini' type="success" @click='downloadPDF'>Dowload PDF</el-button>
	<v-card >
		<pdf ref="pdf" 

		:src = "PDFfile" 
		:page="pageNum"
		:rotate="pageRotate"  
		@progress="loadedRatio = $event"
		@page-loaded="pageLoaded($event)" 
		@num-pages="pageTotalNum=$event" 
		@error="pdfError($event)" 
		@link-clicked="page = $event"
		:style="{ width: 100+ '%' }"
		>
		</pdf>
	</v-card>
        <v-container>
            <v-row>
                <v-spacer/>
                <v-btn class="ma-1" color="orange darken-2" dark @click.stop="prePage">
                <v-icon dark left>mdi-arrow-left</v-icon>
                </v-btn>
                <p class="ma-4" >{{pageNum}}/{{pageTotalNum}} </p>
                <v-btn class="ma-1" color="green darken-2" dark @click.stop="nextPage">
                <v-icon dark left>mdi-arrow-right</v-icon>
                </v-btn>
                <v-spacer/>
            </v-row>
        </v-container>
    <v-btn class= "mx-5"
      color="primary"
      @click="onBackStep"
      >
      Back
    </v-btn>
	
    </div>
	
</template>




<script>
	import {mapState} from 'vuex';
	import pdf from 'vue-pdf';
	
	export default {
		name: 'Home',
		components: {
			pdf
		},
		data() {
			return {
				PDFfile:'',
				pageNum: 1,
				pageTotalNum: 1,
				pageRotate: 0,
				// 加载进度
				loadedRatio: 0,
				curPageNum: 0,
			}
		},

        created() {
			this.postRequest()
        },
		computed:{
			...mapState({CurrentForm : state => state.form,})
        },
		methods: {
            onBackStep(){
				
                this.$store.commit('backStep')
             },
            // 上一页函数，
			prePage() {
				var page = this.pageNum
				page = page > 1 ? page - 1 : this.pageTotalNum
				this.pageNum = page
			},
            // 下一页函数
			nextPage() {
				var page = this.pageNum
				page = page < this.pageTotalNum ? page + 1 : 1
				this.pageNum = page
			},
            // 页面顺时针翻转90度。
			clock() {
				this.pageRotate += 90
			},
            // 页面逆时针翻转90度。
			counterClock() {
				this.pageRotate -= 90
			},
            // 页面加载回调函数，其中e为当前页数
			pageLoaded(e) {
				this.curPageNum = e
			},
            // 其他的一些回调函数。
			pdfError(error) {
				console.error(error)
			},
			// getPDFurl(){
			// 	// this.url = this.url + this.CurrentForm.ESRNumber +'/' + this.CurrentForm.ESRNumber + '_' + this.CurrentForm.date1 + '.pdf'
			// 	this.url = this.url + this.CurrentForm.ESRNumber +'/' + this.CurrentForm.ESRNumber + '_' + this.CurrentForm.date1 + '.pdf'
			// 	console.log(this.url)
			// 	console.log(window.location.href)
			// },
			postRequest(){
				this.$axios.post('/api/RequestForm',JSON.stringify(this.$store.state.form),{headers:{'Content-Type':'application/x-www-form-urlencoded'}})
					.then(res=>{
						const blob = this.base64ToBlob(res.data,'application/pdf')
						this.PDFfile= window.URL.createObjectURL(blob)
							})
					.catch(function (error) {
						console.log(error);
						})
				},

			base64ToBlob(b64Data, contentType='', sliceSize=512) {
				const byteCharacters = atob(b64Data);
				const byteArrays = [];

				for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
					const slice = byteCharacters.slice(offset, offset + sliceSize);

					const byteNumbers = new Array(slice.length);
					for (let i = 0; i < slice.length; i++) {
					byteNumbers[i] = slice.charCodeAt(i);
					}

					const byteArray = new Uint8Array(byteNumbers);
					byteArrays.push(byteArray);
				}

				const blob = new Blob(byteArrays, {type: contentType});
				return blob;
				},
			downloadPDF(){
				// location.href =  this.url
				let routeData = this.$router.resolve({

				});
				routeData.url = this.PDFfile
				
				window.open(routeData.url, '_blank');
			}
		}
	}
</script>


