# Generated by Django 3.1.3 on 2020-12-09 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appraisalapp', '0005_auto_20201209_0634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='cop_dev',
            new_name='corporate_development',
        ),
    ]
