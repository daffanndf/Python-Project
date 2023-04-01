from .IndexRead import read_result
from .IndexDatabase import DATABASE_NAME
import os

def delete_start(**kwargs) :
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


def delete_process(no_book) :
    try :
        with open(DATABASE_NAME, "r") as file :
            counter = 1

            while True :
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == no_book :
                    pass
                else :
                    with open("Backup.txt", "a", encoding="UTF-8") as backup_file :
                        backup_file.write(content)
                counter += 1
    except :
        print("Terjadi error pada saat menghapus data buku")

    os.replace("Backup.txt", DATABASE_NAME)


def delete_result() :
    read_result()

    while True : 
        print("\nMasukan nomor buku yang ingin di delete")
        no_book = int(input("Nomor buku : "))
        data_buku = delete_start(index = no_book)

        if data_buku :
            data_break = data_buku.split(",")
            key = data_break[0]
            date = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            print(f"\n=========================")
            print("Data buku yang akan di delete")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun}\n")

            is_done = input("Apakah anda yakin akan menghapus data buku ini? (y/n) : ")
            print(f"=========================")
            if is_done == "y" or is_done == "Y" :
                delete_process(no_book)
                break
        else :
            print("Nomor yang anda masukan tidak tersedia, silahkan input ulang")
    
    print("Data berhasil di delete\n")
    read_result()