from django.db import models


class Gallery(models.Model):
    """Stores campus photos uploaded by admin."""

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.title
