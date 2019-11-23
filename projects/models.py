from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    url = models.URLField()

    def __str__(self):
        return self.title
