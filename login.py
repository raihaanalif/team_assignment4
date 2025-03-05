import menu

def login_main(mydb):
    loginBerhasil = False
    
    while loginBerhasil == False:
        print("="*100)
        print("LOGIN")
        print("="*100)
        
        userid = input("Masukkan USER ID anda: ")
        password = input("Masukkan kata sandi anda: ")
    
        mycursor = mydb.cursor()
        sql = "select * from users where username = %s and password = %s"
        val = (userid, password)

        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            print("="*100)
            print("Berhasil Masuk!")
            print("="*100)
            print("Selamat datang", result[1]) # mengasumsikan nama ada di index 3 pada tabel users
            print("="*100)
            
            menu.main(mydb)

            # data_pengguna = {
            #     "user-id": result[0],
            #     "email": result[1],
            #     "password": result[2],
            #     "nama": result[3],
            #     "umur": result[4],
            #     "gender": result[5],
            #     "pekerjaan": result[6],
            #     "kota": result[7],
            #     "rt": result[8],
            #     "rw": result[9],
            #     "latitude": result[10],
            #     "longitude": result[11],
            #     "nomor": result[12]
            # }
            
            loginBerhasil = True
        else:
            print("="*100)
            print("UserID atau kata sandi yang anda masukkan salah!")
            print("="*100)
            
            coba_lagi = input("apakah anda ingin masku kembali? (Y/N): ")
            if coba_lagi.lower() == "n":
                print("="*100)
                print("Terima kasih telah menggunakan layanan kami")
                print("="*100)
                return None

# def tampilan_info_pengguna(data_pengguna):
#     if data_pengguna:
#         print("="*100)
#         print("INFORMASI PENGGUNA")
#         print("="*100)
#         print("Nama:", data_pengguna["nama"])
#         print("Email:", data_pengguna["email"])
#         print("Umur:", data_pengguna["umur"])
#         print("Jenis Kelamin:", data_pengguna["gender"])
#         print("Pekerjaan:", data_pengguna["pekerjaan"])
#         print("Kota:", data_pengguna["kota"])
#         print("RT:", data_pengguna["rt"])
#         print("RW:", data_pengguna["rw"])
#         print("Latitude:", data_pengguna["latitude"])
#         print("Longitude:", data_pengguna["longitude"])
#         print("Nomor Telepon:", data_pengguna["nomor"])
#         print("="*100)

# Contoh penggunaan:
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="nama_pengguna",
#     password="kata_sandi",
#     database="nama_database"
# )

# pengguna = login_main(mydb)
# if pengguna:
#     tampilkan_info_pengguna(pengguna)