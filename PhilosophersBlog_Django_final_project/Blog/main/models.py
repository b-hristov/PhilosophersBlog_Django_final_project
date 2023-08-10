from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from tinymce import models as tinymce_models

UserModel = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(
        max_length=40,
        unique=True,
    )

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


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
        return f'{self.title}, {self.user}'


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
        return f'{self.content[:30]}, {self.user}'


class Like(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

