from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    # context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name="published")
        context["post_list"] = (
            Post.objects.filter(status=published_status)
            .order_by("created_on")
            .reverse()
        )
        return context


class DraftListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = (
            Post.objects.filter(status=draft_status)
            .filter(author=self.request.user)
            .order_by("created_on")
            .reverse()
        )
        return context

class ArchiveListView(LoginRequiredMixin,ListView):
    template_name = "posts/list.html"
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name="archived")
        context["post_list"] = (
            Post.objects.filter(status=published_status)
            .order_by("created_on")
            .reverse()
        )
        return context


class PostDetailView(DetailView,UserPassesTestMixin):
    template_name = "posts/detail.html"
    model = Post
    # context_object_name = 'post'
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if str(post.status) == 'archived' and (not request.user.is_authenticated) or str(post.status) == 'draft' and (not request.user.is_authenticated):
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    # def test_func(self):
    #     post = self.get_object()
    #     if post.status.name == 'published':
    #         return True
    #     else:
    #         if post.status.name == 'draft':
    #             return self.request.user == post.author
    #         elif post.status.name == 'archived':
    #             return True
    #     return False

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
