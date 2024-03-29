# Generated by Django 3.2.12 on 2022-05-15 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vac_drive', '0009_studentvaccination_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvaccination',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vac_drive.student'),
        ),
        migrations.AlterField(
            model_name='studentvaccination',
            name='vaccineDr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vac_drive.vaccinedrive'),
        ),
    ]
