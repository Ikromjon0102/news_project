from django.urls import reverse
from django.utils import timezone
from django.db import models




# class PublishedManager(models.Model):
#     def get_queryset(self):
#         return super().get_queryset().filter(status=News.Status.Published)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class News(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True)
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Publish'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email