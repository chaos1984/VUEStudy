<template>
    <div>
	<v-card >
		<pdf ref="pdf" 

		:src="url" 
		:page="pageNum"
		:rotate="pageRotate"  
		@progress="loadedRatio = $event"
		@page-loaded="pageLoaded($event)" 
		@num-pages="pageTotalNum=$event" 
		@error="pdfError($event)" 
		@link-clicked="page = $event">
		</pdf>
        

	</v-card>
            <v-container>
            <v-row>
                <v-spacer/>
                <v-btn class="ma-2" color="orange darken-2" dark @click.stop="prePage">
                <v-icon dark left>mdi-arrow-left</v-icon>Back
                </v-btn>
                <p class="ma-4" >{{pageNum}}/{{pageTotalNum}} </p>
                <v-btn class="ma-2" color="green darken-2" dark @click.stop="nextPage">
                <v-icon dark left>mdi-arrow-right</v-icon>NEXT
                </v-btn>
                <v-spacer/>
            </v-row>
        </v-container>
    </div>
</template>

<script>
	import pdf from 'vue-pdf'
	export default {
		name: 'Home',
		components: {
			pdf
		},
		data() {
			return {
				url: "./static/www.pdf",
				pageNum: 1,
				pageTotalNum: 1,
				pageRotate: 0,
				// 加载进度
				loadedRatio: 0,
				curPageNum: 0,
			}
		},
		mounted: function() {},
		methods: {
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
		}
	}
</script>
