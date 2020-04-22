from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    dcn_number = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="")
    category_of_change = models.CharField(max_length=100, default="")

    description_of_change = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
