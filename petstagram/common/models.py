from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )

    text = models.TextField(max_length=300)

    datetime = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )