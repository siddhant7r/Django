# Generated by Django 5.1.1 on 2024-10-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_query', models.TextField(max_length=50)),
            ],
        ),
    ]
