# Ganti list_data_buku dengan list_data_gudang
List_Daftar_Gudang = [
    {
        "ID_Barang"     : "001",
        "Nama_Barang"   : "Komputer",
        "Jenis_Barang"  : "Elektronik",
        "Merek"         : "Asus",
        "Jumlah_Stok"   : 10,
    },
    {
        "ID_Barang"     : "002",
        "Nama_Barang"   : "Printer",
        "Jenis_Barang"  : "Elektronik",
        "Merek"         : "Epson",
        "Jumlah_Stok"   : 5,
    },
    {
        "ID_Barang"     : "003",
        "Nama_Barang"   : "Meja",
        "Jenis_Barang"  : "Furniture",
        "Merek"         : "IKEA",
        "Jumlah_Stok"   : 20,
    },
    {
        "ID_Barang"     : "004",
        "Nama_Barang"   : "Buku",
        "Jenis_Barang"  : "Stationery",
        "Merek"         : "Gramedia",
        "Jumlah_Stok"   : 50,
    },
    {
        "ID_Barang"     : "005",
        "Nama_Barang"   : "Kamera",
        "Jenis_Barang"  : "Elektronik",
        "Merek"         : "Canon",
        "Jumlah_Stok"   : 8,
    },
]

# Update fungsi Tabel_Daftar_Gudang
from tabulate import tabulate
def Tabel_Daftar_Gudang(list_Data_Gudang):
    headers = ["ID_Barang", "Nama_Barang", "Jenis_Barang", "Merek", "Jumlah_Stok"]
    table_data = []

    for data in list_Data_Gudang:
        baris = [data["ID_Barang"], data["Nama_Barang"], data["Jenis_Barang"], data["Merek"], data["Jumlah_Stok"]]
        table_data.append(baris)

    print(tabulate(table_data, headers, tablefmt="grid"))

# Update fungsi Tabel_Daftar_Gudang_Update
from tabulate import tabulate
def Tabel_Daftar_Gudang_Update(list_Data, x, Data_Baru):
    headers = ["ID_Barang", "Nama_Barang", "Jenis_Barang", "Merek", "Jumlah_Stok"]
    table_data = []

    for data in list_Data:
        baris = [data["ID_Barang"], data["Nama_Barang"], data["Jenis_Barang"], data["Merek"], data["Jumlah_Stok"]]
        table_data.append(baris)

    for baris in table_data:
        baris[x - 1] = Data_Baru

    # Display the updated table using tabulate
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Update fungsi CariDaftar_Gudang
def CariDaftar_Gudang(Input):
    DaftarCari = (list(filter(lambda data: data['ID_Barang'] == str(Input), List_Daftar_Gudang)))
    return DaftarCari

# Update fungsi Update_Gudang
def Update_Gudang(Data, Kolom, Data_baru):
    Input_Update_Gudang = (input("\tApakah data yang diupdate sudah sesuai? (Ya/Tidak): "))
    if Input_Update_Gudang == "ya":
        Data[0][Kolom] = Data_baru
        print("\tData yang Anda upload sudah diupdate!")
    elif Input_Update_Gudang == "tidak":
        print("\tData yang Anda upload tidak diupdate!")
    else:
        print("\tInput tidak valid. Harap masukkan 'Ya' atau 'Tidak'.")

# Update fungsi add_Gudang
def add_Gudang(List_Daftar_Gudang):
    input_add = (int(input("""Menu Menambah Daftar Gudang:
1. Menambah daftar barang
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:""")))

    if input_add == 1:   
        add_ID_Barang_Baru    = str(input("\tMasukkan ID Barang yang ingin Anda tambahkan:"))
        list_value          = [str(value) for data_gudang in List_Daftar_Gudang for value in data_gudang.values()] 
        if str(add_ID_Barang_Baru) in list_value:
            print("\n\tData yang Anda input sudah terdapat di sistem\n")
            return(add_Gudang(List_Daftar_Gudang))   
        else:
            add_Nama_Barang_Baru     = input("\tSilahkan masukkan nama barang:")
            add_Jenis_Barang_Baru    = input("\tSilahkan masukkan jenis barang:")
            add_Merek_Baru           = input("\tSilahkan masukkan merek:")
            add_Jumlah_Stok_Baru     = int(input("\tSilahkan masukkan jumlah stok:"))
            List_Daftar_Gudang_Baru  = [{
                "ID_Barang"     : add_ID_Barang_Baru,
                "Nama_Barang"   : add_Nama_Barang_Baru,
                "Jenis_Barang"  : add_Jenis_Barang_Baru,
                "Merek"         : add_Merek_Baru,
                "Jumlah_Stok"   : add_Jumlah_Stok_Baru
            }]

            Tabel_Daftar_Gudang(List_Daftar_Gudang_Baru)
            penyimpanan_data = (input("\n\t Apakah Anda ingin menyimpan Data ke sistem (ya/tidak)?")).lower()
            if penyimpanan_data == "ya":
                List_Daftar_Gudang += (List_Daftar_Gudang_Baru)
                Tabel_Daftar_Gudang(List_Daftar_Gudang)
                print("\n\tData barang baru tersimpan!")
            else:
                print("\n\tData tidak tersimpan!")
    elif input_add == 2:
        Menu_Gudang()
    else:
        print("\n\tTidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
    add_Gudang(List_Daftar_Gudang)

# Update fungsi Update_Gudang
def Update_Gudang(Data, Kolom, Data_baru):
    Input_Update_Gudang = (input("\tApakah data yang diupdate sudah sesuai? (Ya/Tidak): "))
    if Input_Update_Gudang == "ya":
        Data[0][Kolom] = Data_baru
        print("\tData yang Anda upload sudah diupdate!")
    elif Input_Update_Gudang == "tidak":
        print("\tData yang Anda upload tidak diupdate!")
    else:
        print("\tInput tidak valid. Harap masukkan 'Ya' atau 'Tidak'.")

# Update fungsi update_Gudang
def update_Gudang():
    input_update = (int(input('''Menu Mengubah Daftar Gudang:
1. Mengubah daftar barang
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:''')))
    
    if input_update == 1:
        Update_Barang = str(input("\tMasukkan ID Barang yang ingin Anda ubah:"))
        list_value  = [str(value) for data_gudang in List_Daftar_Gudang for value in data_gudang.values()]
        if Update_Barang not in list_value:
            print("\n\tData yang Anda input tidak terdapat di sistem silahkan masukkan kembali ID Barang yang benar\n")
        
        else:
            CariDaftar_Gudang(Update_Barang)
            Tabel_Daftar_Gudang(CariDaftar_Gudang(Update_Barang))
            input_update = (input("\tApakah Anda yakin ingin melakukan update data berikut? (Ya/Tidak): ")).lower()
            if input_update== "ya":
                input_kategori = int(input("""\tKategori Database Barang: 
    1. ID Barang 
    2. Nama Barang
    3. Jenis Barang
    4. Merek
    5. Jumlah Stok
    Masukkan kategori yang ingin diubah: """))
                
                if input_kategori == 1:
                    Masukkan_Data = str(input("\tMasukkan data baru yang ingin diinput: ")).lower()
                    Tabel_Daftar_Gudang_Update(CariDaftar_Gudang(Update_Barang),1,Masukkan_Data)
                    Update_Gudang(CariDaftar_Gudang(Update_Barang), "ID_Barang",Masukkan_Data)

                elif input_kategori == 2:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Gudang_Update(CariDaftar_Gudang(Update_Barang),2,Masukkan_Data)
                    Update_Gudang(CariDaftar_Gudang(Update_Barang), "Nama_Barang",Masukkan_Data)
               

                elif input_kategori == 3:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Gudang_Update(CariDaftar_Gudang(Update_Barang),3,Masukkan_Data)
                    Update_Gudang(CariDaftar_Gudang(Update_Barang), "Jenis_Barang",Masukkan_Data)


                elif input_kategori == 4:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Gudang_Update(CariDaftar_Gudang(Update_Barang),4,Masukkan_Data)
                    Update_Gudang(CariDaftar_Gudang(Update_Barang), "Merek",Masukkan_Data)


                elif input_kategori == 5:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Gudang_Update(CariDaftar_Gudang(Update_Barang),5,Masukkan_Data)
                    Update_Gudang(CariDaftar_Gudang(Update_Barang), "Jumlah_Stok",Masukkan_Data)

                else: 
                    print("\tKategori tidak ada!")

    elif input_update == 2:
        Menu_Gudang()
    else:
        print("\tInput yang Anda masukkan tidak valid. Harap masukkan angka yang tersedia.")
    update_Gudang()

# Update fungsi delete_Gudang
def delete_Gudang():
    input_Delete = (int(input('''Menu Menghapus Daftar Gudang:
1. Menghapus Daftar Barang
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:''')))
    
    
    if input_Delete == 1:
        Delete_Barang = str(input("\tMasukkan ID Barang yang ingin Anda ubah:"))
        list_value  = [str(value) for data_gudang in List_Daftar_Gudang for value in data_gudang.values()]
        if Delete_Barang not in list_value:
            print("\n\t Maaf, Data yang ingin Anda hapus tidak ada. Silahkan menghapuskan data yang tersedia!")

        else:
            CariDaftar_Gudang(Delete_Barang)
            Tabel_Daftar_Gudang(CariDaftar_Gudang(Delete_Barang))
            Menghapus = input("\n\t Hapus Data (Ya/Tidak)?").lower()
            if Menghapus == "ya":            
                for item in CariDaftar_Gudang(Delete_Barang): 
                    List_Daftar_Gudang.remove(item)
                print("\n\t Data yang ingin Anda hapus telah berhasil terhapus!")

            else: 
                print("\n\t Data tidak berhasil terhapus!")
    elif input_Delete == 2:
        Menu_Gudang()
    else:
        print("\n\tTidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
    delete_Gudang()

# Update fungsi Menu
def Menu_Gudang():
    while True:
        pilihanMenu = input('''
Selamat Datang di Gudang

List Menu :
1. Menampilkan Daftar Barang
2. Menambah Daftar Barang
3. Mengubah Daftar Barang
4. Menghapus Daftar Barang
5. Exit Program

Masukkan angka Menu yang ingin Anda jalankan : ''')

        if(pilihanMenu == "1") :
            Tabel_Daftar_Gudang(List_Daftar_Gudang)
        elif(pilihanMenu == "2") :
            add_Gudang(List_Daftar_Gudang)
        elif(pilihanMenu == "3") :
            update_Gudang(List_Daftar_Gudang)
        elif(pilihanMenu == "4") :
            delete_Gudang()
        else:
            Menu_Gudang()

# Memanggil Menu utama
Menu_Gudang()
