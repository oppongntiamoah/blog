from django.db import models
from user.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICE = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]

    CATEGORY = [
        ('python', 'Python'),
        ('php', 'PHP'),
        ('js', 'Javascript'),
        ('blog', 'Blog'),
    ]

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    body = models.TextField()
    publish = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICE, default='draft' ,max_length=9)
    category = models.CharField(choices=CATEGORY,
                              default='blog', max_length=9)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": self.slug})
    
