# Generated by Django 3.2.12 on 2022-05-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac_drive', '0012_rename_studentdtls_studentvaccination_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='studentvaccination',
            name='vaccinationDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='vaccinedrive',
            name='vacdriveDate',
            field=models.DateTimeField(),
        ),
    ]
