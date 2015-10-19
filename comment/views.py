from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from datetime import datetime

from .models import Comment

def getComment(request):
    commentList = Comment.objects.all().order_by('time')
    htmlContent=''
    for comment in commentList:
        htmlContent += '<div>'+comment.content+' time'+ comment.time+comment.get_comment_tree()+'</div>'

    return render(request, 'comment.html', {'htmlContent': htmlContent})






