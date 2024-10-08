# Generated by Django 4.2.2 on 2024-08-16 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0011_alter_kurs_description_alter_kurs_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='kurs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kurs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='urok',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите картинку', null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='urok',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uroki', to=settings.AUTH_USER_MODEL),
        ),
    ]
