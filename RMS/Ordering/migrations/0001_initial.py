# Generated by Django 4.2.5 on 2023-09-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True)),
                ('table_status', models.CharField(choices=[('occupied', 'occupied'), ('booked', 'booked'), ('Vacant', 'vacant')], default='Vacant', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default='1')),
                ('customer_preferences', models.CharField(max_length=500)),
                ('customer_name', models.CharField(default='your name', max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ordering.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiter', models.CharField(max_length=100)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='Ordering.orders')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_history_id', to='Ordering.orders')),
                ('table_of_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ordering.tables')),
            ],
        ),
    ]
