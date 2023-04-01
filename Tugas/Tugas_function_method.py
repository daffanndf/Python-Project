class Kontak :
   def __init__(self, input_name, input_telephone, date_add) :
      self.name = input_name
      self.telephone = input_telephone
      self.date = date_add
   
   def adding() :
      nama = input("Masukan nama  : ")
      nomor = input("Masukan nomor : ")
      data_kontak = Kontak(nama, nomor, date_add())
      
      print("\nData kontak yang ingin ditambahkan")
      print(f"Nama  : {data_kontak.name}")
      print(f"Nomor : {data_kontak.telephone}")
      user_option = input("\nLanjutkan ? (Y/N) : ")
      while True :
         if user_option == "Y" or user_option == "y" :
            kontak_add(data_kontak)
            break
         else :
            print("Kontak gagal ditambahkan")
            continue
     
if __name__ == "__main__" :
   while True :
      print("KONTAK TELEPON")
      print("==============")
      print("\n1. Daftar Kontak")
      print("2. Cari Kontak")
      print("3. Tambah Kontak")
      print("4. Hapus Kontak")
      print("0. Keluar Program")
      
      user_option = input("\nMasukan pilihan : ")
      if user_option == "1" :
        
      elif user_option == "2" :
        
      elif user_option == "3" :
         Kontak.adding()
          
      elif user_option == "4" :
        
      elif user_option == "0" :
        
      else :
        
print("Anda telah keluar dari program")
