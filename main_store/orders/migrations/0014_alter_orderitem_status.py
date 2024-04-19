# Generated by Django 3.2.3 on 2024-04-13 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Rejection', 'Rejection'), ('Pending', 'Pending'), ('Shipping', 'Shipping')], default=('Pending', 'Pending'), max_length=50),
        ),
    ]