# Generated by Django 4.1.3 on 2023-01-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default=' ', max_length=150, null=True),
        ),
    ]
