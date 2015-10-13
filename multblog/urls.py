from django.conf.urls import  url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.ArticleContentView.as_view(), name='content'),
    url(r'^post/category/(?P<category>[a-zA-Z]+)/$', views.showArticleByCategory, name='category'),

]