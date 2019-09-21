from django.db import models

# Create your models here.

class db_design(models.Model):
	first_name = models.CharField(max_length =100)
	last_name = models.CharField(max_length =100)

	def __str__(self):
		return self.last_name + ' ' + self.first_name


### to store speeches
class speech(models.Model):
	voice_to_text= models.CharField(max_length=1000)
	
	
	def __str__(self):
		return self.voice_to_text



### to store syndromes
class store_syn(models.Model):
	syndrome_store = models.CharField(max_length=1000)

	def __str__(self):
		return self.syndrome_store