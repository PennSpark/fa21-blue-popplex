# Generated by Django 2.2.24 on 2021-11-17 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_request', models.CharField(choices=[('GEN', 'General'), ('SLOW', 'Slow Down'), ('REP', 'Repeat That'), ('REPHR', 'Rephrase'), ('EX', 'Provide An Example'), ('OTHER', 'Other')], default='GEN', max_length=5)),
                ('created_at', models.DateTimeField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
