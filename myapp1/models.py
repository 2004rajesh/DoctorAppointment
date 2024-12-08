from django.db import models

# Create your models here.

class Userdata(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self) :
        return self.email
    
class Doctor(models.Model):
    
    doctor_name=models.CharField(max_length=100)
    doctor_image=models.ImageField(upload_to="doctor/")
    Department=models.CharField(max_length=100)
    
    def __str__(self):
        return self.doctor_name
    
class Patient(models.Model):
    user = models.ForeignKey(Userdata,on_delete=models.CASCADE)
    doctorinfo = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    phoneno=models.BigIntegerField()
    date=models.DateField()
    description =models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.name
    
