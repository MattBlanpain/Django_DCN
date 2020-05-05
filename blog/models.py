from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

PRIORITY_CHOICES = (
    ('1_day', '1 Day'),
    ('2_day', '2 Days'),
    ('1_week', '1 week'),
    ('2_week', '2 weeks'),
)


class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # -------------------    DCN  --------------------------

    dcn_number = models.CharField(max_length=100, verbose_name='DCN number')
    state = models.CharField(max_length=100, default="")
    category_of_change = models.CharField(max_length=100, default="")

    description_of_change = models.TextField(default="enter description of change")

    reason_of_change = models.TextField(default="enter reason of change")

    closes_dcr = models.BooleanField(default=False)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default='1_week')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
