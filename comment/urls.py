from django.conf.urls import  url
from . import views
urlpatterns = [
    url(r'^comment/new/$', views.CommonNewView.as_view()),

]
