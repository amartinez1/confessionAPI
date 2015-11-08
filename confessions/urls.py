from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/confessions/$', views.ConfessionList.as_view(),
        name='confessions-list'),
    url(r'^api/motels/filters/$', views.ConfessionListFilters.as_view(),
        name='confessions-filters'),
]
