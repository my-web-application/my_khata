# Generated by Django 3.0.3 on 2020-04-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_accountstatus_logindetail_shopkeeperaccount'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.ShopKeeperAccount'),
            preserve_default=False,
        ),
    ]
