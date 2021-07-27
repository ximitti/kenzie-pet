from django.db import models

# --------------------------------------------


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    scientific_name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "groups"

    def __repr__(self):
        return self.name
