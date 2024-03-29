# Generated by Django 3.2.12 on 2022-05-15 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vac_drive', '0004_alter_studentvaccination_vaccinationdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=32)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=32)),
                ('aadharID', models.CharField(max_length=12)),
                ('existingComorbidites', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='studentvaccination',
            old_name='vaccineName',
            new_name='vaccineDr',
        ),
        migrations.RemoveField(
            model_name='studentvaccination',
            name='aadharID',
        ),
        migrations.RemoveField(
            model_name='studentvaccination',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='studentvaccination',
            name='existingComorbidites',
        ),
        migrations.RemoveField(
            model_name='studentvaccination',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='studentvaccination',
            name='studentName',
        ),
        migrations.AlterField(
            model_name='studentvaccination',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='studentvaccination',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Student', to='vac_drive.student'),
            preserve_default=False,
        ),
    ]
