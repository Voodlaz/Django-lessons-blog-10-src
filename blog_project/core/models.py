from django.db import models
from users.models import Account
from django.shortcuts import reverse

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=43)
    body = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id})
