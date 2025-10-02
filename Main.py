def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")



# Exercice 1 :

def exercice2():
    print("Hello World")

# Exercice 2 :

def exercice3() :
    name = input("Quel est ton prénom ?")
    print("Bonjour", name)

# Exercice 3 :

def exerccie4() :
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
    number = int(input("Veuillez entrer un premier nombre : "))
    print(number ** 2)

# Exercice 10

def exercice11():
    number = int(input("Veuillez entrer un premier nombre : "))
    print("Le double de", number ,"est",number * 2)

# Exercice 11

def exercice12():
    number = int(input("Veuillez entrer un premier nombre : "))
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
    long = int(input("Veuillez entrer un premier nombre : "))
    print("Périmètre =", long * 4)

# Exercice 15 :

def exercice16():
    long = int(input("Veuillez entrer un premier nombre : "))
    print("Périmètre =", long * 4)

# Exercice 16 :

def exercice17():
    long = int(input("Veuillez entrer un premier nombre : "))
    print("Aire =", long ** 2)

def main():
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exerccie4()
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
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()