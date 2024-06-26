# Generated by Django 4.2 on 2024-05-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_code_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_after_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='00G3H846', max_length=8),
        ),
    ]
