# Generated by Django 3.2.20 on 2023-09-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_line_of_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=15)),
                ('telephone', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
