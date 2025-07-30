from django.db import models

# Create your models here.
class Toy(models.Model):
   
    name = models.CharField(max_length=100,blank=False,default="")
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    was_included_in_home = models.BooleanField(default=False)
    toy_category = models.CharField(max_length=200,blank=False,default="")
    class Meta:
        ordering =['-name']
