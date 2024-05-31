from django.db import models

# Create your models here.


class Statstics(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True) 
    source = models.CharField(max_length=100, blank=True, null=True)
    pestle = models.CharField(max_length=100 ,blank=True, null=True)
    region = models.CharField(max_length=200 ,blank=True, null=True)
    topic = models.CharField(max_length=500 ,blank=True, null=True) 
    sector = models.CharField(max_length=300 ,blank=True, null=True)
    insight = models.CharField(max_length=500 ,blank=True, null=True)
    impact = models.CharField(max_length=200 ,blank=True, null=True)
    start_year = models.CharField( blank=True, null=True, default="", max_length=50) 
    end_year = models.CharField ( blank=True, null=True, default="", max_length=50) 
    published = models.CharField( max_length=100, blank=True, null=True) 
    added = models.CharField(max_length=100, blank=True, null=True) 
    relevance = models.IntegerField(blank=True, null=True) 
    intensity = models.IntegerField(blank=True, null=True)
    likelihood = models.IntegerField(blank=True, null=True) 
    url = models.CharField(blank=True, null=True, max_length=500) 


    @property
    def data(self):
        return Statstics.objects.all()
    
    def __str__(self):
        return self.title
    

