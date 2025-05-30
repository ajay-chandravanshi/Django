# Generated by Django 5.2 on 2025-04-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_name_student_stu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, help_text='enter a username', max_length=30, null=True, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('bio', models.CharField(blank=True, db_index=True, help_text='write a short bio about your', max_length=50, null=True)),
                ('is_active', models.BooleanField(db_index=True, default=False)),
                ('Qualification', models.CharField(choices=[('1', 'bba'), ('2', 'mba')], db_index=True, max_length=100, null=True, verbose_name='Quali')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_name',
            field=models.CharField(max_length=50),
        ),
    ]
