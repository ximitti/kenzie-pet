from django.db import models

# -----------------------------


class Characteristic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "characteristics"

    def __repr__(self):
        return self.name
