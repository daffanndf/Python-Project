from .IndexDatabase import DATABASE_NAME

# Function untuk membaca data pada database
def read_data() :
    try :
        with open(DATABASE_NAME, "r") as file :
            content = file.readlines()
            return content
    except :
        return False

# Function untuk menampilkan hasil baca database
def read_result() :
    hasil_read = read_data()
    
    nomor = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("="*102)
    print(f"| {nomor:^4} | {judul:^40} | {penulis:^40} | {tahun:^6}")
    print("="*102)

    # Isi Data
    for index, data in enumerate(hasil_read) :
        hasil_baru = data.split(",")
        
        key = hasil_baru[0]
        date = hasil_baru[1]
        judul = hasil_baru[2]
        penulis = hasil_baru[3]
        tahun = hasil_baru[4]

        print(f"| {index+1:4} | {judul:.40} | {penulis:.40} | {tahun:5}",end="")

    # Footer
    print("="*102)


