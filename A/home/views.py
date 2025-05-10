from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View

from accounts.models import User
from .forms import CommentForm
from .models import Post, Comment


class HomeView(View):
    def get(self, request):
        posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
        return render(request, 'home/landing.html', {'posts': posts})


class DetailView(View):

    def get(self, request, post_slug):
        form = CommentForm()
        post = get_object_or_404(Post, slug=post_slug)
        comments = Comment.objects.filter(post=post, is_reply=False).order_by('created_at')
        return render(request, 'home/detail.html', {'post': post, 'comments': comments, 'form': form})

    def post(self, request, post_slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=post, is_reply=False).order_by('created_at')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            # اگر فیلد مخفی reply_comment پر شده، این یک ریپلایه
            if comment.reply_comment:
                comment.is_reply = True
            else:
                comment.is_reply = False

            comment.save()
            messages.success(request, 'Your comment has been added.', 'success')
            return redirect('home:detail', post_slug=post.slug)

        return render(request, 'home/detail.html', {'post': post, 'comments': comments, 'form': form})


class AboutUsView(View):
    def get(self, request):
        users = User.objects.all()
        print(users, "======================")
        # for user in users:
        #     if user.posts.all().exists():
        #
        #         print(user)
        return render(request, 'home/about.html', {'users': users})
