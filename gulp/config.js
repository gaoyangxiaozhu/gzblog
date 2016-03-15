'use strict';

var gutil = require('gulp-util');

exports.paths = {
  src: 'src',
  dist: 'dist',
  tmp: '.tmp',
  e2e: 'test_e2e',
  mocha: 'test_mocha',
  istanbul: 'test_mocha_coverage',
  server:'server'
};

//用于wiredep获取bower依赖主要JS文件列表的options
exports.wiredep = {
  exclude: [/bootstrap.js$/, /bootstrap-sass-official\/.*\.js/, /bootstrap\.css/],
  directory: 'bower_components'
};

/**
 *  错误处理
 */
exports.errorHandler = function() {
  return function (err) {
    gutil.beep();
    gutil.log(err.toString());
  }
};