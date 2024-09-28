from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=30)

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True
    )


# class PetsPhoto(models.Model):
#     photo = models.ImageField()

