'use strict';

var express = require('express');
var passport = require('passport');
var auth = require('../auth.service');
var router = express.Router();

// weibo ---------------------------------

router
  .get('/', auth.snsPassport(), passport.authenticate('weibo', {
    failureRedirect: '/',
    session: false
  }))
  .get('/callback',function (req,res,next) {
    passport.authenticate('weibo', {
      session: false
    },function (err, user, redirectURL){
      var redirectUrl = req.session.passport.redirectUrl || '/';
      var snsmsg = {};
      if (err) {
        snsmsg.msg = err.message;
        snsmsg.msgtype = 'error';
      }else if(!user){
        snsmsg.msg = '登录失败,请重试';
        snsmsg.msgtype = 'error';
      }else{
        snsmsg.msgtype = 'success';
        snsmsg.msg  = '登录成功,欢迎光临!';
        var token = auth.signToken(user._id);
        res.cookie('token', JSON.stringify(token));
      }
      res.cookie('snsmsg',JSON.stringify(snsmsg),{maxAge:30000});
      return res.redirect(redirectUrl);
    })(req, res, next);
  });
  
module.exports = router;
