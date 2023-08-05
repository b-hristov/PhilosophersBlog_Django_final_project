from django.contrib.auth import get_user_model
from django.db import models
from tinymce import models as tinymce_models

UserModel = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(
        max_length=40,
        unique=True,
    )

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    title = models.CharField(
        max_length=200,
    )

    content = tinymce_models.HTMLField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    edited_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    class Meta:
        ordering = ['created_on']

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.content[:30]}'


class Like(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

