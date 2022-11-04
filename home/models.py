from django.db import models


# Create your models here.
class EgModel(models.Model):
    string_field = models.CharField(max_length=100)
    textarea = models.TextField()
    integer = models.IntegerField()
    floating_number = models.FloatField()
    date_filed = models.DateField()
    image_filed = models.ImageField(upload_to="images")
