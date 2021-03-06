# Generated by Django 3.0.3 on 2020-03-10 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_logindetail_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('status_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'account_status',
            },
        ),
        migrations.AddField(
            model_name='shopkeeperaccount',
            name='status_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.AccountStatus'),
            preserve_default=False,
        ),
    ]
