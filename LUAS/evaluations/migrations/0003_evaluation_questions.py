# Generated by Django 5.1.4 on 2025-01-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0002_alter_evaluationresponse_evaluation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='questions',
            field=models.ManyToManyField(related_name='evaluations', to='evaluations.evaluationquestion'),
        ),
    ]
