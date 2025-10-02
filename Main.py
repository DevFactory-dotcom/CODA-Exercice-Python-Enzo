def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")



# Exercice 1 :

def exercice2():
    print("Hello World")

# Exercice 2 :

def exercice3() :
    name = input("Quel est votre prénom ?")
    print("Bonjour", name)

# Exercice 3 :

def exercice4() :
    print("Première ligne \nDeuxième ligne \nTroisième ligne")

# Exercice 4 :

def exercice5():
    année = int(input("Votre année de naissance :"))
    print("Vous avez environ", 2025-année, "ans")

# Exercice 5 :

def exercice6():
    number1 = int(input("Veuillez entrer un premier nombre : "))
    number2 = int(input("Veuillez entrer un deuxième nombre : "))
    print(number1, "+" ,number2, "=",number1 + number2)

# Exercice 6 :

def exercice7():
    number1 = int(input("Veuillez entrer un premier nombre : "))
    number2 = int(input("Veuillez entrer un deuxième nombre : "))
    print(number1, "-" ,number2, "=",number1 - number2)

# Exercice 7 :

def exercice8():
    number1 = int(input("Veuillez entrer un premier nombre : "))
    number2 = int(input("Veuillez entrer un deuxième nombre : "))
    print(number1, "-" ,number2, "=", number1 - number2)

# Exercice 8 :

def exercice9():
    number1 = int(input("Veuillez entrer un premier nombre : "))
    number2 = int(input("Veuillez entrer un deuxième nombre : "))
    print(number1, "x" ,number2, "=", number1 * number2)

# Exercice 9 :

def exercice10():
    number1 = int(input("Veuillez entrer un premier nombre : "))
    number2 = int(input("Veuillez entrer un deuxième nombre : "))
    print(number1, "/" ,number2, "=", number1 / number2)

# Exercice 10

def exercice11():
    number = int(input("Veuillez entrer un nombre : "))
    print(number ** 2)

# Exercice 10

def exercice11():
    number = int(input("Veuillez entrer un nombre : "))
    print("Le double de", number ,"est",number * 2)

# Exercice 11

def exercice12():
    number = int(input("Veuillez entrer un nombre : "))
    print("Le moitié de", number ,"est", number / 2)

# Exercice 12

def exercice13():
    message = input("Veuillez entrer votre message : ")
    for i in range(1,6) :
        print(message)

# Exercice 13

def exercice14():
    for i in range(1,6) :
        print(i)

# Exercice 14 :

def exercice15():
    for i in range (1, 6) :
        print("2 x ",i ,"=", 2 * i )

# Exercice 15 :

def exercice16():
    long = int(input("Veuillez entrer la longueur du coté de votre carré : "))
    print("Périmètre =", long * 4)

# Exercice 15 :

def exercice16():
    long = int(input("Veuillez entrer la longueur du coté de votre carré : "))
    print("Périmètre =", long * 4)

# Exercice 16 :

def exercice17():
    long = int(input("Veuillez entrer un nombre : "))
    print("Aire =", long ** 2)

# Exercice 17 :

def exercice18():
    euro = int(input("Veuillez entrer le nombre d'euro que vous voulez convertir : "))
    print(euro,"€ =", euro * 1.1)

# Exercice 18 :

def exercice19():
    minutes = int(input("Veuillez entrer le nombre de minutes que vous voulez convertir : "))
    print(minutes,"minutes =", minutes * 60,"secondes")

# Exercice 19 :

def exercice20():
    HT = int(input("Veuillez entrer le montant hors taxe que vous voulez convertir : "))
    print("Prix TTC =",HT * 1.20)

# Exercice 20 :

def exercice21():
    age = int(input("Veuillez entrer votre âge : "))
    name = input("Veuillez entrer votre prénom : ")
    print(name,"a",age,"ans")

# Exercice 21 :

def exercice22():
    number = int(input("Veuillez entrer un nombre positif ou négatif : "))
    if number >= 0 :
        print(number,"→ Positif")
    elif number < 0 :
        print(number,"→ Négatif")
    elif number == 0 :
        print(number,"→ Nul")
    else :
        print("Ce n'est pas un nombre")
        exercice22()

# Exercice 22 :

def exercice23():
    age = int(input("Veuillez entrer votre age : "))
    if age >= 18 :
        print(age,"→ Majeur")
    elif age < 18 :
        print(age,"→ Mineur")

# Exercice 23 :

def exercice24():
    note = int(input("Veuillez entrer votre note : "))
    if note >= 10 :
        print(note,"→ Validé")
    elif note < 10 :
        print(note,"→ Non validé")

# Exercice 24 :

def exercice25():
    age1 = int(input("Veuillez entrer votre age : "))
    age2 = int(input("Veuillez entrer votre age : "))
    if age1 > age2 :
        print(age1,"est plus grand")
    elif age1 < age2 :
        print(age2,"est plus grand")

# Exercice 25 :

def exercice26():
    number1 = int(input("Veuillez entrer le premier nombre : "))
    number2 = int(input("Veuillez entrer le deuxième nombre : "))
    if number1 > number2 :
        print("Ordre croissant : OUI")
    elif number1 < number2 :
        print("Ordre croissant : NON")

# Exercice 26 :

def exercice27():
    number = int(input("Veuillez entrer le nombre : "))
    if number % 5 == 0  :
        print(number ,"→Divisible par 5")
    elif number % 5 != 0 :
        print(number, "→Non divisible par 5")

# Exercice 27
   
def exercice28():
    age = int(input("Veuillez entrer votre age : "))
    if age >= 18 :
        print(age,"ans → Adulte")
    elif 12 >= age > 18 :
        print(age,"ans → Adolescent")
    elif age < 12 :
        print(age,"ans → Enfant")


def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11" :
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15" :
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18" :
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()