from django.db import models
from group.models import Group
from characteristic.models import Characteristic

# -----------------------------


class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=30)

    characteristics = models.ManyToManyField(Characteristic)

    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = "animals"

    def __repr__(self):
        return self.name
