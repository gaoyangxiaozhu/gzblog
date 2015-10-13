from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import UserAccount, Article, Categories


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()
class ArticleContentView(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'
def showArticleByCategory(request, category):
    category = get_object_or_404(Categories, category=category)
    return render(request, 'article_list.html', {'category': category})




