from django.db import models
class Contest(models.Model):
	contest_name=models.TextField()
	book_name=models.TextField()
	starting=models.DateField()
	ending=models.DateField()
    

	
    
   



# Create your models here.
