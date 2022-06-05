# Generated by Django 4.0.4 on 2022-06-05 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0016_alter_openuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openuser',
            name='name',
            field=models.CharField(help_text='The name of this Openuser profile. Spaces are replaces with underscores', max_length=20, validators=[django.core.validators.RegexValidator(message='Must begin with a letter and can only contain letters and numbers', regex='^[a-zA-Z]+[a-zA-Z0-9]*')], verbose_name='Name'),
        ),
    ]