# -*- coding: utf-8 -*-
from django.db import models

from multblog.models import Article


def get_comment_header(people, re_people):
    div_header_html="<div class='comment-header'>"+\
        "<span class='comment-avator'>"+\
        "<img src='#' alt='img'>"+\
        "</span>"+\
        "<span class='comment-name'>"+\
        people+\
        "</span>"+\
        "<span class='re-text'>"+\
        ' 回复 '+\
        "</span>"+\
        "<span class=name>"+\
        re_people+\
        "</span>"+\
        "</div>"
    return div_header_html
def get_comment_content(content):
    div_content_html="<p class='comment-content'>"+content+"</p>"
    return div_content_html
def get_comment_footer(time):
    div_comment_footer_html="<div class='comment-footer'>"+\
        "<span class='comment-time'>"+\
        str(time)+\
        "</span>"+\
        "</div>"
    return div_comment_footer_html

def get_comment_body(comment):
    return "<div class='comment-children'>"+\
            comment+\
            "</div>"


class Comment(models.Model):

    article = models.ForeignKey(Article, null=True, blank=True)
    relate_comment = models.ManyToManyField('self', symmetrical=False, blank=True)
    time = models.DateTimeField()
    comment_people = models.CharField(max_length=100)
    content = models.TextField()
    email = models.CharField(max_length=100)
    webSite = models.CharField(max_length=100)

    def get_comment_html_tree(self):
        comment_html=''
        for comment in self.relate_comment.order_by('time'):
            comment_html+= get_comment_body(get_comment_header(comment.comment_people.__str__(), self.comment_people.__str__())+get_comment_content(comment.content.__str__())+get_comment_footer(comment.time.strftime('%Y-%m-%d %H:%M:%S')))
            if len(comment.relate_comment.all()):
                comment_html+=Comment.get_comment_html_tree(comment)

        return comment_html

    def __str__(self):
        return str(self.id)
    def get_related_comments(self):
        return self.get_comment_html_tree()
