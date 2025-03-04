def create_data(db):
    name = input("Masukkan nama siswa: ")
    age = input("Masukkan umur siswa: ")
    Class = input("Masukkan kelas siswa: ")

    science_score = int(input("Masukkan nilai IPA siswa: "))
    math_score = int(input("Masukkan nilai Matematika siswa: "))
    english_score = int(input("Masukkan nilai B.Inggris siswa: "))
    bahasa_score = int(input("Masukkan nilai B.Indonesia siswa: "))

    print("="*100)
    set_dict_siswa = {
        "Name" : name,
        "Age" : age,
        "Class" : Class,
        "Science" : science_score,
        "Math": math_score,
        "English": english_score,
        "Bahasa": bahasa_score 
    }

    confirmed = input("Apakah data yang anda masukkan sudah benar? Y/N: ")
    if confirmed.capitalize == 'Y':
        mycursor = db.cursor()

        sql = "INSERT INTO students (name, age, class, science_score, math_score, english_score, bahasa_score) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (set_dict_siswa['Name'], set_dict_siswa['Age'], set_dict_siswa['Class'], set_dict_siswa['Science'], set_dict_siswa['Math'], set_dict_siswa['English'], set_dict_siswa['Bahasa'])
        
        mycursor.execute(sql, val)
        db.commit()

        print("Data berhasil dimasukkan!")
        print("="*100)
    else:
        print("Data tidak berhasil dimasukkan!")

def search_data(name, list):
    search_result=[]
    for item in list:
        if item['Name'] == name:
            search_result.append(item)    
    if len(search_result) == 0:
        print("Data tidak ditemukan")
    else:
        print(f"{len(search_result)} data ditemukan")
        show_table(search_result)

def show_table(rest):

    for row in rest:
        print(row)
    # keys = list[0].keys()
    # print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("No", *keys))

    # for index, item in enumerate(list):
    #     print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(index+1, item['Name'], item['Age'], 
    #                                                                 item['Class'], item['Science'],
    #                                                                 item['Math'], item['English'],
    #                                                                 item['Bahasa']))
    # print("="*100)

def update_data(list, index):
    if index <= len(list):
        keys = list[0].keys()
        print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("No", *keys))

        value = list[index-1]
        print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(index, value['Name'], value['Age'], 
                                                                    value['Class'], value['Science'],
                                                                    value['Math'], value['English'],
                                                                    value['Bahasa']))

        print("""
            Kolom yang dapat diubah:
            1. Nama
            2. Umur
            3. Kelas
            4. Nilai IPA
            5. Nilai Matematika
            6. Nilai B.Inggris
            7. Nilai B.Indonesia
        """)

        edit_command = int(input("Pilih Kolom yang ingin anda ubah: "))

        if edit_command == 1:
            name = input("Masukkan ubah data nama baru: ")
            value['Name'] = name
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 2:
            age = input("Masukkan ubah data umur baru: ")
            value['Age'] = age
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 3:
            Class = input("Masukkan ubah data kelas baru: ")
            value['Class'] = Class
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 4:
            science = input("Masukkan ubah data nilai IPA baru: ")
            value['Science'] = science
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 5:
            math = input("Masukkan ubah data nilai Matematika baru: ")
            value['Math'] = math
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 6:
            english = input("Masukkan ubah data nilai B.Inggris baru: ")
            value['English'] = english
            print("Data berhasil diubah!")
            print("="*100)
        elif edit_command == 7:
            indonesia = input("Masukkan ubah data nilai B.Indonesia baru: ")
            value['Bahasa'] = indonesia
            print("Data berhasil diubah!")
            print("="*100)
        else:
            print("Kolom yang anda masukkan tidak sesuai dengan jumlah kolom!")
            print("="*100)
    else:
        print("Index yang anda masukkan tidak sesuai dengan jumlah data!")
        print("="*100)

def delete_data(list, index):
    if index <= len(list):
        keys = list[0].keys()
        print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("No", *keys))

        value = list[index-1]
        print("{:<8} {:<10} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(index, value['Name'], value['Age'], 
                                                                    value['Class'], value['Science'],
                                                                    value['Math'], value['English'],
                                                                    value['Bahasa']))
        
        confirmation = input("Apa anda yakin ingin menghapus data? Y/N: ")
        if confirmation == 'Y':
            list.pop(index-1)
        elif confirmation == 'N':
            print("Anda memutuskan untuk tidak melanjutkan proses")
        else:
            print("Proses dibatalkan, masukkan command yang sesuai! ")
