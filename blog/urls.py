from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.post_list, name="home"),
    path("upload/", views.image_upload_view),
    path("<slug:slug>/", views.post_detail, name="post_detail"),   
]
