# Generated by Django 4.1 on 2022-08-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_student_bitiruvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='olingan_sana',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='qaytarish_sana',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
