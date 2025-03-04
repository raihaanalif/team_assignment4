import connect
import register
import login

print("## Selamat Datang di Database Sekolah Bina Bangsa ###")

def display_menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Silahkan anda pilih menu yang sesuai: ")
    print("#"*100)
    return int(pilihan)

if connect.mydb:
    # print("Database berhasil connect")
    start = True
    while start == True:
        menu = display_menu()
        if menu == 1:
            # print("ini register")
            register.register_main(connect.mydb)
            if register.register == True:
                print("Register berhasil, silahkan langsung login")
        elif menu == 2:
            data_pengguna = login.login_main(connect.mydb)
            if data_pengguna:
                login.tampilan_info_pengguna(data_pengguna) 
        elif menu == 3:
            print("Anda berhasil keluar dari aplikasi")
            break
    
else:
    print("Database tidak connect")



