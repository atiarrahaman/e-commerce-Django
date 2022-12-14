# Generated by Django 3.2.8 on 2021-10-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('des', models.TextField()),
                ('discount_price', models.FloatField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(choices=[('tw', 'topWear'), ('bw', 'bottomWear'), ('tw', 'topWear'), ('l', 'laptop')], max_length=2)),
            ],
        ),
    ]
