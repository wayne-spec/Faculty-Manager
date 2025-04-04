# Generated by Django 5.1.4 on 2024-12-05 17:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_unit', models.BooleanField(default=False)),
                ('offered_unit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MaxAllocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_allocations', models.PositiveIntegerField()),
                ('dead_end_allocations', models.PositiveIntegerField()),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.academicyear')),
                ('faculty_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.facultytype')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(default='0712345678', max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10)),
                ('address', models.TextField(default='Default Address')),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('profile_link', models.URLField(blank=True, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('joining_date', models.DateField()),
                ('field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.facultyfield')),
                ('school', models.ForeignKey(default='Gender', on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.school')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.school')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.academicyear')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=255)),
                ('unit_short_name', models.CharField(default='Math', max_length=50)),
                ('unit_code', models.CharField(default='1101', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(default='Computer Science', on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.course')),
                ('unit_type', models.ForeignKey(default='Service Unit', on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.unittype')),
            ],
        ),
        migrations.CreateModel(
            name='UnitAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocation_date', models.DateField()),
                ('group_name', models.CharField(default='Group A', max_length=255)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.academicyear')),
                ('course', models.ForeignKey(default='Computer Science', on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.faculty')),
                ('semester', models.ForeignKey(default='November- March', on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.semester')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Workrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workrate', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unitallocation.faculty')),
            ],
        ),
    ]
