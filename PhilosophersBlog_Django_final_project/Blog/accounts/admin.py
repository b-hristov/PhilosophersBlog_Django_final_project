from django.contrib import admin
from PhilosophersBlog_Django_final_project.Blog.accounts.models import Profile, BlogUser


@admin.register(Profile)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')


@admin.register(BlogUser)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'is_staff')
