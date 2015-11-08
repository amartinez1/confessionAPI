from django.db import models

from core.models import TimeStampedModel
from autoslug import AutoSlugField


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class User(TimeStampedModel):
    device_id = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.device_id


class Confession(TimeStampedModel):
    title = models.CharField(max_length=50, unique=False)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True, max_length=50)
    score = models.IntegerField(default=0)
    posted = models.DateTimeField(auto_now_add=True, editable=False)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_categories(self):
        return ', '.join([str(c) for c in self.categories.all()])


class Like(TimeStampedModel):
    user = models.ForeignKey(User)
    confession = models.ForeignKey(Confession)
