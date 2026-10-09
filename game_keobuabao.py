from random import randint

user = input("Nhap keo, bua hoac bao: ")
may = randint(0, 2)

if may == 0:
    may = "bua"
elif may == 1:
    may = "keo"
else:
    may = "bao"

print("Máy chọn:", may)

if user == "keo" and may == "bao":
    print("Máy thua")
elif user == "keo" and may == "keo":
    print("Hòa")
elif user == "keo" and may == "bua":
    print("Máy thắng")
elif user == "bao" and may == "bao":
    print("Hòa")
elif user == "bao" and may == "keo":
    print("Máy thắng")
elif user == "bao" and may == "bua":
    print("Người thắng")
elif user == "bua" and may == "bao":
    print("Máy thắng")
elif user == "bua" and may == "keo":
    print("Máy thua")
else:
    print("Hòa")