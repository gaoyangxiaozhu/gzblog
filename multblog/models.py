from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    intro = models.CharField(max_length=200)
    current_job = models.CharField(max_length=100)
    avatar = models.URLField(blank=True)
    def __str__(self):
        return self.username

class Categories(models.Model):
    category = models.CharField(max_length=60, default='live')
    def __str__(self):
        return self.category
    def related_article_list(self):
        return self.article_set.all()

class Article(models.Model):
    author = models.ForeignKey(UserAccount)
    title = models.CharField(max_length=100)
    post_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='write some content in here!')
    category=models.ManyToManyField(Categories)
    def __str__(self):
        return self.title
    def get_author(self):
        currentUser= UserAccount.objects.get(pk=self.author_id)
        return currentUser.username
    def get_content(self):
        return self.content


