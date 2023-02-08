# Generated by Django 4.1.5 on 2023-02-03 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_rename_categorykol_postcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]