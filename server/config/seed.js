/**
 * 初始化数据
 */

'use strict';

var mongoose = require('mongoose'),
	User = mongoose.model('User'),
	Article = mongoose.model('Article'),
	TagCategory = mongoose.model('TagCategory'),
	Tag = mongoose.model('Tag');
var Promise = require('bluebird');
	//初始化标签,文章,用户
	if(process.env.NODE_ENV === 'development' || process.env.NODE_ENV === 'test'){
		User.countAsync().then(function (count) {
			 if(count === 0){
			 	User.removeAsync().then(function () {
			 		User.createAsync({
			 			nickname:'gyy',
			 			email:'admin@admin.com',
			 			role:'admin',
			 			password:'admin',
						desc: '我是高阳阳，一个喜欢乱捣鼓的人，喜欢电影，音乐，喜欢python,nodeJs,以及前端相关的内容',
						blog: 'http://gyyzyp.com',
			 			status:1
			 		},{
			 			nickname:'zyp',
			 			email:'gyyzyp@163.com',
			 			role:'admin',
			 			password:'admin',
						desc: '我是小朱，博主的女友，哈哈哈',
						blog: 'http://gyyzyp.com',
			 			status:1
			 		},{
			 			nickname:'test001',
			 			email:'test001@test.com',
			 			role:'user',
			 			password:'test',
			 			status:1
			 		},{
			 			nickname:'test002',
			 			email:'test002@test.com',
			 			role:'user',
			 			password:'test',
			 			status:2
			 		},{
			 			nickname:'test003',
			 			email:'test003@test.com',
			 			role:'user',
			 			password:'test',
			 			status:0
			 		});
			 	});
			}
		});

		TagCategory.countAsync().then(function (count) {
			if(count === 0){
				TagCategory.removeAsync().then(function () {
					return Tag.removeAsync();
				}).then(function () {
					return TagCategory.createAsync({
						name:'language',
						desc:'按编程语言分类'
					}).then(function (cat) {
						return Tag.createAsync({
							name:'nodejs',
							cid:cat._id,
							is_show:true
						},{
							name:'angular',
							cid:cat._id,
							is_show:true
						},{
							name:'react',
							cid:cat._id,
							is_show:true
						})
					}).then(function () {
						return TagCategory.createAsync({
							name:'system',
							desc:'按操作系统分类'
						}).then(function (cat) {
							return Tag.createAsync({
								name:'linux',
								cid:cat._id,
								is_show:true
							},{
								name:'ios',
								cid:cat._id,
								is_show:true
							},{
								name:'android',
								cid:cat._id,
								is_show:true
							})
						});
					}).then(function () {
						return TagCategory.createAsync({
							name:'other',
							desc:'其它分类'
						}).then(function (cat) {
							return Tag.createAsync({
								name:'git',
								cid:cat._id,
								is_show:true
							});
						});
					}).then(function () {
						return Tag.findAsync().then(function (tags) {
							return tags;
						})
					});

				}).then(function (tags) {
					return Article.removeAsync().then(function () {
						return tags;
					});
				}).map(function (tag,index) {
					var indexOne = parseInt(index) +1;
					var indexTwo = parseInt(index) +2;
					Article.createAsync({
						title:'第' + (index + indexOne) + '篇文章',
						content:'<p>我第' + (index + indexOne) + '次爱你.</p>',
						tags:[tag._id],
						status:1
					},{
						title:'第' + (index + indexTwo) + '篇文章',
						content:'<p>我第' + (index + indexTwo) + '次爱你.</p>',
						tags:[tag._id],
						status:1
					})
				}).then(function(){
					//增加author_id
					User.findAsync({'role':'admin'}).then(function(users){

						return Article.findAsync().then(function(articles){
							articles.forEach(function(article, index){
								article.author_id= users[parseInt(Math.random()*users.length)]._id;
								article.save();
							})
						});
					});
				});

			}
		});
	}
