# Generated by Django 4.1.2 on 2022-10-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_care', '0002_patient_role_staff_healthhistory_vitalsigns_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]
