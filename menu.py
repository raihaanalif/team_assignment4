import system

def main(mydb):
    start = True
    list_data_siswa = []

    while start == True:
        print("""
            Menu:
            1. Tampilkan data siswa
            2. Tambahkan data siswa terbaru 
            3. Edit data siswa
            4. Hapus data siswa
            5. Logout
        """)
        menu = int(input("Masukkan menu yang ingin anda akses: "))
        print("="*100)
        if menu == 1:
            cursor = mydb.cursor()
            cursor.execute("SELECT COUNT(*) FROM students")
            result = cursor.fetchone()

            if result[0] == 0:
                print("Database masih kosong, silahkan masukkan beberapa data terlebih dahulu")
                print("="*100)
            else:
                print("""
                Pilih opsi selanjutnya:

                1. Melihat semua data siswa.
                2. Mencari data

                """)
                option = int(input("Masukkan pilihan anda: "))
                print("="*100)
                if option == 1:
                    # menampilkan seluruh hasil data
                    system.show_table(result)
                    
                elif option == 2:
                    # melakukan pencarian terhadap data sesuai dengan namanya
                    search = input("Masukkan nama siswa yang ingin anda cari: ")
                    system.search_data(search, list_data_siswa)
            # print(1)
            # memperintahkan program untuk menampilkan data tergantung dengan perintah selanjutnya


            # if len(list_data_siswa) == 0:
            #     print("Database masih kosong, silahkan masukkan beberapa data terlebih dahulu")
            #     print("="*100)
            # else:
            #     print("""
            #     Pilih opsi selanjutnya:

            #     1. Melihat semua data siswa.
            #     2. Mencari data

            #     """)
            #     option = int(input("Masukkan pilihan anda: "))
            #     print("="*100)
            #     if option == 1:
            #         # menampilkan seluruh hasil data
            #         system.show_table(list_data_siswa)
                    
            #     elif option == 2:
            #         # melakukan pencarian terhadap data sesuai dengan namanya
            #         search = input("Masukkan nama siswa yang ingin anda cari: ")
            #         system.search_data(search, list_data_siswa)
            cursor.close()
            mydb.close()
        elif menu == 2:
            #print(2)
            data_siswa = system.create_data()
            list_data_siswa.append(data_siswa)

        elif menu == 3:
            # print(3)
            # melakukan update atau edit atas suatu data di dalam table
            if len(list_data_siswa) == 0:
                print("Database masih kosong, silahkan masukkan beberapa data terlebih dahulu")
                print("="*100)
            else:
                system.show_table(list_data_siswa)
                find_index = int(input("Pilih index data yang ingin anda edit: "))
                system.update_data(list_data_siswa, find_index)
        
        elif menu == 4:
            if len(list_data_siswa) == 0:
                print("Database masih kosong, silahkan masukkan beberapa data terlebih dahulu")
                print("="*100)
            else:
                system.show_table(list_data_siswa)
                find_index = int(input("Pilih index data yang ingin anda hapus: "))
                system.delete_data(list_data_siswa, find_index)
        elif menu == 5:
            # print(5)
            print("Anda berhasil keluar dari sistem")
            break
            