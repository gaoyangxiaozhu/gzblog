from django.contrib import admin

from .models import UserAccount, Article, Categories
from comment.models import  Comment



class ArticleInline(admin.TabularInline):

    model = Article
    extra = 2

class CommentInline(admin.TabularInline):

    model = Comment
    extra = 3
    exclude = ('relate_comment',)


class UserAccountAdmin(admin.ModelAdmin):

    list_display = ('username', 'intro', 'current_job')
    inlines = [ArticleInline]
class ArticleAdmin(admin.ModelAdmin):

    filter_horizontal = ('category',)
    list_display = ('id', 'title')
    inlines = [CommentInline]

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categories)

