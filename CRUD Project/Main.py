import os
import CRUD

if __name__ == "__main__" :
    match os.name :
        case "posix" : os.system("clear")
        case "nt" : os.system("cls")
    
    print(f"SELAMAT DATANG DI PROGRAM")
    print(f"{'DATABASE PERPUSTAKAAN':^25}")
    print(f"=========================")

    # Pengecekan Database
    CRUD.init_console()

    while True :
        match os.name :
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
    
        print(f"SELAMAT DATANG DI PROGRAM")
        print(f"{'DATABASE PERPUSTAKAAN':^25}")
        print(f"=========================")

        print(f"1. Read data")
        print(f"2. Create data")
        print(f"3. Update data")
        print(f"4. Delete  data\n")

        user_input = input("Masukan opsi : ")
        
        print(f"\n=========================\n")

        match user_input :
            case "1" : CRUD.read_result()
            case "2" : CRUD.create_result()
            case "3" : CRUD.update_result()
            case "4" : CRUD.delete_result()
    
        print(f"\n=========================\n")

        is_done = input("Apakah sudah selesai? (y/n) : ")
        if is_done == "y" or is_done == "Y" :
            break

    print(f"Program telah berakhir")
