# Generated by Django 4.2.5 on 2023-10-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormRequest', '0003_bookrequest_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BookRequest',
        ),
    ]
