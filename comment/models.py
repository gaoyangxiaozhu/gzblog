# -*- coding: utf-8 -*-
from django.db import models

from multblog.models import Article

def get_comment_author(people, re_people):
    div_author_html = \
    "<div class='comment-author'>"+\
        people+\
        "<div class='reply-author'>"+\
            "<span class='re-text'>"+\
            ' 回复 '+\
            "</span>"+\
            "<span class=name>"+\
                re_people+\
            "</span>"+\
        "</div>"+\
    "</div>"

    return div_author_html
def get_comment_time(time):
    div_time_html=\
        "<div class='comment-time'>"+\
            time+\
        "</div>"
    return div_time_html
def get_comment_text(text):
    div_text_html=\
        "<div class='comment-text'>"+\
            "<p>"+\
                text+\
            "</p>"+\
        "</div>"
    return div_text_html

def get_comment_content(comment, re_comment):
    div_content_html=\
    "<div class='comment-content'>"+\
        get_comment_author(comment.author.name.__str__(), re_comment.author.name.__str__())+\
        get_comment_time(comment.time.strftime('%Y-%m-%d %H:%M:%S'))+\
        get_comment_text(comment.content.__str__())+\
    "</div>"

    return div_content_html


def get_comment_avator():
    div_avator_html="<div class='comment-avatar'>"+\
        "<img src='../../static/imags/avatar.png' alt='img' class='img-avatar-small avatar'>"+\
        "<span class='comment-name'>"+\
        "</div>"
    return div_avator_html

def get_comment_body(comment):
    return "<div class='comment-children'>"+\
            comment+\
            "</div>"

class CommentPeople(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    webSite=models.CharField(max_length=100)

class Comment(models.Model):

    article = models.ForeignKey(Article, null=True, blank=True)
    author = models.ForeignKey(CommentPeople)
    relate_comment = models.ManyToManyField('self', symmetrical=False, blank=True)
    time = models.DateTimeField()
    content = models.TextField()


    def get_comment_html_tree(self):
        comment_html=''
        for comment in self.relate_comment.order_by('time'):
            comment_html+= get_comment_body(get_comment_avator()+get_comment_content(comment, self))
            if len(comment.relate_comment.all()):
                comment_html+=Comment.get_comment_html_tree(comment)

        return comment_html

    def __str__(self):
        return str(self.id)
    def get_related_comments(self):
        return self.get_comment_html_tree()