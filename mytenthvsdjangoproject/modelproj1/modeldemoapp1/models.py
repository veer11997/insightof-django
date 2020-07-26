from django.db import models


class Book(models.Model):
    book_Id=models.IntegerField()
    book_name=models.TextField()
    bookprice=models.FloatField()
    subject=models.CharField(max_length=30)
    pub_date=models.DateField()


    def __str__(self):
        return self.book_name
# Create your models here.
