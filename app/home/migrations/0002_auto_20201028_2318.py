# Generated by Django 3.1.2 on 2020-10-28 22:18

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.today()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
