from django.contrib import admin
from PhilosophersBlog_Django_final_project.Blog.accounts.models import Profile


@admin.register(Profile)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user',)
