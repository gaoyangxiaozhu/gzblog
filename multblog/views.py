from django.shortcuts import get_object_or_404, render, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import UserAccount, Article, Categories


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()
class ArticleDetailsView(generic.DetailView):
    template_name = 'article_detail.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        try:
            context['article'] = Article.objects.get(pk=kwargs['pk'])
        except:
            raise Http404
        context['related_comments'] = Article.objects.get(pk=kwargs['pk']).comment_set.all()
        return self.render_to_response(context=context)

def showArticleByCategory(request, category):
    category = get_object_or_404(Categories, category=category)
    return render(request, 'article_list.html', {'category': category})




