###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
senyal = float(input("Introdueix el nivell de senyal: "))
if senyal >= -50:
    print("La cobertura es excel·lent")
elif senyal >= -67:
    print("La cobertura es bona")
elif senyal >= -75:
    print("La cobertura es feble")
else:
    print("La cobertura es molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Introdueix la potencia òptica: "))
if potencia <= -27:
    print("Nivell massa baix")
elif potencia >= -8:
    print("Nivell massa alt")
else:
    print("Nivell acceptable")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix consum de dades en GB: "))
if consum <= 20:
    print("Consum a dins del limit")
else:
    adicionals = consum - 20
    print(f"Has superat el limit, has utilitzat {adicionals} GB adicionals")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = str(input("Introdueix indicador LOS (si/no): "))
internet = str(input("Introdueix l'indicador d'Internet (si/no): "))
if los == "si" and internet == "si":
    print("Tot funciona correctament")
elif los == "si" and internet == "no":
    print("Comprovar servei del proveïdor")
elif los == "no" and internet == "si":
    print("Comprovar cable de fibra")
else:
    print("Revisar cable de fibra i servei del proveïdor")


# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
nivell = float(input("Introdueix nivell de bateria: "))

if nivell < 0 or nivell > 100:
    print("Valor fora del rang")
elif nivell < 20:
    print("Nivell critic")
elif nivell < 49:
    print("Nivell baix")
else:
    print("Nivell suficient")
