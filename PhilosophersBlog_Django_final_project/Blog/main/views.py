from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from PhilosophersBlog_Django_final_project.Blog.main.forms import CreatePostForm
from PhilosophersBlog_Django_final_project.Blog.main.models import Post, Category


class IndexView(ListView):
    template_name = 'main/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-created_on']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['categories'] = Category.objects.all()
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post/create-post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('index')  # to be changed later to reverse_lazy('my_posts')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PostDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'post/post-details.html'
    model = Post
    context_object_name = 'post'


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/edit-post.html'
    fields = ['title', 'content', 'category']

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs={'pk': self.object.pk})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('index')
