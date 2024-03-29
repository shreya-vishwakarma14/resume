# Generated by Django 4.2.7 on 2024-02-09 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gst_no', models.CharField(max_length=15)),
                ('state_code', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Consigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gst_no', models.CharField(max_length=15)),
                ('state_code', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_no', models.CharField(max_length=15)),
                ('driver_name', models.CharField(max_length=255)),
                ('driver_address', models.CharField(max_length=512)),
                ('contact_no', models.IntegerField()),
                ('engine_no', models.CharField(max_length=30)),
                ('chasis_no', models.CharField(max_length=30)),
                ('dl_no', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=255)),
                ('owner_address', models.CharField(max_length=512)),
                ('owner_contact', models.CharField(max_length=15)),
                ('owner_pan', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True)),
                ('from_field', models.CharField(max_length=255)),
                ('to_field', models.CharField(max_length=255)),
                ('nature_of_goods', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('freight_rate', models.FloatField()),
                ('freight_total', models.FloatField()),
                ('toll_tax', models.FloatField()),
                ('gr_sr_charges', models.FloatField()),
                ('fooding', models.IntegerField()),
                ('kata', models.CharField(max_length=30)),
                ('gst', models.FloatField()),
                ('advance', models.IntegerField()),
                ('payable_amt', models.FloatField()),
                ('e_way_bill_no', models.CharField(max_length=30)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('consignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.consignee')),
                ('consigner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.consigner')),
            ],
        ),
    ]
