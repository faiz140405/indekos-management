# kost/views.py
from django.shortcuts import render
from django.db import models # <-- Pastikan baris ini ada
from django.db.models import Count
from .models import Kost, Kamar
import matplotlib.pyplot as plt
import io
import base64

def daftar_kost(request):
    daftar_kost_obj = Kost.objects.all()

    room_stats = Kamar.objects.aggregate(
        available_rooms=Count('id', filter=models.Q(is_tersedia=True)),
        occupied_rooms=Count('id', filter=models.Q(is_tersedia=False))
    )

    available = room_stats.get('available_rooms', 0)
    occupied = room_stats.get('occupied_rooms', 0)

    plot_base64 = None # Inisialisasi dengan None

    try:
        # Hanya buat plot jika ada data untuk ditampilkan (total kamar > 0)
        if (available + occupied) > 0:
            labels = ['Tersedia', 'Terisi']
            counts = [available, occupied]
            colors = ['#4CAF50', '#FF9800']

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(labels, counts, color=colors)
            ax.set_ylabel('Jumlah Kamar')
            ax.set_title('Statistik Ketersediaan Kamar')

            for i, count in enumerate(counts):
                ax.text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10)

            plt.tight_layout()

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', bbox_inches='tight')
            plt.close(fig)
            plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        else:
            print("DEBUG: Tidak ada kamar di database, grafik tidak dibuat.") # Pesan debug
    except Exception as e:
        print(f"ERROR: Gagal membuat grafik: {e}") # Cetak error ke konsol server
        plot_base64 = None # Pastikan plot_base64 tetap None jika ada error

    context = {
        'daftar_kost': daftar_kost_obj,
        'plot_base64': plot_base64,
        'total_available_rooms': available,
        'total_occupied_rooms': occupied,
        'total_rooms': available + occupied
    }
    return render(request, 'kost/daftar_kost.html', context)

def daftar_kost(request):
    daftar_kost_obj = Kost.objects.all()

    # Hitung statistik kamar yang tersedia vs terisi
    room_stats = Kamar.objects.aggregate(
        available_rooms=Count('id', filter=models.Q(is_tersedia=True)),
        occupied_rooms=Count('id', filter=models.Q(is_tersedia=False))
    )

    available = room_stats.get('available_rooms', 0)
    occupied = room_stats.get('occupied_rooms', 0)

    # Buat Bar Chart
    labels = ['Tersedia', 'Terisi']
    counts = [available, occupied]
    colors = ['#4CAF50', '#FF9800'] # Hijau untuk tersedia, Oranye untuk terisi

    fig, ax = plt.subplots(figsize=(6, 4)) # Ukuran grafik
    ax.bar(labels, counts, color=colors)
    ax.set_ylabel('Jumlah Kamar')
    ax.set_title('Statistik Ketersediaan Kamar')

    # Tambahkan label angka di atas setiap bar
    for i, count in enumerate(counts):
        ax.text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10)

    plt.tight_layout() # Sesuaikan layout agar tidak ada yang terpotong

    # Simpan grafik ke objek BytesIO dan encode ke base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight') # Simpan sebagai PNG
    plt.close(fig) # Penting: Tutup plot untuk menghemat memori
    plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {
        'daftar_kost': daftar_kost_obj,
        'plot_base64': plot_base64, # Kirim data grafik ke template
        'total_available_rooms': available,
        'total_occupied_rooms': occupied,
        'total_rooms': available + occupied
    }
    return render(request, 'kost/daftar_kost.html', context)

def daftar_kost(request):
    daftar_kost = Kost.objects.all()
    return render(request, 'kost/daftar_kost.html', {'daftar_kost': daftar_kost})

def detail_kost(request, kost_id):
    kost = Kost.objects.get(id=kost_id)
    kamar_list = kost.kamar_set.all()
    return render(request, 'kost/detail_kost.html', {'kost': kost, 'kamar_list': kamar_list})

def tentang_kami(request):
    return render(request, 'kost/tentang_kami.html')

def kontak(request):
    # Untuk halaman kontak, Anda bisa menambahkan form di sini nanti
    return render(request, 'kost/kontak.html')