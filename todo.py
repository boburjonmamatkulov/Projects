vazifalar = []

print("=== Vazifalar ro'yxati ===")
print("1 - Vazifa qo'shish")
print("2 - Vazifalarni ko'rish")
print("3 - Vazifa o'chirish")
print("4 - Chiqish")

while True:
    tanlov = input("\nAmalni tanlang (1-4): ")
    
    if tanlov == "1":
        vazifa = input("Vazifa: ")
        vazifalar.append(vazifa)
        print("Qo'shildi!")
    
    elif tanlov == "2":
        if len(vazifalar) == 0:
            print("Vazifalar yo'q!")
        else:
            for i, vazifa in enumerate(vazifalar, 1):
                print(i, "-", vazifa)
    
    elif tanlov == "3":
        if len(vazifalar) == 0:
            print("Vazifalar yo'q!")
        else:
            for i, vazifa in enumerate(vazifalar, 1):
                print(i, "-", vazifa)
            raqam = int(input("Qaysi vazifani o'chirish? ")) - 1
            vazifalar.pop(raqam)
            print("O'chirildi!")
    
    elif tanlov == "4":
        print("Xayr!")
        break