from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from PhilosophersBlog_Django_final_project.Blog.accounts.managers import BlogUserManager
from PhilosophersBlog_Django_final_project.Blog.main.validators import validate_letters, clean_avatar


class BlogUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = BlogUserManager()


class Profile(models.Model):

    first_name = models.CharField(
        max_length=25,
        validators=(validate_letters,)
    )

    last_name = models.CharField(
        max_length=25,
        validators=(validate_letters,)
    )

    image = models.ImageField(
        upload_to='media',
        default='static/images/avatar.png',
        null=True,
        blank=True,
        validators=(
            clean_avatar,
        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.user}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
