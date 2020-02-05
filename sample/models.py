from django.db import models

# Create your models here.

class Model1(models.Model):
	name=models.CharField(max_length=20)
	marks=models.IntegerField()
	experience=models.CharField(max_length=30)
	qualification=models.CharField(max_length=20)
	designation=models.CharField(max_length=20)
	
	def __str__(self):
		return self.name


class Model2(models.Model):
	name=models.CharField(max_length=20)
	phone_number=models.IntegerField()
	email=models.EmailField(max_length=40)
	location=models.CharField(max_length=20)
	
	def __str__(self):
		return self.email


class Model3(models.Model):
	name=models.CharField(max_length=30)
	address=models.TextField(max_length=100)
	about=models.TextField(max_length=200, blank=True,null=True)
	date_of_birth=models.DateField()

	def __str__(self):
		return self.name
	
