class Hotel:
    def __init__(self):
        self.ketersediaan_kamar = {
            "Standard": 5,
            "Deluxe": 2,
            "Suite": 1
        }
        self.data_reservasi = []

    def reservasi_kamar(self, nama_pengunjung, nomor_identitas, tipe_kamar, tanggal_check_in, durasi_menginap):
        if self.ketersediaan_kamar.get(tipe_kamar, 0) > 0:
            self.ketersediaan_kamar[tipe_kamar] -= 1
            reservasi = {
                "nama": nama_pengunjung,
                "nomor_identitas": nomor_identitas,
                "tipe_kamar": tipe_kamar,
                "tanggal_check_in": tanggal_check_in,
                "durasi": durasi_menginap
            }
            self.data_reservasi.append(reservasi)
            print("Reservasi berhasil disimpan.")
        else:
            print("Kamar tidak tersedia.")

# Contoh penggunaan
hotel = Hotel()
hotel.reservasi_kamar("Cici", "987654321", "Deluxe", "2024-10-20", 3)
hotel.reservasi_kamar("Coco", "123456789", "Suite", "2024-10-21", 2)
hotel.reservasi_kamar("Coco", "123456789", "Suite", "2024-10-21", 2)