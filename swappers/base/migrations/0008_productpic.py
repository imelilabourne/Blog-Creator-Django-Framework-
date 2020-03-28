# Generated by Django 3.0.2 on 2020-02-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200203_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('location', models.TextField()),
                ('title', models.TextField()),
                ('story', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
