from django.db import models

# Create your models here.
class empregmodel(models.Model):
    emp_name=models.CharField(max_length = 10)
    emp_address=models.CharField(max_length = 10)
    emp_gender=models.CharField(max_length = 10)
    emp_number=models.CharField(max_length = 10)
    emp_salary=models.CharField(max_length = 30)
    empemail=models.CharField(max_length = 20)
    emp_photo=models.CharField(max_length = 100)
    emp_joindate=models.CharField(max_length = 20)
    class Meta:
        db_table='empreg'



class empanotherdatamodel (models.Model) :
    emp_name = models.CharField (max_length = 10)
    emp_color = models.CharField (max_length = 10)
    emp_height = models.IntegerField (max_length = 5)
    emp_ofc = models.CharField (max_length = 20)
    class Meta :
        db_table = 'empanotherdata'