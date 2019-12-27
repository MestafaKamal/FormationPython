print("\nDébut du programme:")
a = True
while a:
    m = input("Quelle est votre moyenne? ")
    m = float(m)
    if m <= 20 and m >= 0:
        if m < 10:
            print("----> Vous devez refaire.\n")
        else:
            print("----> Félicitation!\n")
            a = False
    else:
        print("Erreur!!")

print("Fin du programme.")
