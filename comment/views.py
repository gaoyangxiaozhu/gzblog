from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Comment

def getComment(request):
    commentList = Comment.objects.all()
    htmlContent=''
    for comment in commentList:
        htmlContent += comment.getCommentTree()

    return render(request, 'comment.html', {'htmlContent': htmlContent})






