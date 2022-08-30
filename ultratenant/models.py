from django.db import models


class DefaultTenant(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
