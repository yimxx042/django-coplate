# Generated by Django 2.2 on 2021-08-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0003_auto_20210811_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image1',
            field=models.ImageField(upload_to='review_pics'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image2',
            field=models.ImageField(blank=True, upload_to='review_pics'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image3',
            field=models.ImageField(blank=True, upload_to='review_pics'),
        ),
    ]
