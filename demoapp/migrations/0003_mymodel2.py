# Generated by Django 4.0.6 on 2023-06-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_message_alter_todo1_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('mobile_number', models.IntegerField()),
            ],
        ),
    ]
