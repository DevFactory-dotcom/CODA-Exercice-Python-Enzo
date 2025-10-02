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
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()