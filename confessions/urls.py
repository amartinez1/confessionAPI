from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/confessions/$', views.ConfessionList.as_view(),
        name='confessions-list'),
    url(r'^api/confessions/(?P<pk>[0-9]+)/$', views.ConfessionDetail.as_view(),
        name='confession-detail'),
    url(r'^api/users/(?P<pk>[0-9]+)/likes/$', views.LikeList.as_view(), name='user-likes'),
    url(r'^api/users/(?P<pk>[0-9]+)/likes/(?P<pk>[0-9]+)$', views.LikeDetail.as_view(),
    	name='user-like-detail'),
]
