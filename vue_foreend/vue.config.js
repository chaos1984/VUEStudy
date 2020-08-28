module.exports = {
      // 公共路径(必须有的)
      publicPath: "./",
      // // 输出文件目录
      outputDir: "templates",
      // // 静态资源存放的文件夹(相对于ouputDir)
      assetsDir: "static",
      // eslint-loader 是否在保存的时候检查(果断不用，这玩意儿我都没装)
      // lintOnSave:false,
      // 我用的only，打包后小些
      // compiler: false,
     // productionSourceMap: true, // 不需要生产环境的设置false可以减小dist文件大小，加速构建
      // css相关配置(我暂时没用到)
      // css: {
      // 是否使用css分离插件 ExtractTextPlugin
      // extract: true,
      // 开启 CSS source maps?
      // sourceMap: false,
      // css预设器配置项
      // loaderOptions: {},
      // 启用 CSS modules for all css / pre-processor files.
      // modules: false
      // },
      // webpack-dev-server 相关配置
        
    // webpack-dev-server 相关配置

    // devServer: {
        // //配置跨域
        // proxy: {
            // '/api': {
                // target: 'http://127.0.0.1:5000',
                // ws: true,
                // changeOrigin: true,
                // pathRewrite: {
                    // '^/api': ''  //通过pathRewrite重写地址，将前缀/api转为/
                // }
            // }
        // }
    // },
}