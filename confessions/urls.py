from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/confessions/$', views.ConfessionListFilters.as_view(),
        name='confessions-list'),
    url(r'^api/confessions/(?P<pk>[0-9]+)/$', views.ConfessionDetail.as_view(),
        name='confessions-filters'),
]
