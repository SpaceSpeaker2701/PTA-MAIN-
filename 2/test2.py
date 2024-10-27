# class Cat: # lớp(class)
#     #  name = ""
#     # # age =  ""
#     # # weight = ""
#     # # type = ""
#     # # color = ""
#     # # condition = ""
#     # # sex = ""

# Animal1 = Cat() # đối tượng(object)
# Animal2 = Cat()
# Cat.name = "Pikachu"
# Cat.age = 4
# Cat.color = "Orange"

# class Xe:
#     def __init__(self, name, age, weight, sex, type, color):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.sex = sex
#         self.type = type
#         self.color = color

# Animal1 = Xe()
# print(Animal1.name == "Tom")

class People:
    def __init__(self, ten, tuoi, dan_toc, ton_giao, can_nang, chieu_cao, vung_mien):
        self.ten = ten
        self.tuoi = tuoi
        self.dan_toc = dan_toc
        self.ton_giao = ton_giao 
        self.can_nang = can_nang
        self.chieu_cao = chieu_cao
        self.vung_mien = vung_mien

European = People("Daniel", 20, "Tây", "Jesus", 100, 123, "America")
Asian = People("Hoàng", 14, "Kinh", "Phật", 72, 165, "Việt Nam" )
print("Tên",European.ten)

    