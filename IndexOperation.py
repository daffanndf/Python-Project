import random
import string
import time

# Function untuk key book
def key_book(banyak_angka) :
    key = "".join(random.choice(string.digits) for i in range(banyak_angka))
    return key

# Function untuk tanggal ditambahkan buku
def date_add() :
    date = time.strftime("%d/%m/%Y")
    return date