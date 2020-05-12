from django.db import models

# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16,unique=True)
    p_age = models.IntegerField(default=18,db_column="age")
    p_sex =models.BooleanField(default=True,db_column="sex")

    @classmethod
    def create(cls,p_name,p_age=100,p_sex=True):
        return cls(p_name,p_age=p_age,p_sex=p_sex)
    class Meta:
        db_table = 'People'