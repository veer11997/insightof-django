from django.db import models
class Contest(models.Model):
	conest_name=models.TextField()
	contest_type=models.TextField()
	contest_site=models.TextField()
	starting=models.DateField()
	ending=models.DateField()

    


# Create your models here.
