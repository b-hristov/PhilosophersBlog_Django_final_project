from django.contrib import admin

from PhilosophersBlog_Django_final_project.Blog.main.models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_on', 'edited_on')
    search_fields = ('title', 'user__username',)
    list_filter = ('user__is_staff', 'created_on',)
    date_hierarchy = 'created_on'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post_title',)

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = 'Post Title'
