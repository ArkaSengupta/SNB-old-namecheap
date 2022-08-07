# Generated by Django 3.0.8 on 2020-08-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0009_career_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='Subject_of_Query',
            field=models.CharField(blank=True, choices=[('Income_Tax', 'Income Tax'), ('Audit', 'Audit'), ('Service_Tax', 'Service Tax'), ('Company_Law', 'Company Law'), ('Excise_Duty', 'Excise Duty'), ('Customs', 'Customs'), ('Wealth_Tax', 'Wealth Tax'), ('ST/VAT', 'Sales Tax / Value Added Tax'), ('FEMA', 'FEMA'), ('RBI', 'RBI'), ('GST', 'GST'), ('Labour_Law', 'Labour_Law'), ('Others', 'Others')], max_length=200, null=True),
        ),
    ]
