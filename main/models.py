from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phno=models.BigIntegerField()
    email=models.CharField(max_length=50)
    address=models.TextField()
    def __str__(self):
        return self.full_name
