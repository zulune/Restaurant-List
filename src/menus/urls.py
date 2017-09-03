from django.conf.urls import url

from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView
)

urlpatterns = [

    url(r'^create$', ItemCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name="detail"),
    # url(r'^(?P<pk>\d+)/update$', ItemUpdateView.as_view(), name="update"),
    url(r'$', ItemListView.as_view(), name="list"),
]
