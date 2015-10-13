from django.contrib import admin

from .models import UserAccount, Article, Categories


class ArticleInline(admin.TabularInline):
    model = Article
    extra = 2

class UserAccountAdmin(admin.ModelAdmin):

    list_display = ('username', 'intro', 'current_job')
    inlines = [ArticleInline]
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Categories)

