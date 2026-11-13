###
# EXERCICIS
###

# Exercici 1: El missatge secret
# Donada la llista següent:
missatge = ["C", "o", "d", "i", " ", "s", "e", "c", "r", "e", "t"]
# Fent servir slicing i concatenació, crea una llista nova que contingui només
# el missatge "secret".
missatge_canviat = missatge[5:]
print(f"{missatge_canviat}")

# Exercici 2: Intercanvi de posicions
# Donada la llista següent:
nombres = [10, 20, 30, 40, 50]
# Intercanvia la primera i l'última posició fent servir només l'assignació per índex.
canvi = nombres[0]
nombres[0] = nombres[4]
nombres[4] = canvi
print(f"{nombres}")

# Exercici 3: L'entrepà de llistes
# Donades les llistes següents:
pa_de_dalt = ["pa de dalt"]
ingredients = ["pernil", "formatge", "tomàquet"]
pa_de_sota = ["pa de sota"]
# Crea una llista anomenada entrepa que contingui, en aquest ordre, el pa de dalt,
# els ingredients i el pa de sota.
entrepa = pa_de_dalt
entrepa += ingredients
entrepa += pa_de_sota
print(f"{entrepa}")
# Exercici 4: Duplicar una llista
# Donada una llista:
# llista = [1, 2, 3]
# Crea una llista nova que contingui duplicats els elements de la llista original.
# Exemple: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Exercici 5: Extreure l'element central
# Donada una llista amb un nombre senar d'elements, extreu-ne l'element central
# fent servir slicing.
llista = [10, 20, 30, 40, 50] 
index = int(len(llista)/2)
element_central = llista[index]
print(f"{element_central}")

# Exercici 6: Inversió parcial
# Donada una llista, inverteix-ne només la primera meitat (fent servir slicing
# i concatenació).
llista = [1, 2, 3, 4, 5, 6] 
meitat = int(len(llista)/2)
meitat_girada = llista[:meitat]
meitat_girada = meitat_girada[::-1]
segona_meitat = llista[meitat:]
llista_final = meitat_girada + segona_meitat
print(f"{meitat_girada}")
print(f"{segona_meitat}")
print(f"{llista_final}")
