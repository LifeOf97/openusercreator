# Generated by Django 4.0.4 on 2022-06-04 14:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Openuser',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this Openuser profile', max_length=10, verbose_name='Name')),
                ('profiles', models.IntegerField(default=5, help_text='Number of openuser profiles to create, defaul is 10', validators=[django.core.validators.MaxValueValidator(limit_value=50)], verbose_name='Profiles')),
                ('profile_password', models.CharField(default='p@ssw0rd', help_text='The password to use for all profiles', max_length=20, verbose_name='Profile password')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The date and time this Openuser profile was created', verbose_name='Date Created')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, help_text='The last time this Openuser profile was updated', verbose_name='Last Updated')),
                ('creator', models.ForeignKey(help_text='The Appuser who owns this Openuser profiles', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'ordering': ['-last_updated'],
            },
        ),
        migrations.AddConstraint(
            model_name='openuser',
            constraint=models.UniqueConstraint(fields=('creator', 'name'), name='unique_openuser'),
        ),
    ]