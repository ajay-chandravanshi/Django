# Generated by Django 5.2 on 2025-06-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clt_username', models.CharField(max_length=50)),
                ('clt_email', models.EmailField(max_length=254, unique=True)),
                ('clt_phone', models.IntegerField()),
                ('clt_dob', models.DateField()),
                ('clt_gender', models.CharField(max_length=10)),
                ('clt_image', models.ImageField(upload_to='image/')),
                ('clt_detail', models.CharField(max_length=100)),
                ('clt_password', models.CharField(max_length=20)),
                ('clt_cpassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_query', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='image/')),
                ('room_name', models.CharField(max_length=30)),
                ('room_price', models.IntegerField()),
                ('room_size', models.IntegerField()),
                ('room_capacity', models.IntegerField()),
                ('room_bed', models.CharField(max_length=25)),
                ('room_services', models.CharField(max_length=30)),
            ],
        ),
    ]
