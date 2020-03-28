# Generated by Django 2.2.4 on 2020-02-06 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_auto_20200206_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='food_pics', verbose_name='Image')),
                ('location', models.TextField()),
                ('title', models.TextField()),
                ('story', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
