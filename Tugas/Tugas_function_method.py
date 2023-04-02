import time

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
            
   def removing(input_nomor) :
      os.system("cls")
      for i in range(len(daftar_kontak)) :
         if input_nomor == daftar_kontak[i].__dict__["telephone"] :
            print("Data Kontak")
            print("===========")
            print(f"Nama                : {daftar_kontak[i].__dict__['name']}")
            print(f"Nomor               : {daftar_kontak[i].__dict__['telephone']}")
            print(f"Tanggal ditambahkan : {daftar_kontak[i].__dict__['date']}")

            print("\nAnda yakin ingin menghapus kontak ini?")
            user_option = input("Lanjutkan ? (Y/N) : ")
            if user_option == "Y" or user_option == "y" :
               kontak_remove(daftar_kontak[i])
               continue
            else :
               print("Kontak gagal dihapus")
               break

               
def date_add() :
   tanggal = time.strftime("%d/%m/%Y")
   return tanggal

def kontak_add(kontak_baru) :
   daftar_kontak.append(kontak_baru)

def kontak_remove(kontak_hapus) :
   daftar_kontak.remove(kontak_hapus)

daftar_kontak = []
     
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
         nomor = input("Masukan nomor telepon : ")
         Kontak.removing(nomor)
         
      elif user_option == "0" :
        
      else :
        
print("Anda telah keluar dari program")
