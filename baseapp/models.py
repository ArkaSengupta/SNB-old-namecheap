from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_file_extension
# Create your models here.

class Query(models.Model):
    Sub = (('Income_Tax', 'Income Tax'),
			('Audit', 'Audit'),
            ('Service_Tax', 'Service Tax'),
            ('Company_Law', 'Company Law'),
            ('Excise_Duty', 'Excise Duty'),
            ('Customs', 'Customs'),
            ('Wealth_Tax', 'Wealth Tax'),
            ('ST/VAT', 'Sales Tax / Value Added Tax'),
            ('FEMA', 'FEMA'),
            ('RBI', 'RBI'),
            ('GST', 'GST'),
            ('Labour_Law', 'Labour_Law'),
            ('Others', 'Others'),
			)

    Name = models.CharField(max_length=200, null=True)
    Designation = models.CharField(max_length=50,blank=True, null=True)
    Organization = models.CharField(max_length=100,blank=True, null=True)
    Office_Address = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=50,blank=True, null=True)
    Email = models.EmailField(max_length=254, null=True)
    Telephone_Office = models.TextField(blank=True, null=True)
    Mobile = models.CharField(max_length=50,blank=True, null=True)
    Subject_of_Query = models.CharField(max_length=200,blank=True, null=True, choices=Sub)
    Query_Content = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['id']


class Career(models.Model):
    Gen = (('Male', 'Male'),
			('Female', 'Female'),)

    First_Name = models.CharField(max_length=100, null=True)
    Last_Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=254, null=True)
    Mobile = models.CharField(max_length=50, blank=True, null=True)
    Gender = models.CharField(max_length=200, blank=True, null=True, choices=Gen)
    Postion = models.CharField(max_length=50, blank=True, null=True)
    DOB = models.DateField()
    Qualification = models.CharField(max_length=200,blank=True, null=True)
    Portfolio_Website = models.CharField(max_length=50,blank=True, null=True)
    Resume = models.FileField(upload_to='documents/', validators=[validate_file_extension], blank=True, null=True)
    Experience = models.CharField(max_length=50,blank=True, null=True)
    RCQ = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.First_Name + ' ' + self.Last_Name)

    def validate_resume(Resume):
        file_size = Resume.file.size
        limit_kb = 1500
        if file_size > limit_kb * 1024:
            raise ValidationError("Max size of file is %s KB" % limit)

        #limit_mb = 8
        #if file_size > limit_mb * 1024 * 1024:
