# Generated by Django 3.2.3 on 2024-04-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('R', 'REJECTION'), ('P', 'PENDING'), ('S', 'SHIPPING')], default='P', max_length=1),
        ),
    ]
