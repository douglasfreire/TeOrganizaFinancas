# Generated by Django 3.2.1 on 2021-06-20 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banco', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Histories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('due_date', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('value', models.BigIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('fees', models.IntegerField()),
                ('total_bank_balance', models.BigIntegerField()),
                ('balance_available', models.BigIntegerField()),
                ('id_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.banksusers')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
