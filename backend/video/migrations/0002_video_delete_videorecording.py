# Generated by Django 4.2.5 on 2023-10-01 02:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('status', models.CharField(default='recording', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='VideoRecording',
        ),
    ]