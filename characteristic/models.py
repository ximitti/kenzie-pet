from django.db import models

from animal.models import Animal

# -----------------------------


class Characteristic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    animals = models.ManyToManyField(Animal, related_name="characteristics")

    class Meta:
        db_table = "characteristics"

    def __repr__(self):
        return self.name
