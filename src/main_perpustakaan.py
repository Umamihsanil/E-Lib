import os
import sys
import function
from function import databaseBuku
from function import database_buku_dipinjam

# Main Menu
main_menu = f"""
Selamat Datang di Perpustakaan Ganesha

Menu:
1. Menampilkan Daftar Buku
2. Menambah Daftar Buku
3. Mengubah Daftar Buku
4. Menghapus Buku Dari Daftar
5. Peminjaman Buku
6. Daftar Buku Yang Dipinjam
7. Pengembalian
8. Exit
"""

def main():
    global databaseBuku
    global database_buku_dipinjam
    while True:
        numChoice = input(main_menu)

        if numChoice == '1':
            function.read(databaseBuku)
        elif numChoice == '2':
            function.tambahBuku(databaseBuku)
        elif numChoice == '3':
            function.changeData(databaseBuku)
        elif numChoice == '4':
            function.deleteData(databaseBuku)
        elif numChoice == '5':
            function.pinjam(databaseBuku)
        elif numChoice == '6':
            function.daftarPinjamanBuku(database_buku_dipinjam)
        elif numChoice == '7':
            function.returnBuku(database_buku_dipinjam)
        elif numChoice == '8':
            clear_screen()
            print('Terima Kasih, Sampai Jumpa!')
            sys.exit()
        else:
            print('Masukkan Angka Pilihan Sesuai Daftar!')
            continue

def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

main()