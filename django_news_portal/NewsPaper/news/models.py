from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    full_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, blank=True)
    author_raiting = models.IntegerField(default=0)
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        post_raiting = self.post_set.aggregate(PostRaiting=Sum("raiting"))
        pRait = 0
        pRait += post_raiting.get("PostRaiting")

        com_raiting = self.author_user.comment_set.aggregate(CommentRaiting=Sum("raiting"))
        cRait = 0
        cRait += com_raiting.get('CommentRaiting')

        self.author_raiting = pRait * 3 + cRait
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = [
        (NEWS, "Новость"),
        (ARTICLE, "Статья"),
    ]
    post_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_header = models.CharField(max_length=64)
    post_text = models.TextField()
    raiting = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def post_like(self):
        self.raiting += 1
        self.save()

    def post_dislike(self):
        self.raiting -= 1
        self.save()

    @property
    def post_preview(self):
        return self.post_text[0:123] + "..."


class PostCategory(models.Model):
    postTo = models.ForeignKey(Post, on_delete=models.CASCADE)
    catTo = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    com_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com_author = models.ForeignKey(User, on_delete=models.CASCADE)
    com_text = models.TextField()
    raiting = models.IntegerField(default=0)
    com_time = models.DateTimeField(auto_now_add=True)

    def com_like(self):
        self.raiting += 1
        self.save()

    def com_dislike(self):
        self.raiting -= 1
        self.save()
