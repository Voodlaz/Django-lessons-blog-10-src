from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post
from core.forms import NewPostForm


def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "homepage.html", context)

def post_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    return render(request, "post_view.html", context)

def new_post_form(request):
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('login')

    form = NewPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = NewPostForm()
        return redirect(obj)

    context["new_post_form"] = form
    return render(request, "new_post_form.html", context)
