# Generated by Django 4.2.2 on 2024-08-16 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0010_alter_kurs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название курса'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]