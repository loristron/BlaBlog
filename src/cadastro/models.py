from django.db import models

# Create your models here
class UserProfile(models.Model):
	nome		= models.CharField(max_length=120)
	sobrenome	= models.CharField(max_length=120)
	#username	= models.OneToOneField(User)
	email		= models.EmailField()
	user_bio	= models.CharField(max_length=240)
