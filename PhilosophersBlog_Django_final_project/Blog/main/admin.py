from django.contrib import admin

from PhilosophersBlog_Django_final_project.Blog.main.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
