# tampilan awal
print("===== HOTEL MAKMUR JAYA =====")
user = input("Masukkan nama anda: ")

print("\nSelamat Datang,", user)
print("Silahkan lakukan pemesanan kamar anda")
while True :
    print ("===== Daftar Menu =====")
    print ("1. Pemesanan kamar")
    print ("2. Bukti pemesanan")
    print ("0. Exit")
    print ("=" * 24)
    menu = input("Pilih menu: ")

    if menu == "1":
        from datetime import datetime

        def biaya_hotel(kamar, durasi):
            if kamar == "standart":
                tarif = 200000
            else:
                tarif = 350000

            total = tarif * durasi
            return total

        kamar = input("\nJenis kamar (standart/deluxe): ")
        check_in = input("Tanggal check-in (DD-MM-YYYY): ")
        check_out = input("Tanggal check-out (DD-MM-YYYY): ")
        print()

    elif menu == "2":
        tanggal_masuk = datetime.strptime (check_in, "%d-%m-%Y")
        tanggal_keluar = datetime.strptime (check_out, "%d-%m-%Y")
        durasi = (tanggal_keluar - tanggal_masuk).days
        hasil = biaya_hotel(kamar, durasi)
        print("\n𓆝 𓆟 𓆞 𓆝 𓆟  BUKTI PEMESANAN  𓆝 𓆟 𓆞 𓆝 𓆟")
        print("Kamar atas nama: ", user)
        print("Jenis kamar:", kamar)
        print("Check-in: ", check_in)
        print("Check-out: ", check_out)
        print("Lama menginap: ",durasi, "malam")
        print("Total biaya kamar yang harus anda bayar: Rp", hasil)
        print("𓆝 𓆟 𓆞 𓆝 𓆟" * 5)
        break

    elif menu == "0":
        break
    else:
        print("Nomor tidak valid")
        continue