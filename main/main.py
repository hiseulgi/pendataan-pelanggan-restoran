import pandas as pd
from datetime import date, datetime
from os import system
from time import sleep 

# inisialisasi class
class Pelanggan():

    def __init__(self):
        self.data = []
        
    def tambah_data(self, nama, jenis, umur, menu):
        tanggal = date.today().strftime("%d/%m/%y")
        waktu = datetime.now().strftime("%H:%M")
        self.data.append({'Tanggal':tanggal,
                    'Waktu':waktu,
                    'Nama':nama,
                    'Gender':jenis,
                    'Umur':umur,
                    'Menu Favorit':menu})

    def tampilkan_data(self):
        df = pd.DataFrame(self.data)
        
        clear()
        print("="*50)
        print("Data Pelanggan Restoran Mas Bagus".center(50,' '))
        print("="*50)
        print(df)
        print("="*50)
        print()
        lanjut = input("Ketik apapun untuk lanjut! ")

    def hapus_data(self, index):
        del self.data[index]
    
    def ekspor_data(self):
        df = pd.DataFrame(self.data)
        tanggal = date.today().strftime("%y%m%d")

        df.to_csv('{}_data-pelanggan.csv'.format(tanggal), \
            mode='a', index=False, encoding="utf-8")
        print("Data telah diekspor ke dalam file CSV!")

# function
def clear():
    system('cls')

def get_option():
    clear()
    print("="*50)
    print("Program Pendataan Pelanggan Restoran Mas Bagus".center(50,' '))
    print("="*50)
    print("1. Tambahkan Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ekspor Data sebagai File CSV")
    print("5. Keluar")
    print("="*50)
    
    pilih = int(input("Masukkan pilihan : "))
    print()
    return pilih

def tambah():
    print("1. Tambahkan Data")
    nama = input("Nama\t\t\t: ")
    jenis = input("Jenis Kelamin (L/P)\t: ")
    umur = int(input("Umur\t\t\t: "))
    menu = input("Menu Favorit\t\t: ")
    
    pelanggan.tambah_data(nama, jenis, umur, menu)

def hapus():
    print("3. Hapus Data")
    index = int(input("Masukkan Index Data \t: "))
    pelanggan.hapus_data(index)
    print("Data pada index ke-", index, "telah terhapus!")

# main program
pelanggan = Pelanggan()
while (True):
    pilih = get_option()

    if (pilih == 1):
        tambah()
        sleep(0.5)
        
    elif (pilih == 2):
        pelanggan.tampilkan_data()
        
    elif (pilih == 3):
        hapus()
        sleep(0.5)
        
    elif (pilih == 4):
        pelanggan.ekspor_data()
        sleep(1)
        
    elif (pilih == 5):
        print("Keluar dari program!")
        break
        
    else:
        print("Tidak ada pilihan!")
        sleep(1)
