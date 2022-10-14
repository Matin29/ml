class Bank:
    def __init__(self, ad, soyad, id_number, maash):
        if ad != "" and soyad != "" and maash > 0 and len(str(id_number)) == 8:
            self.ad=ad
            self.soyad=soyad
            self.id_number=id_number
            self.maash=maash
        elif ad == "":
            self.ad = input("Adivizi sehf yazmisiz")
        elif soyad == "":
            self.soyad = input("Soyadi sehf yazmisiz")
        elif maash == 0:
            self.maash = int(input("maashi sehf yazmisiz"))
        elif len(str(id_number)) != 8:
            self.id_number = int(input("shexsiyyet nomrevizi sehf yazibsiz "))

    def credi_advice(self):
        while True:
            credi_percent = self.maash * 0.45
            if (self.maash > 300):
                year_month = int(input("3,6,12,18,24,36\n"
                                       "Neche aylig istiyirsiz kredit\n"
                                       "Bizim bank 13% ile kredit verir"))
                # wanted_credit = int(input("istediyiniz meblig"))
                kredi_for_you=int(credi_percent * year_month)
                with_percent=int(kredi_for_you+(kredi_for_you*0.13))
                aylig_odenishi=int(with_percent/year_month)
                print("size bugeder credit vere bileriy",with_percent,"aylig odenishi iyle",aylig_odenishi)
            elif(self.maash<300):
                print("bizim bank size kredit verenmir")


ad = input("Adivizi yazin")
soyad = input("Soyadivizi yazin")
id_number = int(input("shexsiyyet nomrevizi yazin"))
maash = int(input("maashivizi yazin"))

P1 = Bank(ad, soyad, id_number, maash)
P1.credi_advice()
