from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

from core.models import BaseModel
from users.models import User


class Post(BaseModel):
    title = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)

    @property
    def score(self):
        return Vote.objects.filter(post=self).aggregate(Avg('vote')).get('vote__avg')


class Vote(BaseModel):
    voter = models.ForeignKey(User, on_delete=models.PROTECT)
    vote = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='votes')

    class Meta:
        unique_together = ('voter', 'post')


