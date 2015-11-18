import django_filters
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework import filters
from rest_framework import generics

from rest_framework.views import APIView

from .models import Category, Confession, User, Like

from .serializers import ConfessionListSerializer, LikeSerializer


class ConfessionFilter(django_filters.FilterSet):

    """
    Filter model by category or user
    """
    user = django_filters.CharFilter(name='user__device_id')
    categories = django_filters.CharFilter(name='categories__name')

    class Meta:
        model = Confession
        fields = ['categories', 'user']


class ConfessionList(generics.ListCreateAPIView):

    """
    #Retrieves, creates a list of confessions
    ---
    ### 1.Filters Values Documentation
    > Filters by categories, users

    - ####Examples:
        *  #####Filter by cateogries: [?categories=all](?categories=popular)
        *  #####Filter by users: [?user=device_id](?user=cfhdjsks123kdj)
    """
    queryset = Confession.objects.all()
    serializer_class = ConfessionListSerializer
    filter_class = ConfessionFilter


class ConfessionDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    #Retrieve, update or delete a confession
    ---
    """
    queryset = Confession.objects.all()
    serializer_class = ConfessionListSerializer


class LikeList(generics.ListCreateAPIView):

    """
    #Retrieve, creates a like association to a confession
    ---
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    #Retrieve, update, or delete like association
    ---
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
