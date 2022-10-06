from django.db import models


# Create your models here.
class Advocates(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='advocates/')
    short_bio = models.TextField(max_length=500)
    long_bio = models.TextField(max_length=1000)
    advocate_years_exp = models.IntegerField()
    youtube = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    github = models.URLField(max_length=200)


class Companies(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='companies/')
    summary = models.TextField(max_length=500)
    advocates = models.ForeignKey('Advocates', on_delete=models.CASCADE, related_name='companies')
