from django.db import models
from group.models import Group

# -----------------------------


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=30)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="animals")

    class Meta:
        db_table = "animals"

    def __repr__(self):
        return self.name
