###
# EXERCICIS (while)
###
"""
# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
i = 10
while i > 0:
    print(f"{i}")
    i -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
suma = 0
i = 0
while i < 21:
    if i % 2 == 0:
        suma += i
    i += 1
print(f"{suma}")


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Introdueix un nombre enter positiu: "))
i = 1
r = 1
while i <= numero:
    r *= i
    i += 1
print(f"El resultat es {r}.")


# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = input("Introdueix la contrasenya: ")
while len(contrasenya) < 8:
    print("Ha de tenir almenys 8 caracters")
    contrasenya = input("Introdueix la contrasenya: ")
else:
    print("Contrasenya valida")

    
# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero = int(input("Introdueix numero: "))
i = 0
producte = 0
while i <= 10:
    producte = i*numero
    print(f"Per {i} = {producte}")
    i += 1
else:
    print("Final")

#-----------------------------------------
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
nom = int(input("Introdueix un numero enter positiu: "))
i = 2
while i <= nom:
    j = 2
    es_primer = True
    while j < i:
        if i % j == 0:
            es_primer = False
            break
        j += 1
    if es_primer:
        print(i)
    i += 1




#-----------------------------------------
# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
num = int(input("Introdueix un numero enter: "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Introdueix un numero enter: "))
print(f"El resultat final es {suma}")



# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
numero = int(input("Introdueix un numero enter positiu: "))
comptador = 0
while numero > 0:
    numero //= 10
    print(f"{numero}")
    comptador += 1
print(f"El nombre de xifres es {comptador}")

"""
# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

n = int(input("Quants nombres de la freqüencia de fibonacci vols veure: "))
i = 1
e = 1
anterior = e
r = 0
while i <= n:

    e += anterior
    anterior = e
    print(f"Nombre {i}, {e}")
    i += 1

"""

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num = int(input("Introdueix el nombre: "))
while num != 7:
    if num < 7:
        print("El nombre es mes gran")
    elif num > 7:
        print("El nombre es mes petit")
    num = int(input("Introdueix el nombre: "))
else:
    print("L'has endevinat!")

"""