# Generated by Django 3.2.3 on 2024-04-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_comments_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('PO', 'ProductOffers'), ('RP ,Regularproduct', 'Regularproduct')], default='RP ,Regularproduct', max_length=20),
        ),
    ]
