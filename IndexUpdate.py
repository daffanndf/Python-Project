from .IndexRead import read_result
from .IndexDatabase import DATABASE_NAME, TEMPLATE

def update_start(**kwargs) :
    try :
        with open(DATABASE_NAME, "r") as file :
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs :
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku >= jumlah_buku :
                    return False
                else :
                    return content[index_buku]

    except :
        return False


def update_process(no_book, key, date, judul, penulis, tahun) :
    data_template = dict.fromkeys(TEMPLATE)
    data_template["kb"] = key
    data_template["date"] = date
    data_template["judul"] = judul
    data_template["penulis"] = penulis
    data_template["tahun"] = tahun

    update_database = f'{data_template["kb"]:<6},{data_template["date"]:<10},{data_template["judul"]:<80},{data_template["penulis"]:<80},{data_template["tahun"]:<4}\n'
    panjang_data = 186

    with open(DATABASE_NAME, "r+", encoding="UTF-8") as file :
        file.seek(panjang_data * (no_book - 1))
        file.write(update_database)


def update_result() :
    read_result()

    while True : 
        print("\nMasukan nomor buku yang ingin di update")
        no_book = int(input("Nomor buku : "))
        data_buku = update_start(index = no_book)

        if data_buku :
            break
        else :
            print("Nomor yang anda masukan tidak tersedia, silahkan input ulang")
    
    data_break = data_buku.split(",")
    key = data_break[0]
    date = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while True :
        print(f"\n=========================")
        print("Masukan nomor data yang ingin diupdate")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun}\n")
        no_data = input("Nomor data : ")
        print(f"=========================")

        match no_data :
            case "1" : judul = input("Masukan judul baru : ")
            case "2" : penulis = input("Masukan penulis baru : ")
            case "3" :
                while True :
                    try :
                        tahun = int(input("Masukan tahun rilis baru : "))
                        if len(str(tahun)) == 4 :
                            break
                        else :
                            print("Jumlah angka yang bisa diinput pada tahun adalah 4 angka")
                            print("Silahkan inputkan ulang data buku\n")
                            continue
                    
                    except :
                        print("Tahun rilis buku hanya bisa diisi dengan angka")
                        print("Silahkan inputkan ulang data buku\n")
                        continue
            case _ : print("Data yang diinputkan tidak diketahui, silahkan input ulang data")
        
        print(f"\n=========================")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun}\n")
        
        is_done = input("Apakah sudah selesai? (y/n) : ")
        if is_done == "y" or is_done == "Y" :
            break
    
    update_process(no_book, key, date, judul, penulis, tahun)
    print("\nData buku berhasil di update\n")
    read_result()
