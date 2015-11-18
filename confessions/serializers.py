from django.core.paginator import Paginator

from .models import Category, Confession, User, Like
from rest_framework import pagination
from rest_framework import serializers

from rest_framework.renderers import JSONRenderer


class CategorySerielizer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'device_id')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like


class ConfessionListSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    categories = CategorySerielizer(many=True)

    class Meta:
        model = Confession
        fields = ('id', 'title', 'content', 'score', 'categories', 'user')
        depth = 1
