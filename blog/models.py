from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def save(self):
        super(Post, self).save()
        self.slug = slugify(self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
