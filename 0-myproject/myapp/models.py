from django.db import models

class main_table(models.Model):
    brand = models.TextField(max_length=100, blank=True, null=True)
    part_no = models.TextField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    cross_part = models.TextField(max_length=100, blank=True, null=True)
    price = models.TextField(max_length=100, blank=True, null=True)
    url = models.TextField(max_length=500, blank=True, null=True)
    part_no_form = models.TextField(max_length=100, blank=True, null=True)
    supplier = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.part_no

