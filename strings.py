ville = "Tizi Ouzou"
text = 'Ma ville est {} \n et mon école est "{}"'
print(text.format(ville, "2int"))
# Ici je vais expliquer les casts
x = "3"
print(x + "1")
print(float(x) + 1)  # affche 4 en tant que nombre
# 431
print(str(int(x) + 1))  # affiche 4 en tant que caractère
print(str(int(x) + 1) + x + "1")

f = float(x) + 0.5
print(f)  # ceci est un float
print(str(f) + " °C")
