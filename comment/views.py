from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.views.generic import View
from datetime import datetime
from .comment_form import CommonForms
from .utils import check_article_comment, Article, Comment

class CommonNewView(View):

    @staticmethod
    def insert_new_comment(data):

        article = Article.objects.get(pk=data['article_id'])

        comment_new = Comment(comment_people=data['author'],
                              email=data['email'],
                              webSite=data['url'],
                              content=data['comment'],
                              time=datetime.now()
                              )
        comment_new.save()
        if data['comment_id']:
            comment = Comment.objects.get(pk=data['comment_id'])
            comment_new.relate_comment.add(comment)
        else:
            comment_new.article=article
        comment_new.save()

        return {'status': 'ok'}

    def post(self, request):
        form = CommonForms(request.POST)
        if not form.is_valid():
            return JsonResponse({
                'status': 'error',
                'msg': str(form.errors)
            })
        data = form.cleaned_data
        (article_id, comment_id)= (data['article_id'], data['comment_id'])

        (status, msg)=check_article_comment(article_id, comment_id)

        if not status:
            return JsonResponse({
                'status': 'error',
                'msg':msg
            })

        CommonNewView.insert_new_comment(data)

        return JsonResponse({
            'status': 'ok',
            'msg': ''
        })







