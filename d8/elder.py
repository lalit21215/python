ram = int(input("Enter age of Ram: "))
mohan = int(input("Enter age of Mohan: "))
sham = int(input("Enter age of Sham: "))
if ram > mohan:
    if ram > sham:
        print("Ram is eldest")
    else:
        print("Sham is eldest")
else:
    if mohan > sham:
        print("Mohan is eldest")
    else:
        print("Sham is eldest")
