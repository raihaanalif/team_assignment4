import system

def main(db):
    start = True
    while start == True:
        print("Menu:")
        print("1. Tampilkan Data Siswa")
        print("2. Tambah Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Logout")
        print("#"*100)
        menu = int(input("Silahkan anda pilih menu yang sesuai: "))
        if menu == 1:
            system.show_table(db)
        elif menu == 2:

            system.create_data(db)

            # print("Tambah Data Siswa")
        elif menu == 3:
            print("Update Data Siswa")
        elif menu == 4:
            print("Hapus Data Siswa")
        elif menu == 5:
            print("Anda berhasil logout")
            break