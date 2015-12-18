from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    category = models.ForeignKey('blog.Category', related_name='posts', default=None)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def posts_liked(self):
        return self.liked.filter(is_liked=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey('blog.Post', related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def comments_liked(self):
        return self.liked.filter(is_liked=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    is_liked = models.BooleanField(default=False)


    def like(self):
        self.is_liked = not self.is_liked
        self.save()


class PostLike(Like):
    author = models.ForeignKey('auth.User', related_name='postlikes', default=None)
    post = models.ForeignKey('blog.Post', related_name='liked', default=None)


class CommentLike(Like):
    author = models.ForeignKey('auth.User', related_name='commentlikes', default=None)
    comment = models.ForeignKey('blog.Comment', related_name='liked', default=None)
