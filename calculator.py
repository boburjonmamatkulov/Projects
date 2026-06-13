print("Kalkulyator")
print("1 - Qo'shish")
print("2 - Ayirish")
print("3 - Ko'paytirish")
print("4 - Bo'lish")

tanlov = input("Amalni tanlang (1-4): ")
a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
if tanlov == "1":
    print("Natija:", a + b)
elif tanlov == "2":
    print("Natija:", a - b)
elif tanlov == "3":
    print("Natija:", a * b)
elif tanlov == "4":
    print("Natija:", a / b)
else:
    print("Noto'g'ri tanlov!")