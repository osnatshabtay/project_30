# Generated by Django 4.1.3 on 2022-11-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('descprition', models.CharField(max_length=200)),
            ],
        ),
    ]