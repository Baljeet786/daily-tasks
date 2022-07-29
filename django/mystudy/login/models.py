from django.db import models



class Customer(models.Model):
	username=models.CharField(max_length=20,null=False,blank=False)
	email=models.CharField(max_length=20,null=False,blank=False)
	password=models.CharField(max_length=10,null=False,blank=False)
	subject=models.CharField(max_length=20,null=False,blank=False)
	message=models.TextField(max_length=100,null=True,blank=True)
	image=models.ImageField(null=True,upload_to='images/')

	def __str__(self):
		return self.username