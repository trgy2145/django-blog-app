#from msilib.schema import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from hitcount.views import HitCountDetailView
from main.settings import LOGIN_REDIRECT_URL
# Create your views here.


@login_required()
def PostCreateView(request):
    model = BlogPost
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('list')
            messages.success(request, 'Blog added successfully')
            # success_message =('Blog added successfully.')
    context = {"form": form}
    return render(request, "blog/post_create.html", context)


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = BlogPost
    context_object_name = 'blogs'


class PostDetailView(HitCountDetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
    count_hit = True


class PostUpdateView(UpdateView):
    model = BlogPost
    #form_class = BlogPostForm
    template_name = 'blog/post_update.html'
    fields = ['title', 'slug', 'content', 'image']
    success_url = reverse_lazy('list')


class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('list')


@login_required()
def LikeView(request, pk):
    user = request.user
    post = get_object_or_404(BlogPost, id=request.POST.get('blog_id'))

    if user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('list')


# def search(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         blogs = BlogPost.objects.filter(title__contains=searched)
#         return render(request, "search.html", {'searched':searched, 'blogs':blogs})
#     else:
#         return render(request, "search.html", {})
