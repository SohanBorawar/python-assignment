from django.db import models

# Create your models here.
class Contact(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	remarks = models.TextField()

	def __str__(self):
		return self.name
	
class User(models.Model):
	
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.EmailField()
	mobile = models.PositiveIntegerField()
	gender = models.CharField(max_length=100)
	address = models.TextField()
	password = models.CharField(max_length=50)
	profile_pic = models.ImageField(upload_to='profile_pic/',default="")


	def __str__(self):
		return self.fname + " " + self.lname