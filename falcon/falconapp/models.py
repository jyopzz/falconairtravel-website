from django.db import models

# Create your models here.
class Addreview(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='images/',null=False,blank=False)
    designation=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):

        return self.name 