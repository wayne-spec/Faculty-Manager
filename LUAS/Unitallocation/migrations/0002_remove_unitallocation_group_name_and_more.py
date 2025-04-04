# Generated by Django 5.1.4 on 2024-12-12 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unitallocation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitallocation',
            name='group_name',
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.facultytype'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='staff_number',
            field=models.IntegerField(default=166937, unique=True),
        ),
        migrations.AddField(
            model_name='facultyfield',
            name='FieldDescription',
            field=models.CharField(default='Researcher in Machine Learning/Machhine Learning Engineer '),
        ),
        migrations.AddField(
            model_name='facultyfield',
            name='School',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.school'),
        ),
        migrations.AddField(
            model_name='school',
            name='Director',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unitallocation',
            name='group',
            field=models.CharField(default='Group A', max_length=20),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='academic_year_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='mobile_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.school'),
        ),
        migrations.AlterField(
            model_name='facultytype',
            name='faculty_type_name',
            field=models.CharField(default='Full-Time', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(default='School of Computing and Engineering Sciences', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.course'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_short_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.unittype'),
        ),
        migrations.AlterField(
            model_name='unitallocation',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.course'),
        ),
        migrations.AlterField(
            model_name='unitallocation',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.semester'),
        ),
        migrations.DeleteModel(
            name='Workrate',
        ),
    ]
