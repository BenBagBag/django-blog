from django.conf.urls import url
from blog.views import list_view, stub_view

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
    stub_view,
    name="blog_detail"),
]
