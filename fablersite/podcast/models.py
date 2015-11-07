from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from durationfield.db.models.fields.duration import DurationField
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from threaded_comments.models import Comment

class Publisher(models.Model):
    """
    Model for each Publisher of Podcasts
    """
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=255, blank=True, unique=True)
    users = models.ManyToManyField(User, blank=True)
    comments = GenericRelation(Comment)
    #slug = models.SlugField(unique=True)
    #@models.permalink
    #def get_absolute_url(self):
    #    return 'podcast:publisher', (self.slug,)
    def __str__(self):
        return self.name


class Podcast(models.Model):
    """
    Model for each podcast
    """
    publisher = models.ForeignKey(Publisher, related_name='podcast')
    title = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    summary = models.TextField(max_length=4000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    explicit = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    copyright = models.CharField(max_length=255, blank=True)
    blocked = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    keywords = models.CharField(max_length=100, blank=True)
    comments = GenericRelation(Comment)
    #slug = models.SlugField(unique=True)
    #@models.permalink
    #def get_absolute_url(self):
    #    return 'podcast:podcast', (self.slug,)
    def __str__(self):
        return self.title
    # image = FieleField(max_length=255)


class Episode(models.Model):
    """
    Model for episodes of Podcasts
    """
    podcast = models.ForeignKey(Podcast, related_name='episode')
    title = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=4000, blank=True)
    blocked = models.BooleanField(default=False)
    pubdate = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)
    keywords = models.CharField(max_length=100, blank=True)
    explicit = models.CharField(max_length=255, blank=True)
    comments = GenericRelation(Comment)
    #slug = models.SlugField(unique=True)
    #@models.permalink
    #def get_absolute_url(self):
    #    return 'podcast:episode', (self.slug,)
    def __str__(self):
        return self.title


class Subscription(models.Model):
    """
    Model for Subscription of Podcasts
    """
    podcast = models.ForeignKey(Podcast, related_name='subscription')
    user = models.ForeignKey(User, related_name='subscription')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('podcast', 'user',)


# class EpisodeTimeline(models.Model)


# class EpisodeDiscussion(models.Model)
