# Generated by Django 3.0.2 on 2020-01-27 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_base_choice_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='base.Post'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Post'),
        ),
        migrations.DeleteModel(
            name='Base',
        ),
    ]
