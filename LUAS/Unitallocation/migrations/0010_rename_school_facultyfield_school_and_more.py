# Generated by Django 5.1.4 on 2024-12-20 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Unitallocation', '0009_rename_school_unit_school'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='facultyfield',
            old_name='School',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='Director',
            new_name='director',
        ),
        migrations.RemoveField(
            model_name='facultyfield',
            name='FieldDescription',
        ),
        migrations.AddField(
            model_name='academicyear',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faculty',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faculty',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facultyfield',
            name='field_description',
            field=models.CharField(default='Researcher in Machine Learning/Machine Learning Engineer', max_length=255),
        ),
        migrations.AddField(
            model_name='facultyfield',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='facultyfield',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maxallocations',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='maxallocations',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maxallocations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='maxallocations',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='school',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='semester',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='semester',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='semester',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unit',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='unitallocation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='unitallocation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='unitallocation',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='facultyfield',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='facultyfield',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unitallocation',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
