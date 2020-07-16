# Generated by Django 3.0.7 on 2020-07-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=700)),
                ('head0', models.CharField(default='', max_length=6000)),
                ('head1', models.CharField(default='', max_length=6000)),
                ('head2', models.CharField(default='', max_length=6000)),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
                ('Published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
