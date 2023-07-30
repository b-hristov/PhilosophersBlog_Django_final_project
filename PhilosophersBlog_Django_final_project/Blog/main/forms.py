from django import forms

from PhilosophersBlog_Django_final_project.Blog.main.models import Post, Category


class CreatePostForm(forms.ModelForm):
    PREDEFINED_CATEGORIES = [
        ('Ethics', 'Ethics'),
        ('Epistemology', 'Epistemology'),
        ('Metaphysics', 'Metaphysics'),
        ('Political Philosophy', 'Political Philosophy'),
        ('Aesthetics', 'Aesthetics'),
        ('Philosophy of Science', 'Philosophy of Science'),
        ('Philosophy of Religion', 'Philosophy of Religion'),
        ('Existentialism', 'Existentialism'),
        ('Eastern Philosophy', 'Eastern Philosophy'),
        ('Feminist Philosophy', 'Feminist Philosophy'),
        ('Memes', 'Memes'),
    ]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        # Categories from the database
        existing_categories = Category.objects.all()

        seen_categories = set()
        merged_choices = [('', 'Select a category')]

        # Add predefined categories to the merged choices if not already encountered
        for category_title, category_label in self.PREDEFINED_CATEGORIES:
            if category_title not in seen_categories:
                seen_categories.add(category_title)
                merged_choices.append((category_title, category_label))

        # Add existing categories to the merged choices if not already encountered
        for category in existing_categories:
            if category.title not in seen_categories:
                seen_categories.add(category.title)
                merged_choices.append((category.title, category.title))

        # Update the 'category' field in the form with the merged choices
        self.fields['category'] = forms.ChoiceField(choices=merged_choices)

    class Meta:
        model = Post
        fields = ['title', 'content']

    def save(self, commit=True):
        post = super().save(commit=False)
        category_name = self.cleaned_data.get('category')

        if category_name:
            category, _ = Category.objects.get_or_create(title=category_name)
            post.category = category

        post.user = self.user

        if commit:
            post.save()
            self._save_m2m()

        return post
