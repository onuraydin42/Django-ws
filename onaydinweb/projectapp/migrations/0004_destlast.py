# Generated by Django 4.0 on 2023-01-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_professional_second_bilgi2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destlast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlel', models.CharField(max_length=50)),
                ('name_date', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='img')),
            ],
        ),
    ]
