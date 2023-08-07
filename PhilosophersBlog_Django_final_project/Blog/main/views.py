from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView

from PhilosophersBlog_Django_final_project.Blog.main.forms import CreatePostForm, CommentForm
from PhilosophersBlog_Django_final_project.Blog.main.models import Post, Category, Comment, Like


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['user_liked'] = self.object.like_set.filter(user=self.request.user)
        return context


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/edit-post.html'
    fields = ['title', 'content', 'category']

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('index')


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/post-details.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.post = post
        comment.user = self.request.user
        comment.save()
        return redirect('post_details', pk=post.pk)

    def get_success_url(self):
        return reverse('post_details', kwargs={'pk': self.kwargs['pk']})


class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/edit-comment.html'

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comment, id=self.kwargs['pk'])
        return comment

    def get_success_url(self):
        return reverse('post_details', kwargs={'pk': self.object.post.pk})


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'comment/delete-comment.html'

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comment, id=self.kwargs['pk'])
        return comment

    def get_success_url(self):
        return reverse('post_details', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context


class LikeView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])

        kwargs = {
            'post': post,
            'user': self.request.user
        }

        like_object = Like.objects.filter(**kwargs).first()

        if like_object:
            like_object.delete()
        else:
            new_like_object = Like(**kwargs)
            new_like_object.save()

        return reverse_lazy('post_details', kwargs={'pk': post.pk})
