from django.shortcuts import get_object_or_404, render
#from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import CommentForm, ImageForm
from .models import Post


def post_list(request):
    object_list = Post.objects.filter(status=1).order_by("-created_on")
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        #if page is out of range delive last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {"post": post,
                                        "comments": comments,
                                        "new_comment": new_comment,
                                        "comment_form": comment_form})


def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, "index.html", {"form": form, "img_obj": img_obj})
    else:
        form = ImageForm()
    return render(request, "index.html", {"form": form})