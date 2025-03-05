def show_table(db):
    # dia ngecek dbnya close apa ngga? klo close reconnect
    if not db.is_connected():
        db.reconnect()
    cursor = db.cursor()
    cursor.execute("select count(*) from students")
    result = cursor.fetchone()

    if result[0] == 0:
        print("Tidak ada data siswa yang tersimpan, Silahkan tambahkan data siswa terlebih dahulu")
        print("#"*100)
    else:
        print("Pilih opsi selanjutnya: ")
        print("1. Tampilkan semua data siswa")
        print("2. Mencari data siswa")
        print("3. Kembali")
        print("#"*100)
        read = input("Silahkan anda pilih menu yang sesuai: ")
        if int(read) == 1:
            cursor.execute("select * from students")
            result = cursor.fetchall()
            print("Data Siswa:")
            print("="*100)
            print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
            for data in result:
                print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
            print("="*100)
        elif int(read) == 2:
            print("Cari Data Siswa")
            print("#"*100)
            nama = input("Masukkan nama siswa yang ingin dicari: ")
            cursor.execute("select * from students where name = %s", (nama,))
            result = cursor.fetchall()
            if result:
                print("Ditemukan data siswa sebanyak {} data".format(len(result)))
                print("="*100)
                print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
                for data in result:
                    print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
                print("="*100)
            else:
                print("Data siswa tidak ditemukan")
                print("#"*100)
    cursor.close()
    db.close()
    return None

def create_data(db):
    if not db.is_connected():
        db.reconnect()
    cursor = db.cursor()
    print("Tambah Data Siswa")
    print("#"*100)
    nama = input("Masukkan nama siswa: ")
    umur = input("Masukkan umur siswa: ")
    kelas = input("Masukkan kelas siswa: ")
    nilai_ipa = input("Masukkan nilai IPA siswa: ")
    nilai_matematika = input("Masukkan nilai Matematika siswa: ")
    nilai_bahasa_inggris = input("Masukkan nilai Bahasa Inggris siswa: ")
    nilai_bahasa_indonesia = input("Masukkan nilai Bahasa Indonesia siswa: ")
    
    sql = "insert into students (name, age, class, science_score, math_score, english_score, bahasa_score) values (%s, %s, %s, %s, %s, %s, %s)"
    val = (nama, umur, kelas, nilai_ipa, nilai_matematika, nilai_bahasa_inggris, nilai_bahasa_indonesia)
    
    cursor.execute(sql, val)
    db.commit()
    
    print("Data siswa berhasil ditambahkan")
    print("#"*100)
    cursor.close()
    db.close()
    return None