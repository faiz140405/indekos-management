# kost/models.py
from django.db import models

class Kost(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    jumlah_kamar = models.IntegerField(default=0)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

class Kamar(models.Model):
    kost = models.ForeignKey(Kost, on_delete=models.CASCADE, related_name='kamar_set')
    nomor_kamar = models.CharField(max_length=10)
    tipe_kamar = models.CharField(max_length=50) # Contoh: 'AC', 'Non-AC', 'Kamar Mandi Dalam'
    harga_sewa = models.DecimalField(max_digits=10, decimal_places=0)
    is_tersedia = models.BooleanField(default=True)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nomor_kamar} - {self.kost.nama}"