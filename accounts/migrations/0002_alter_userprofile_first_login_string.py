# Generated by Django 3.2.5 on 2021-08-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_login_string',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]