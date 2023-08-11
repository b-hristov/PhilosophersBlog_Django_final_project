from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from PhilosophersBlog_Django_final_project.Blog.accounts.managers import BlogUserManager
from PhilosophersBlog_Django_final_project.Blog.common.validators import validate_names, clean_avatar


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
        validators=(validate_names,)
    )

    last_name = models.CharField(
        max_length=25,
        validators=(
            validate_names,
        )
    )

    image = models.ImageField(
        upload_to='profile_avatars',
        default='default_avatar/sample-avatar.png',
        null=True,
        blank=True,
        validators=(
            clean_avatar,
        )
    )

    date_of_birth = models.DateField(
        null=False,
        blank=False,
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
