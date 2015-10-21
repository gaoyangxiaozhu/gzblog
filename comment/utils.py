
from .models import Comment, Article
def check_article_comment(article_id, comment_id):
    article_query_set = Article.objects.filter(id=article_id)
    comment_query_set = Comment.objects.filter(id=comment_id)
    if not (article_query_set.exists() and comment_query_set.exists()):
        return False, 'article id  or comment id not exist'

    return True, ''
