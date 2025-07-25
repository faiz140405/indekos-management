# Generated by Django 5.2.3 on 2025-06-17 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('jumlah_kamar', models.IntegerField(default=0)),
                ('deskripsi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_kamar', models.CharField(max_length=10)),
                ('tipe_kamar', models.CharField(max_length=50)),
                ('harga_sewa', models.DecimalField(decimal_places=0, max_digits=10)),
                ('is_tersedia', models.BooleanField(default=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('kost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kamar_set', to='kost.kost')),
            ],
        ),
    ]
