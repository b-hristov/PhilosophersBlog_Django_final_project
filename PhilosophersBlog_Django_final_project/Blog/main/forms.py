from django import forms

from PhilosophersBlog_Django_final_project.Blog.main.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']

        category = forms.Select(
            
        )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.user
        if commit:
            post.save()
            self._save_m2m()
        return post
