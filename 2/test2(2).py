class VatNuoi:
    def __init__(self, giong, mau_sac, tuoi, can_nang):
        self.giong = giong
        self.mau_sac = mau_sac
        self.tuoi = tuoi
        self.can_nang = can_nang

pet1 = VatNuoi()
print(pet1.giong == "Chihuahua")
print(pet1.mau_sac == "Red")
print(pet1.tuoi == 12)
print(pet1.can_nang == 5)
