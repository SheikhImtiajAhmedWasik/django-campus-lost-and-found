from django.db import models


class Report(models.Model):
    CHOOSE_TYPE = (
        ('Lost', 'L'),
        ('Found', 'F'),
    )
    item_name = models.CharField(max_length=100)
    type = models.CharField(max_length=5, choices=CHOOSE_TYPE)
    category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lost_found/image')