# Generated by Django 3.0.5 on 2020-04-14 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0008_auto_20200414_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.CharField(default='536696f831ee4d0a8d430e332639e54c', editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(default='', editable=False, max_length=3, verbose_name='тип транзакции'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='wallet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='wallet_app.Wallet', verbose_name='кошелек'),
        ),
    ]