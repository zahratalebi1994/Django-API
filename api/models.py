from django.db import models


class Attacks (models.Model):
    source_name = models.CharField(max_length=250)
    destination_name = models.CharField(max_length=250)
    impact_type = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return str(self.id) + ' - ' + self.source_name + ' - ' + self.destination_name + ' - ' + self.impact_type
