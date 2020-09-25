<template>
    <div>
	<v-card class='mx-10'>
	<el-button :disabled="PDFSettings.downlenable" size='mini' type="success" @click='downloadPDF'>Dowload PDF</el-button>
		
		<v-container >
		<v-spacer/>
		<v-row>
		<pdf ref="pdf" 
			
		:src="PDFSettings.url" 
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
		</v-row>
		<v-spacer/>
		</v-container>
              <v-container>
            <v-row>
                <v-spacer/>
                <v-btn class="mx-1" color="orange darken-2" dark @click.stop="prePage">
                <v-icon dark left>mdi-arrow-left</v-icon>
                </v-btn>
                <p class="ma-2" >{{pageNum}}/{{pageTotalNum}} </p>
                <v-btn class="mx-1" color="green darken-2" dark @click.stop="nextPage">
                <v-icon dark left>mdi-arrow-right</v-icon>
                </v-btn>
                <v-spacer/>
            </v-row>
        </v-container>  

	</v-card>


    </div>
</template>

<script>
	import pdf from 'vue-pdf';
	export default {
		props: {
            data: {
            default () {
                return []
                },
                type: Object
                },

        },
		components: {
			pdf
		},
		data() {
			return {
                PDFSettings:{
                    url:"",
                    downlenable:true
                },
				
				pageNum: 1,
				pageTotalNum: 1,
				pageRotate: 0,
				// 加载进度
				loadedRatio: 0,
				curPageNum: 0,
			}
		},
		created: function() {
			this.PDFSettings = this.data

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
			downloadPDF(){
				window.open(this.PDFSettings.url, '_blank');
			}
		}
	}
</script>
