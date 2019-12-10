# Generated by Django 2.2 on 2019-12-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(max_length=200)),
                ('contract_email', models.CharField(max_length=200)),
                ('contract_subject', models.CharField(max_length=200)),
                ('contract_message', models.TextField(max_length=500)),
            ],
        ),
    ]
