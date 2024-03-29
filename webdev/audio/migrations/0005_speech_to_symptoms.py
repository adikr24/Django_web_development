# Generated by Django 2.2.1 on 2019-09-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_store_syn'),
    ]

    operations = [
        migrations.CreateModel(
            name='speech_to_symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eci_id', models.CharField(max_length=10000)),
                ('voice_to_text', models.CharField(max_length=1000)),
                ('symptom1', models.CharField(max_length=1000)),
                ('symptom2', models.CharField(max_length=1000)),
                ('symptom3', models.CharField(max_length=1000)),
                ('symptom4', models.CharField(max_length=1000)),
                ('symptom5', models.CharField(max_length=1000)),
                ('ailment', models.CharField(max_length=1000)),
            ],
        ),
    ]
