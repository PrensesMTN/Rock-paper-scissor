
bilgisayar_hamlesi = "makas"
kullanici_hamlesi =input("""
        tas, kagit, makas;
        hamlenizi giriniz: 
                               """)

print(f"""
      Bilgisayar hamlesi = {bilgisayar_hamlesi}
      Kullanıcı Hamlesi = {kullanici_hamlesi}""")

if bilgisayar_hamlesi == kullanici_hamlesi :
    print("Berabere!!!")

if bilgisayar_hamlesi == "makas":
    if kullanici_hamlesi == "kağıt":
        print("Kullanıcı kesildi")
    if kullanici_hamlesi == "tas":
        print("bilgisayar kırıldı")

if bilgisayar_hamlesi== "tas": 
    if kullanici_hamlesi == "kagıt":
        print("bilgisayar buruştu")

