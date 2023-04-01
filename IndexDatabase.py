from . import IndexOperation

DATABASE_NAME = "Database.txt"
TEMPLATE = {
    "kb" : "",
    "date" : "",
    "judul" : "",
    "penulis" : "",
    "tahun" : ""
}

# Function untuk pengecekan database
def init_console() :
    try :
        with open(DATABASE_NAME, "r") as file :
            print("Database tersedia")
    except : 
        with open(DATABASE_NAME, "w", encoding="UTF-8") as file :
            print("Database tidak tersedia, silahkan membuat Database baru")
            JUDUL = input("Judul   : ")
            PENULIS = input("Penulis : ")
            TAHUN = input("Tahun   : ")

            data_template = dict.fromkeys(TEMPLATE)
            data_template["kb"] = IndexOperation.key_book(6)
            data_template["date"] = IndexOperation.date_add()
            data_template["judul"] = JUDUL
            data_template["penulis"] = PENULIS
            data_template["tahun"] = TAHUN

            first_database = f'{data_template["kb"]:<6},{data_template["date"]:<10},{data_template["judul"]:<80},{data_template["penulis"]:<80},{data_template["tahun"]:<4}\n'
            file.write(first_database)