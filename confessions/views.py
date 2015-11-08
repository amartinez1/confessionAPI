import django_filters
from django.shortcuts import render, get_object_or_404

from rest_framework import filters
from rest_framework import generics

from .models import Category, Confession, User, Like

from .serializers import ConfessionListSerializer


class ConfessionFilter(django_filters.FilterSet):

    """
    Filter model by category or user
    """
    class Meta:
        model = Confession
        fields = ['categories', 'user']


class ConfessionList(generics.ListAPIView):

    """
    #Retrieves a list of all confessions
    """
    queryset = Confession.objects.all()
    serializer_class = ConfessionListSerializer

class ConfessionListFilters(generics.ListAPIView):
	"""
	#Retrieves a list of all confessions
	---
	###Filters Values Documentation
	> Filters by categories, users

	- ####Examples:
	    *  #####Filter by cateogries: [?categories=all](?categories=popular)
	    *  #####Filter by users: [?user=device_id](?user=cfhdjsks123kdj)
	"""
	queryset = Confession.objects.all()
	serializer_class = ConfessionListSerializer
	filter_class = ConfessionFilter