from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    model =Comment
    filter_horizontal = ('relate_comment',)

admin.site.register(Comment,CommentAdmin)
