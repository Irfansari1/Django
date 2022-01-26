# Generated by Django 4.0.1 on 2022-01-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_student_last_updated_date_student_register_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
