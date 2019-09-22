from django.db import models
from datetime import date
#today = date.today()
#print("Today's date:", today)


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


class speech_to_symptoms(models.Model):
	eci_id = models.CharField(max_length = 10000)
	voice_to_text= models.CharField(max_length=1000)
	symptom1 = models.CharField(max_length=1000)
	symptom2 = models.CharField(max_length=1000)
	symptom3 = models.CharField(max_length=1000)
	symptom4 = models.CharField(max_length=1000)
	symptom5 = models.CharField(max_length=1000)
	ailment = models.CharField(max_length =1000)
	
	def __str__(self):
		return self.eci_id + "  " + self.ailment 



##### use this as final no matter what
class speech_symptoms(models.Model):
	severity = models.CharField(max_length = 1000)
	date_logged = models.DateField()
	eci_id = models.CharField(max_length = 10000)
	voice_to_text= models.CharField(max_length=1000)
	symptom1 = models.CharField(max_length=1000)
	symptom2 = models.CharField(max_length=1000)
	symptom3 = models.CharField(max_length=1000)
	symptom4 = models.CharField(max_length=1000)
	symptom5 = models.CharField(max_length=1000)
	ailment = models.CharField(max_length =1000)
	
	def __str__(self):
		return self.severity + "," + self.eci_id + "," + self.ailment + "," + self.symptom1 + ","  + self.symptom2 + "," + self.symptom3 + "," +  self.symptom4 + "," + self.symptom5 + "," + str(self.date_logged)



### to store syndromes
class store_syn(models.Model):
	syndrome_store = models.CharField(max_length=1000)

	def __str__(self):
		return self.syndrome_store