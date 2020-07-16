# Generated by Django 3.0.7 on 2020-07-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='published_date',
            new_name='Published_date',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='SubCategory',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
