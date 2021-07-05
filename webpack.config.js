const path = require('path');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');

module.exports = {
    entry: './src/app.js',
    output: {
        path: path.resolve(__dirname, 'dist/'),
        publicPath: '/static/',
        filename: 'bundle.js',
    },
    devServer: {
        writeToDisk: true,
    },
    module: {
        rules: [
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                loader: 'file-loader',
                options: {
                    name: '[path][name].[ext]?[hash]',
                    context: 'src'
                },
            },
            {
                test: /\.(scss)$/,
                use: [
                    'style-loader',
                    {
                        loader: 'css-loader',
                        options: {importLoaders: 1},
                    },
                    'postcss-loader',
                    'sass-loader'
                ]
            }
        ]
    }, plugins: [
        new CleanWebpackPlugin(),
    ],
};