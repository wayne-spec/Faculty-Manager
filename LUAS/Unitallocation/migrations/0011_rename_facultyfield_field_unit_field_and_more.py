# Generated by Django 5.1.4 on 2025-01-14 20:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unitallocation', '0010_rename_school_facultyfield_school_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacultyField',
            new_name='Field',
        ),
        migrations.AddField(
            model_name='unit',
            name='field',
            field=models.ManyToManyField(blank=True, to='Unitallocation.field'),
        ),
        migrations.AddField(
            model_name='unit',
            name='is_on_offer',
            field=models.BooleanField(default=False, help_text='Is the unit on offer?'),
        ),
    ]
