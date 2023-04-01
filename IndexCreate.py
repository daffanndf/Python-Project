from . import IndexOperation
from .IndexDatabase import DATABASE_NAME
from .IndexRead import read_result

# Function untuk menambahkan data buku baru
def create_result() :
    print("Silahkan masukan data buku yang ingin ditambahkan")
    JUDUL = input("Masukan judul buku        : ")
    PENULIS = input("Masukan penulis buku      : ")
    while True :
        try :
            TAHUN = int(input("Masukan tahun rilis buku  : "))
            if len(str(TAHUN)) == 4 :
                key = IndexOperation.key_book(6)
                date = IndexOperation.date_add()

                with open(DATABASE_NAME, "a", encoding="UTF-8") as file :
                    new_database = f'{key:<6},{date:<10},{JUDUL:<80},{PENULIS:<80},{TAHUN:<4}\n'
                    file.write(new_database)
                print("\nData buku berhasil ditambahkan\n")
                read_result()
                break

            else :
                print("Jumlah angka yang bisa diinput pada tahun adalah 4 angka")
                print("Silahkan inputkan ulang data buku\n")
                continue
        
        except :
            print("Tahun rilis buku hanya bisa diisi dengan angka")
            print("Silahkan inputkan ulang data buku\n")
            continue