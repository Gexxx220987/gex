# Generated by Django 4.1.5 on 2023-02-03 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_category_subcribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subcribers',
            new_name='subscribers',
        ),
    ]
