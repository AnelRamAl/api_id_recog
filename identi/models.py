from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class identif(models.Model):
    appID = models.CharField(max_length=200) #        INPUT USER textshort field                            OK
    userID =  models.IntegerField()
    created = models.DateTimeField(auto_now_add=True) 
    toTestID = models.CharField(max_length=200) # Data created+calculation   
    tipoID = models.CharField(max_length=200)  # Data calculation to a standar status and Mony has its own status   manage
    #data = models.ImageField(upload_to='readData/', default=True)
    #data = models.FileField(upload_to='audio/', default=True)
    file = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'wav', 'mp3'])], default=True)
    result = models.TextField(null=True, blank=True)

