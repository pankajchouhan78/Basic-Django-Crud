# Generated by Django 3.2.16 on 2023-06-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='collage',
            field=models.CharField(default='mit', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
