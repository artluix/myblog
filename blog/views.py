from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Category, Comment, PostLike, CommentLike
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = None
    if request.user.is_authenticated():
            user_posts_pk_liked = request.user.postlikes.filter(is_liked=True).values_list('post', flat=True)
            context = {'posts': posts, 'user_posts_pk_liked': user_posts_pk_liked}

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_comments_pk_liked = request.user.commentlikes.filter(is_liked=True).values_list('comment', flat=True)
    context = {'post': post, 'user_comments_pk_liked': user_comments_pk_liked}
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(request.user)
            post.save()

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    postlike, created = PostLike.objects.get_or_create(post=post, author=request.user)
    postlike.like()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=post.pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


@login_required
def category_post_list(request, pk):
    category = Category.objects.get(pk=pk)
    context = {'category': category, 'posts': category.posts.all()}
    return render(request, 'blog/category_post_list.html', context)


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(post, request.user)
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)

    else:
        form = CommentForm(initial={'author': request.user})
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

@login_required
def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    commentlike, created = CommentLike.objects.get_or_create(comment=comment, author=request.user)
    commentlike.like()
    return redirect(request.META.get('HTTP_REFERER'), pk=comment.post.pk)
