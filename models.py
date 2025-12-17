from django.db import models
from rest_framework import serializers
# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator,MinValueValidator

def check_company_name(value):
    if value=='' or len(value)<5:
        raise serializers.ValidationError('company name is Upto te Mark')

def check_strength(value):
    if value<0:
        raise serializers.ValidationError('strength is Upto te Mark')


class Company(models.Model):
    cid = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=255,validators=[check_company_name])
    email = models.EmailField(unique=False)
    company_code = models.CharField(max_length=5,blank=True,null=True,unique=True,validators=[RegexValidator(regex=r'^[A-Za-z]{2}[0-9]{2}[EN]$' )])
    strength = models.PositiveIntegerField(blank=True,null=True,validators=[check_strength])
    website = models.URLField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name





