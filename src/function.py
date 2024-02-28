from tabulate import tabulate
import datetime

HEADERS = ('ID', 'Title', 'Author', 'Publisher', 'Genre', 'Stock')

databaseBuku = [
                [101, 'Merasa Pintar, Bodoh Saja Tak Punya', 'Rusdi Mathari', 'Buku Mojok', 'Fiction', 3],
                [201,'1Q84','Haruki Murakami','GPU','Novel',10],
                [301, 'Tidak Ada New York Hari Ini', 'Aan Mansyur', 'GPU', 'Poetry', 4],
                [401, 'Tidak Ada Pelangi Di Nusantara', 'Ama Achmad', 'Malatax', 'Poetry', 8]
                ]

# Tampilan Tabel Database Buku Utama
def tampilanDaftarBuku(databaseBuku, headers = HEADERS, title='\nTabel Inventory Buku\n'):
    """Fungsi untuk menampilkan database buku dalam format tabulasi

    Args:
        databaseBuku (List): Database
        headers (tuple, optional): Nama Kolom.
        title (str, optional): Judul Tabel'.
    """
    print(title)
    print (tabulate (databaseBuku, headers, tablefmt = 'grid'))

# Tampilan Tabel Buku Yang Dipinjam
database_buku_dipinjam = []
HEADERS_B = ('ID', 'Title', 'Author', 'Publisher', 'Genre', 'Stock', 'ID Peminjam', 'Tanggal Dipinjam')
def tabelPinjaman(database_buku_dipinjam, headers = HEADERS_B, title = '\nDaftar Pinjaman Buku\n'):
    """Fungsi Menampilkan Daftar Buku Yang Sedang Dipinjam Dalam Format Tabulasi

    Args:
        database_buku_dipinjam (list): Berisi daftar buku yang sedang dipinjam
        headers (tuple, optional): Nama kolom
        title (str, optional): Judul tabel
    """
    print(title)
    print (tabulate (database_buku_dipinjam, headers, tablefmt = 'grid'))


# Fungsi Menampilkan Database Buku
main_read = f"""
Pilih menu di bawah:
1. Daftar Semua Buku
2. Cari Buku
3. Kembali ke Menu Utama
"""
def read(databaseBuku):
    """Fungsi untuk menampilkan daftar buku secara keseluruhan

    Args:
        databaseBuku (list): Database Buku
    """
    while True:
        inputRead = input(main_read)

        if inputRead == '1':
            if len(databaseBuku) == 0:
                print('\nDaftar Buku Kosong!')
                continue
            else:
                tampilanDaftarBuku(databaseBuku)
        elif inputRead == '2':
            if len(databaseBuku) == 0:
                print('\nDaftar Buku Kosong!')
                continue
            else:
                valFilter(databaseBuku)
        elif inputRead == '3':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print('\nMasukkan angka sesuai pilihan!')
            continue

#Fungsi Pilihan Filter

main_valFilter = f"""
Cari Buku Berdasarkan:
1. ID Buku
2. Judul Buku
3. Kembali ke Menu Sebelumnya
"""
def valFilter(databaseBuku):
    while True:
        input_val_filter = input(main_valFilter)

        if input_val_filter == '1':
            cariID(databaseBuku)
        elif input_val_filter == '2':
            searchBook(databaseBuku)
        elif input_val_filter == '3':
            read(databaseBuku)
        else:
            print('Masukkan Angka Sesuai Pilihan!')
        continue

# Fungsi Filter Based ID

def cariID(databaseBuku):
    query_cari_id=[]
    for angka_id, valueID in enumerate (databaseBuku):
        query_cari_id.append(valueID[0])
            
    while True:
        input_cari_id = int_validation('\nMasukkan ID Buku: ')
        if input_cari_id not in query_cari_id:
            print('\nMaaf, ID Tidak Terdaftar!')
            continue
        else:
            data_filter = []  
            for idx, item in enumerate(databaseBuku):
                if input_cari_id == item[0]:
                    data_filter.append(databaseBuku[idx])
            tampilanDaftarBuku(data_filter)
            read(databaseBuku)
            break

# Fungsi Filter Buku Based On Judul Buku

def searchBook(databaseBuku):
    while True:
        buku_judul = input('\nMasukkan Judul Buku: ')
        buku_judul = buku_judul.title()
        kata_kata = buku_judul.split()

        def cari_buku(databaseBuku, kata_kata):
            buku_dengan_kata = []

            for buku in databaseBuku:
                judul = buku[1]
                for kata in kata_kata:
                    if kata in judul:
                        buku_dengan_kata.append(buku)
                        break
            return buku_dengan_kata

        hasil_cari = cari_buku(databaseBuku, kata_kata)
        buku_baru = []
        for buku in hasil_cari:
            buku_baru.append(buku)
        
        if len(buku_baru) > 0:
            tampilanDaftarBuku(buku_baru, headers=HEADERS, title='\nTabel Filter Buku\n')
        else:
            print('\nMaaf, Buku yang Anda Cari Tidak Tersedia.')
            read(databaseBuku)
        break

# Fungsi Menambah Daftar Buku
main_add = f"""
Apa yang Ingin Anda Lakukan?
1. Menambah Daftar Buku
2. Kembali ke Menu Utama
"""

def tambahBuku(databaseBuku):
    while True:
        input_tambah_buku = input(main_add)
        if input_tambah_buku == '1':
            add(databaseBuku)
        elif input_tambah_buku == '2':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print ('\nMasukkan Angka Sesuai Pilihan!')
            continue

def add(databaseBuku):
    while True:
        idBuku = int_validation('\nMasukkan ID Buku: ')
        id_query=[]
        for angka, valId in enumerate (databaseBuku):
            id_query.append(valId[0])

        if idBuku in id_query:
            print('\nID sudah terdaftar, masukkan ID lain!')
            continue
        else:
            break       

    namaBuku = strnum_validation('\nMasukkan Judul Buku: ')
    penulis = str_validation('\nMasukkan Nama Penulis: ')
    penerbit = str_validation('\nMasukkan Nama Penerbit: ')
    genreType = str_validation('\nMasukkan Genre Buku: ')
    stock = int_validation('\nMasukkan Jumlah Buku yang Ingin Ditambahkan: ')

    while True:
        saveValid = input('\nApakah data ingin disimpan? (Yes/No) :')
        if saveValid.lower() in ('no', 'n'):
            print('\nPERINGATAN! Data Tidak Disimpan!')
            read(databaseBuku)
        elif saveValid.lower() in ('yes', 'y'):
            print('\nSelamat ya, Data Berhasil Disimpan :)')
            databaseBuku.append([
                int(idBuku),
                namaBuku.title(),
                penulis.title(),
                penerbit.title(),
                genreType.title(),
                int(stock)])
            tampilanDaftarBuku(databaseBuku)
            tambahBuku(databaseBuku)
            break
        else:
            print('\nMasukkan pilihan Yes/No saja dong ah!')
            continue

# Fungsi Mengupdate Daftar Buku

main_change_data = f"""
Apa yang ingin Anda lakukan?
1. Mengubah Daftar Buku
2. Kembali ke Menu Utama
"""

def changeData(databaseBuku):
    while True:
        input_change_data = input(main_change_data)
        if input_change_data == '1':
            valid_changeData(databaseBuku) #setelahnya masukkan ID dulu + tampilin semua datanya
        elif input_change_data == '2':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print('\nMasukkan Angka Sesuai Pilihan Saja Dong!')
            continue

idLama = []
def valid_changeData(databaseBuku):
    tampilanDaftarBuku(databaseBuku, headers=HEADERS, title='\nTabel Inventory Buku\n')
    query_cari_id=[]

    for angka_id, valueID in enumerate (databaseBuku):
        query_cari_id.append(valueID[0])

    while True:
        input_change_data = int_validation('\n Pilih ID Buku yang Ingin Diubah: ')

        if input_change_data not in query_cari_id:
            print('\nMaaf, ID Tidak Terdaftar!')
            continue
        else:
            data_filter = [] 
            idLama.append(int(input_change_data)) 
            for idx, item in enumerate(databaseBuku):
                if input_change_data == item[0]:
                    data_filter.append(databaseBuku[idx])
            tampilanDaftarBuku(data_filter)
            changeDaftarBuku(databaseBuku)
        break

def changeDaftarBuku(databaseBuku):
    while True:
        validasiDulu = input('Lanjutkan Mengubah? (Yes/No): ')

        if validasiDulu.lower() in ('yes', 'y'):
            changeDaftarBuku2(databaseBuku)
        elif validasiDulu.lower() in ('no', 'n'):
            print('Update Dibatalkan!')
            changeData(databaseBuku)
        else:
            print('Masukkan Yes/No saja!')
            continue
        

main_change_data2 = f"""
Apa yang ingin Anda Ubah?
1. ID Buku
2. Judul Buku
3. Penulis
4. Penerbit
5. Genre
6. Stok Buku
7. Batal
"""

def changeDaftarBuku2(databaseBuku):
    while True:
        pilihan_ubah = input(main_change_data2)
        if pilihan_ubah == '1':
            ubahID(databaseBuku)
        elif pilihan_ubah == '2':
            ubahJudul(databaseBuku)
        elif pilihan_ubah == '3':
            ubahPenulis()
        elif pilihan_ubah == '4':
            ubahPenerbit(databaseBuku)
        elif pilihan_ubah == '5':
            ubahGenre(databaseBuku)
        elif pilihan_ubah == '6' :
            ubahStok(databaseBuku)
        elif pilihan_ubah == '7':
            changeData(databaseBuku)
        else:
            print('Masukkan Angka Pilihan Sesuai Daftar!')
            continue
        
def ubahID(databaseBuku):
    query_cari_id=[]
    for angka_id, valueID in enumerate (databaseBuku):
        query_cari_id.append(valueID[0])

    while True:
        idBaru = int_validation('\nMasukkan ID baru: ')
        if idBaru in query_cari_id:
            print('\nMaaf, ID Susah Terdaftar, Masukkan ID Lain!')
            continue
        else:
            gantiID(databaseBuku, idLama, idBaru)
            break

def gantiID(databaseBuku, idLama, idBaru):
    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[0] = int(idBaru)
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue

def ubahJudul(databaseBuku):
    judulBaru = strnum_validation('Masukkan Judul Baru: ')

    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[1] = judulBaru.title()
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue

def ubahPenulis(databaseBuku):
    penulisBaru = str_validation('Masukkan Nama Penulis Baru: ')

    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[2] = penulisBaru.title()
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue


def ubahPenerbit(databaseBuku):
    penerbitBaru = str_validation('Masukkan Nama Penerbit Baru: ')

    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[3] = penerbitBaru.title()
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue


def ubahGenre(databaseBuku):
    genreBaru = str_validation('Masukkan Genre Baru: ')

    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[4] = genreBaru.title()
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue


def ubahStok(databaseBuku):
    stockBaru = int_validation('\nMasukkan Jumlah Buku Baru: ')
    for buku in databaseBuku:
        if buku[0] == int(idLama[-1]):
            while True:
                validasiDulu = input('Simpan Data? (Yes/No): ')
                if validasiDulu.lower() in ('yes', 'y'):
                    buku[5] = int(stockBaru)
                    print('Data Berhasil Disimpan!')
                    tampilanDaftarBuku(databaseBuku)
                    changeData(databaseBuku)
                    break
                elif validasiDulu.lower() in ('no', 'n'):
                    print('Data Tidak Disimpan!')
                    changeData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue

# Fungsi Menghapus Database
menu_hapus = f"""
Pilih Salah Satu Cara Untuk Menghapus Daftar Buku
1. Hapus Berdasarkan ID
2. Hapus Semua Daftar Buku
3. Kembali ke Menu Utama
"""
def deleteData(databaseBuku):
    while True:
        inputDelete = input(menu_hapus)
        if inputDelete == '1':
            hapusID(databaseBuku)
        elif inputDelete == '2':
            hapusDaftar(databaseBuku)
        elif inputDelete == '3':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print('Masukkan Angka Sesuai Pilihan!')
            continue

def hapusID(databaseBuku):
    query_cari_id=[]
    for angka_id, valueID in enumerate (databaseBuku):
        query_cari_id.append(valueID[0])
    tampilanDaftarBuku(databaseBuku)

    while True:
        input_hapus_id = int_validation('Silakan Masukkan ID Buku yang Ingin Dihapus: ')
        if input_hapus_id not in query_cari_id:
                print('\nMaaf, ID Tidak Terdaftar!')
                continue
        else:
            data_filter = []  
            for idx, item in enumerate(databaseBuku):
                if input_hapus_id == item[0]:
                    data_filter.append(databaseBuku[idx])
            tampilanDaftarBuku(data_filter)
            while True:
                input_hapus_daftar = input('Hapus Data Terpilih? (Yes/No): ')
                if input_hapus_daftar.lower() in ('yes', 'y'): 
                    for idx, item in enumerate(databaseBuku):
                        if input_hapus_id == item[0]:
                            del databaseBuku[idx]
                            print('Data Berhasil Dihapus!')
                            tampilanDaftarBuku(databaseBuku)
                            deleteData(databaseBuku)
                elif input_hapus_daftar.lower() in ('no', 'n'):
                    print('Tidak Ada Data yang Dihapus!')
                    deleteData(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue

def hapusDaftar(databaseBuku):
    tampilanDaftarBuku(databaseBuku)
    while True:
        input_hapus_daftar = input('Hapus Semua Daftar Buku? (Yes/No): ')
        if input_hapus_daftar.lower() in ('yes', 'y'):
            databaseBuku.clear()
            print('Data Berhasil Dihapus Semua!')
            tampilanDaftarBuku(databaseBuku)
            deleteData(databaseBuku)
        elif input_hapus_daftar.lower() in ('no', 'n'):
            print('Tidak Ada Data Tidak Dihapus!')
            deleteData(databaseBuku)
        else:
            print('Masukkan Yes/No saja!')
        continue

# Fungsi Peminjaman Buku
main_pinjam = f"""
Apa yang Ingin Anda Lakukan?
1. Pinjam Buku
2. Kembali ke Menu Utama
"""

def pinjam(databaseBuku):
    while True:
        input_pinjam = input(main_pinjam)
        
        if input_pinjam == '1':
            pinjamBuku(databaseBuku)
        elif input_pinjam == '2':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print ('\nMasukkan Angka Sesui Pilihan!')
            continue

def pinjamBuku(databaseBuku):
    query_cari_id=[]
    for angka_id, valueID in enumerate (databaseBuku):
        query_cari_id.append(valueID[0])
    tampilanDaftarBuku(databaseBuku)

    while True:
        input_pinjam_buku = int_validation('\nMasukkan ID Buku yang Ingin Dipinjam: ')
        if input_pinjam_buku not in query_cari_id:
                print('\nMaaf, ID Tidak Terdaftar!')
                continue
        else:
            data_filter = []  
            for idx, item in enumerate(databaseBuku):
                if input_pinjam_buku == item[0]:
                    data_filter.append(databaseBuku[idx])
            tampilanDaftarBuku(data_filter)

            while True:
                input_validasi_pinjam = input('Ingin Pinjam Buku Tersebut? (Yes/No): ')
                if input_validasi_pinjam.lower() in ('yes', 'y'): 
                    for idx, item in enumerate(databaseBuku):
                        if input_pinjam_buku == item[0]:
                            if item[5] <= 0:
                                print('\nMaaf Stock Buku Tidak Mencukupi!')
                                pinjam(databaseBuku)
                            else:
                                while True:
                                    id_peminjam = int_validation('\nMasukkan ID Peminjam (Nomor Induk Siswa/Pegawai): ')
                                    for indexPinjam, data in enumerate(database_buku_dipinjam):
                                        if data[0] == input_pinjam_buku and data[6] == id_peminjam:
                                            print(f'ID Peminjam {id_peminjam} sedang meminjam buku tersebut. Maks Pinjaman 1 Buku')
                                            pinjam(databaseBuku)
                                        else:
                                            tanggal_pinjaman = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                            buku_dipinjam = list(databaseBuku[idx])
                                            buku_dipinjam[-1] = 1 #Hanya boleh meminjam 1 buku untuk setiap ID buku dan ID peminjam
                                            database_buku_dipinjam.append(buku_dipinjam + [id_peminjam, tanggal_pinjaman])
                                            databaseBuku[idx][-1] -= 1
                                            print('Buku Berhasil Dipinjam!')
                                            tabelPinjaman(database_buku_dipinjam)
                                            pinjam(databaseBuku)
                elif input_validasi_pinjam.lower() in ('no', 'n'):
                    print('Buku Tidak Jadi Dipinjam!')
                    pinjam(databaseBuku)
                else:
                    print('Masukkan Yes/No saja!')
                continue

# Fungsi Menampilkan Daftar Buku Yang Dipinjam
main_daftarPinjam = f"""
Pilih Menu di Bawah
1. Menampilkan Semua Daftar Pinjaman
2. Kembali ke Menu Utama

"""
def daftarPinjamanBuku(database_buku_dipinjam):
    while True:
        menu_daftar_pinjaman = input(main_daftarPinjam)
        if menu_daftar_pinjaman == '1':
            if len(database_buku_dipinjam) == 0:
                print('Tidak Ada Data Pinjaman!')
                continue
            else:
                tabelPinjaman(database_buku_dipinjam)
                continue
        elif menu_daftar_pinjaman == '2':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print('\nMasukkan Angka Sesuai Pilihan!')
            continue


# Fungsi Mengembalikan Buku Yang Dipinjam
main_returnBuku = f"""
Pilih Menu di Bawah
1. Mengembalikan Buku
2. Kembali ke Menu Utama
"""
def returnBuku(database_buku_dipinjam):
    while True:
        menu_return_buku = input(main_returnBuku)
        if menu_return_buku == '1':
            returnBook(database_buku_dipinjam)
        elif menu_return_buku == '2':
            import main_perpustakaan
            main_perpustakaan.main()
            break
        else:
            print('\nMasukkan Angka Sesuai Pilihan!')
            continue

def returnBook(database_buku_dipinjam):
    query_cari_id=[]
    while True:
        input_id = int_validation('\nMasukkan ID Buku: ')
        input_NIP = int_validation('\nMasukkan ID Peminjam Buku: ')

        for indexPinjam, data in enumerate(database_buku_dipinjam):
            if data[0] == input_id and data[6] == input_NIP:  
                query_cari_id.append(data)
                tabelPinjaman(query_cari_id)
                while True:
                    validasi_return = input('Ingin Mengembalikan Buku Tersebut? (Yes/No): ')
                    if validasi_return.lower() in ('yes', 'y'):
                        for idx, item in enumerate(databaseBuku):
                            if input_id == item[0]:
                                databaseBuku[idx][-1] += 1
                        del database_buku_dipinjam[indexPinjam]
                        print ('Buku Berhasil Dikembalikan!')
                        returnBuku(databaseBuku) 
                    elif validasi_return.lower() in ('no', 'n'):
                        print('Buku Tidak Dikembalikan!')
                        returnBuku(databaseBuku) 
                    else:
                        print('Pilih Yes/No Saja!')
                        continue
            else:
                print('Data Tidak Ditemukan!')
                continue

# Fungsi Validasi Angka
def int_validation(prompt):
    """Fungsi untuk validasi input bilangan bulat.

    Args:
        prompt (String): Pesan tampilan pada prompt.

    Returns:
        int: bilangan bulat.
    """
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print('Tidak boleh Nol atau Negatif!')
                continue
            else:
                break
        except:
            print('Silahkan inputkan angka saja!')
            continue
    return int(num)

# Fungsi Validasi String
def str_validation(prompt):
    """Fungsi untuk validasi input teks.

    Args:
        prompt (String): Pesan tampilan pada prompt.

    Returns:
        str: teks.
    """
    while True:
        sentence = input(prompt)
        if sentence.isalpha():
            break
        else:
            print('Silahkan input kan alfabet!')
            continue

    return sentence

# Fungsi Validasi Kombinasi Angka dan Alfabet
def strnum_validation(prompt):
    """Fungsi untuk validasi input teks khusus Judul Buku. Karena judul buku bisa berupa angka.

    Args:
        prompt (String): Pesan tampilan pada prompt.

    Returns:
        str: teks.
    """
    while True:
        sentence_num = input(prompt)
        if sentence_num.isalnum():
            break
        else:
            print('Silahkan input kan alfabet/angka!')
            continue
    return sentence_num