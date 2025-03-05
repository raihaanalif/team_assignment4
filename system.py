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
        elif int(read) == 3:
            return None
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

def update_data(db):
    if not db.is_connected():
        db.reconnect()
    cursor = db.cursor()
    print("Update Data Siswa")
    print("#"*100)
    print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
    cursor.execute("select * from students")
    result = cursor.fetchall()
    for data in result:
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    id = input("Masukkan id siswa yang ingin diupdate: ")
    cursor.execute("select * from students where student_id = %s", (id,))
    result = cursor.fetchone()
    if result:
        print("Data Siswa:")
        print("="*100)
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
        print("="*100)
        print("Silahkan masukkan data yang ingin diupdate")
        print("#"*100)
        print("Data apa yang ingin diupdate?")
        print("1. Nama")
        print("2. Umur")
        print("3. Kelas")
        print("4. Nilai IPA")
        print("5. Nilai Matematika")
        print("6. Nilai Bahasa Inggris")
        print("7. Nilai Bahasa Indonesia")
        print("#"*100)
        pilihan = int(input("Silahkan pilih data yang ingin diupdate: "))
        if pilihan == 1:
            nama = input("Masukkan nama baru: ")
            sql = "update students set name = %s where student_id = %s"
            val = (nama, result[0])
        elif pilihan == 2:
            umur = input("Masukkan umur baru: ")
            sql = "update students set age = %s where student_id = %s"
            val = (umur, result[0])
        elif pilihan == 3:
            kelas = input("Masukkan kelas baru: ")
            sql = "update students set class = %s where student_id = %s"
            val = (kelas, result[0])
        elif pilihan == 4:
            nilai_ipa = input("Masukkan nilai IPA baru: ")
            sql = "update students set science_score = %s student_id = %s"
            val = (nilai_ipa, result[0])
        elif pilihan == 5:
            nilai_matematika = input("Masukkan nilai Matematika baru: ")
            sql = "update students set math_score = %s where student_id = %s"
            val = (nilai_matematika, result[0])
        elif pilihan == 6:
            nilai_bahasa_inggris = input("Masukkan nilai Bahasa Inggris baru: ")
            sql = "update students set english_score = %s where student_id = %s"
            val = (nilai_bahasa_inggris, result[0])
        elif pilihan == 7:
            nilai_bahasa_indonesia = input("Masukkan nilai Bahasa Indonesia baru: ")
            sql = "update students set bahasa_score = %s where student_id = %s"
            val = (nilai_bahasa_indonesia, result[0])

        cursor.execute(sql, val)
        db.commit()
        
        print("Data siswa berhasil diupdate")
        print("#"*100)
    else:
        print("Data siswa tidak ditemukan")
    cursor.close()
    db.close()

def delete_data(db):
    if not db.is_connected():
        db.reconnect()
    cursor = db.cursor()
    print("Hapus Data Siswa")
    print("#"*100)
    print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
    cursor.execute("select * from students")
    result = cursor.fetchall()
    for data in result:
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    id = input("Masukkan id siswa yang ingin dihapus: ")
    cursor.execute("select * from students where student_id = %s", (id,))
    result = cursor.fetchone()
    if result:
        print("Data Siswa:")
        print("="*100)
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Nama", "Umur", "Kelas", "IPA", "Math", "B.Inggris", "B.Indonesia"))
        print("{:<8} {:<20} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
        print("="*100)
        konfirmasi = input("Apakah anda yakin ingin menghapus data siswa ini? (Y/N): ")
        if konfirmasi.lower() == "y":
            cursor.execute("delete from students where student_id = %s", (id,))
            db.commit()
            print("Data siswa berhasil dihapus")
            print("#"*100)
        else:
            print("Data siswa tidak jadi dihapus")
            print("#"*100)
    else:
        print("Data siswa tidak ditemukan")
        print("#"*100)
    cursor.close()
    db.close()
    return None