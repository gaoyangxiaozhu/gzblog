from django.db import models

from multblog.models import Article

class Comment(models.Model):

    article = models.ForeignKey(Article)
    reComment = models.ManyToManyField('self', symmetrical=False)
    time= models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    email = models.CharField(max_length=100)
    webSite = models.CharField(max_length=100)

    def __str__(self):
        re_count = len(self.reComment.all())
        return 'relate author count:'+str(re_count)
    @staticmethod
    def get_li(comment_name, comment_content, child_html=''):
        return '<li><strong>name: '+comment_name+'</strong>content: '+comment_content+child_html+'</li>'
    @staticmethod
    def get_ul(str):
        return '<ul>'+str+'</ul>'
    @staticmethod
    def get_comment_html_tree(currentComment):
        str = ''
        if len(currentComment.reComment.all()) ==0:
            return Comment.get_li(currentComment.name, currentComment.content)
        else:
            for comment in currentComment.reComment.all():
                str+=Comment.get_comment_html_tree(comment)

            return Comment.get_li(currentComment.name, currentComment.content, child_html=Comment.get_ul(str))

    def getCommentTree(self):
        return Comment.get_ul(Comment.get_comment_html_tree(self))



