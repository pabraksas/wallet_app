# Generated by Django 3.0.5 on 2020-04-15 21:08

from django.db import migrations, models
import wallet_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0009_auto_20200414_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.CharField(default=wallet_app.models.generate_id, editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
