full_name = input("Nhập họ và tên")
print("Họ và tên:",full_name)

age = int(input("Nhập tuổi:"))
print("Tuổi:", age)

height = float(input("Nhập chiều cao:"))
print("Chiều cao:", height)

num = int(input("Nhập vào số bất kì:"))
if num // 2 == 0:
    print("Số", num, "là số chẵn.")
else:
    print("Số", num, "là số lẻ.")

a = float(input("Nhập chiều cao của bạn a:"))
b = float(input("Nhập chiều cao của bạn b:"))
c = float(input("Nhập chiều cao của bạn c:"))
if a > b > c :
    print("Bạn cao nhất là a")
elif c > b > a:
    print("Bạn cao nhất là c")
else:
    print("Bạn cao nhất là b")

total = 0 
for num in range(1,6):
    total += num 
if total > 10:
    print("Tổng lớn hơn 10")
else:
    print("Tổng nhỏ hơn hoặc bằng 10")

a = int(input("Nhập số nguyên dương a:"))
b = int(input("Nhập số nguyên dương b:"))
while b != 0:
    a , b = b, a % b
print(" UCLN của a và b là", a,b)

arr = ["dog", "cat", "mouse"]
for i in range(len(arr)):
    print(arr[i])
