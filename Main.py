from random import randint

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

# Exercice 28
   
def exercice29():
    temp = int(input("Veuillez entrer la température de  l'eau : "))
    if temp > 100 :
        print(temp,"°C → Vapeur")
    elif 0 >= temp >= 100 :
        print(temp,"°C → Liquide")
    elif temp < 0 :
        print(temp,"°C → Glace")

# Exercice 29
   
def exercice30():
    note = int(input("Veuillez entrer votre note : "))
    if note >= 17 :
        print(note,"→ Très bien")
    elif 13 >= note >= 10 :
        print(note,"→ Passable")
    elif 16 >= note >= 14:
        print(note,"→ Bien")
    elif 10 > note :
        print(note,"→ Recalé")

# Exercice 30 :

def exercice31():
    number = int(input("Veuillez entrer le nombre : "))
    for i in range(1,number+1) :
        print(i)

# Exercice 31 :

def exercice32():
    number = int(input("Veuillez entrer le nombre : "))
    for _ in range(1,number+1) :
        print(number)
        number -= 1

# Exercice 32 :

def exercice33():
    resultat = 0
    number = int(input("Veuillez entrer le nombre : "))
    for i in range(1,number+1) :
        resultat += i
        print(resultat)
    
# Exercice 33 :

def exercice34():
    number = int(input("Veuillez entrer le nombre : "))
    for i in range(1,11) :
        print(number,"x",i,"=",number * i)

# Exercice 34 :

def exercice35():
    number = int(input("Veuillez entrer le nombre : "))
    for i in range(1,number+1) :
        if i % 2 == 0 :
            print(i)

# Exercice 35 :

def exercice36():
    number = int(input("Veuillez entrer le nombre : "))
    carre_parfait = 1
    for i in range(1,number+1) :
        carre_parfait = i ** 2
        if carre_parfait < number :
            print(carre_parfait)


# Exercice 36 :

def exercice37():
    message = input("Veuillez entrer votre message : ")
    number = int(input("Veuillez entrer le nombre : "))
    for i in range(1,number + 1) :
        print(message)

# Exercice 37 :

def exercice38():
    taille = int(input("chiffre"))
    resultat = taille - (taille - 1)
    wi = taille - resultat
    for i in range(0, taille):
        print(" "*wi, "*"*resultat, " "*wi)
        wi -= 1
        resultat += 2


# Exercice 38 :

def exercice39():
    number1 = int(input("Veuillez entrer le premier nombre : "))
    number2 = int(input("Veuillez entrer le deuxième nombre : "))
    op = input("Veuillez rentrer votre opérateur pour votre opération : ")
    if op == "+":
        print(number1 + number2)
    elif op == "-":
        print(number1 - number2)
    elif op == "*" or op == "x":
        print(number1 * number2)
    elif op == "/":
        print(number1 / number2)

# Exercice 39 :

def exercice40():
    secret = randint(0, 100)
    message = input("Selon vous le nombre secret est pair ou impair ? ")
    if secret % 2 == 0 and message == "pair" :
        print("Gagné !")
    elif secret % 2 != 0 and message == "impair" :
        print("Gagné !")
    else :
        print("Perdu !")

#  Exercice 40 :

def exercice41():
    mdp = input("Veuillez inscrire votre mot de passe : ")
    if len(mdp) <= 6 :
        print(mdp,"→ Trop court")
    else :
        print(mdp,"→ Valide")

# Exercice 41 :

def exercice42():
    notes =[]
    n = int(input("Veuillez entrer le nombre de note que vous voulez calculer : "))
    somme =0
    for i in range (0,n):
        note = int(input("Veuillez entrer vos notes : "))
        notes.append(note)
    for j in range (0, len(notes)):
        somme = somme + notes[j]
    moyenne = somme / n
    print("Moyenne =",moyenne)

# Exercice 42

def exercice43():
    nombres =[]
    n = int(input("Veuillez entrer le nombre de nombre dans votre liste : "))
    min = 0
    max = 0
    for i in range (0,n):
        nombre = int(input("Veuillez entrer vos nombres : "))
        nombres.append(nombre)
        min =nombres[0]
        if nombres[i] > max :
            max = nombres[i]
        elif nombres[i] < min :
            min = nombres[i]
    print("Min =",min,"Max =",max)

# Exercice 43

def exercice44():
    compteur = 0
    mot = input("Donner nous un mot : ")
    voyelle =["a","e","i","o","u","y"]
    for letter in mot :
        for i in voyelle :
            if letter == i :
                compteur += 1
    print(compteur)

# Exercice 44 :

def exercice45():
    mot = input("Donner nous un mot : ")
    result = ""
    for lettre in mot :
        result = lettre + result
    print(result)

# Exercice 45

def exercice46():
    nombres =[]
    n = int(input("Veuillez entrer le nombre de nombre dans votre liste : "))
    somme = 0
    for i in range (0,n):
        nombre = int(input("Veuillez entrer vos nombres : "))
        nombres.append(nombre)
    for j in range (0, len(nombres)):
        somme += nombres[j]
    print(somme)


# Exercice 46

def exercice47():
    nombres =[]
    n = int(input("Veuillez entrer le nombre de nombre dans votre liste : "))
    trouve = int(input("Veuillez entrer le nombre que vous voulez rechercher dans la liste : "))
    for i in range (0,n):
        nombre = int(input("Veuillez entrer vos nombres : "))
        nombres.append(nombre)
    for j in range(0,len(nombres)):
        if nombres[j] == trouve :
            print("Trouvé a l'indice ",j)

# Exercice 47

def exercice48():
    compteur = 0
    tab =[]
    n = int(input("Veuillez entrer le nombre de nombre dans votre liste : "))
    trouve = int(input("Veuillez entrer le nombre que vous voulez rechercher dans la liste : "))
    for i in range (0,n):
        nombre = int(input("Veuillez entrer vos nombres : "))
        tab.append(nombre)
    for j in range(0,len(tab)):
        if tab[j] == trouve :
            compteur += 1
    print(compteur)

# Exercice 48 :

def exercice49() :
    nombre = int(input("Veuillez entrer votre nombre : "))
    diviseur = []
    for i in range (1, nombre+1):
        if nombre % i == 0 :
            diviseur.append(i)
    print(diviseur)

# Exercice 49 : 

def exercice50() :
    nombre = int(input("Veuillez entrer votre nombre : "))
    diviseur = []
    for i in range (2, nombre):
        if nombre % i == 0 :
            diviseur.append(i)
    if len(diviseur) != 0 :
        print(nombre,"→Non premier")
    else:
        print(nombre,"→Premier")

# Exercice 50 :

def exercice51() :
    fibo = int(input("Veuillez entrer votre nombre qui servira de fin a la suite de fibonacci : "))
    a, b = 0, 1
    list = []
    for i in range(0,fibo) :
        list.append(a)
        a, b = b, a + b
    print(list)

#  Exercice 51 :

def exercice52() :
    list = [1]
    n = 3
    for i in range (1, n+1) :
        list2 = list + [1]
        for j in range(len(list) - 1) :
            list2[j+1] = list[j] + list2[j+1]
        list = list2
        print(list)

# Exercice 52 :

def exercice53(grille) :
    somme_cible = 0
    for j in range(3) :
        somme_cible = somme_cible + grille[0][j]

    est_magique = True

    for i in range(3) :
        s = 0
        for j in range(3) :
            s = s + grille[i][j]
        if s != somme_cible:
            est_magique = False

    for j in range(3) :
        s = 0
        for i in range(3) :
            s = s + grille[i][j]
        if s != somme_cible:
            est_magique = False

    s = 0
    for i in range(3) :
        s = s + grille[i][i]
    if s != somme_cible :
        est_magique = False


    s = 0
    for i in range(3) :
        s = s + grille[i][2 - i]
    if s != somme_cible :
        est_magique = False


    if est_magique :
        print("C'est un carré magique.")
    else:
        print("Ce n'est pas un carré magique.")

grille = [
    [1, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

# Exercice 53 :

def exercice54() :
    nombre = int(input("Veuillez entrer le nombre que vous voulez convertir (max 16) : "))
    result = ""
    while nombre > 0 :
        result += str(nombre%2)
        nombre = nombre // 2
    print(result)

# Exercice 54 :

def exercice55() :
    de1 = randint(1,6)
    de2 = randint(1,6)
    print("Total =", de1 + de2)

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
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()
    elif choix == "38":
        exercice38()
    elif choix == "39":
        exercice39()
    elif choix == "40":
        exercice40()
    elif choix == "41":
        exercice41()
    elif choix == "42":
        exercice42()
    elif choix == "43":
        exercice43()
    elif choix == "44":
        exercice44()
    elif choix == "45":
        exercice45()
    elif choix == "46":
        exercice46()
    elif choix == "47" :
        exercice47()
    elif choix == "48":
        exercice48()
    elif choix == "49":
        exercice49()
    elif choix == "50":
        exercice50()
    elif choix == "51":
        exercice51()
    elif choix == "52":
        exercice52()
    elif choix == "53" :
        exercice53(grille)
    elif choix == "54" :
        exercice54()
    elif choix == "55" :
        exercice55()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()