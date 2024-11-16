import math


class Exercices:
    def exercice1(self):
        nom = input("Veuillez saisir votre nom : ")
        print(f"Bonjour {nom} ! Bienvenue.")

    def exercice2(self):
        a = float(input("Veuillez saisir le premier nombre : "))
        b = float(input("Veuillez saisir le deuxième nombre : "))
        somme = a + b
        print(f"La somme de {a} et {b} est : {somme}")

    def exercice3(self):
        a = float(input("Veuillez saisir le premier nombre : "))
        b = float(input("Veuillez saisir le deuxième nombre : "))
        maximum = max(a, b)
        print(f"Le maximum entre {a} et {b} est : {maximum}")

    def exercice4(self):
        for i in range(1, 101):
            print(i)

    def exercice5(self):
        nombre = int(input("Veuillez saisir un nombre entier : "))
        if nombre % 2 == 0:
            print(f"{nombre} est pair.")
        else:
            print(f"{nombre} est impair.")
    
    def exercice6(self):
        age = int(input("Veuillez saisir votre âge : "))
        if age >= 18:
            print("Vous êtes majeur !")
        else:
            print("Vous êtes mineur !")

    def exercice7(self):
        x = float(input("Veuillez saisir le premier nombre : "))
        y = float(input("Veuillez saisir le deuxième nombre : "))
        z = float(input("Veuillez saisir le troisième nombre : "))
        maximum = max(x, y, z)
        print(f"Le maximum est : {maximum}")

    def exercice8(self):
        n = int(input("Veuillez saisir un nombre entier : "))
        somme = sum(range(1, n+1))
        print(f"La somme de 1 à {n} est : {somme}")

    def exercice9(self):
        n = int(input("Veuillez saisir un nombre entier : "))
        factorielle = 1
        for i in range(1, n+1):
            factorielle *= i
        print(f"La factorielle de {n} est : {factorielle}")

    def exercice10(self):
        rayon = float(input("Veuillez saisir le rayon du cercle : "))
        surface = math.pi * rayon**2
        perimetre = 2 * math.pi * rayon
        print(f"La surface du cercle est : {surface:.2f}")
        print(f"Le périmètre du cercle est : {perimetre:.2f}")

    def exercice11(self):
        nombre = int(input("Veuillez saisir un nombre entier : "))
        diviseurs = []
        for i in range(1, nombre + 1):
            if nombre % i == 0:
                diviseurs.append(i)
        print(f"Les diviseurs de {nombre} sont : {diviseurs}")

    def exercice12(self):
        nombre = int(input("Veuillez saisir un nombre entier : "))
        print(f"Table de multiplication de {nombre} :")
        for i in range(1, 11):
            print(f"{nombre} x {i} = {nombre * i}")

    def exercice12(self):
        
        for nombre in range(1, 10):
            print(f"Table de multiplication de {nombre} :")
            for i in range(1, 11):
                print(f"{nombre} x {i} = {nombre * i}")

    def exercice13(self):
        a = int(input("Veuillez saisir le premier nombre : "))
        b = int(input("Veuillez saisir le deuxième nombre (non nul) : "))
        quotient = a // b
        reste = a % b
        print(f"Le quotient de {a} divisé par {b} est : {quotient}")
        print(f"Le reste de la division est : {reste}")

    def exercice14(self):
        nombre = int(input("Veuillez saisir un nombre entier : "))
        racine = int(math.sqrt(nombre))
        if racine * racine == nombre:
            print(f"{nombre} est un carré parfait.")
        else:
            print(f"{nombre} n'est pas un carré parfait.")

    def exercice15(self):
        nombre = int(input("Veuillez saisir un nombre entier supérieur à 1 : "))
        if nombre <= 1:
            print("Veuillez saisir un nombre entier supérieur à 1.")
            return
        for i in range(2, int(math.sqrt(nombre)) + 1):
            if nombre % i == 0:
                print(f"{nombre} n'est pas un nombre premier.")
                return
        print(f"{nombre} est un nombre premier.")

    def exercice16(chaine):
        for caractere in chaine:
            print(caractere)

    def exercice17(chaine):

        compteur = {}
        for caractere in chaine:
            if caractere in compteur:
                compteur[caractere] += 1
            else:
                compteur[caractere] = 1

        for caractere, occurences in compteur.items():
            print(f"Le caractère '{caractere}' figure {occurences} fois dans la chaîne.")

    def exercice18(chaine, lettre):

        positions = []
        for i in range(len(chaine)):
            if chaine[i] == lettre:
                positions.append(i+1)  
        return positions

        chaine = input("Saisissez une chaîne : ")
        lettre = input("Saisissez la lettre à chercher : ")
        positions = trouver_positions_lettre(chaine, lettre)

        if positions:
            for position in positions:
                print(f"La lettre '{lettre}' se trouve à la position : {position}")
        else:
            print(f"La lettre '{lettre}' n'a pas été trouvée.")

    def exercice19():
        liste_chaines = ["laptop", "iphone", "tablet"]

        for chaine in liste_chaines:
            print(f"La chaîne '{chaine}' a une longueur de {len(chaine)} caractères.")
    

    def exercice20(chaine):
        if len(chaine) < 2:
             return chaine
        else:
            return chaine[-1] + chaine[1:-1] + chaine[0]

    def exercice21(chaine):
        voyelles = "aeiouyAEIOUY"
        compteur = 0
        for caractere in chaine:
            if caractere in voyelles:
                compteur += 1
        return compteur
    
    def exercice22(texte):
        mots = texte.split()
        return mots[0] if mots else None

    def exercice23(nom_fichier):
        index_point = nom_fichier.rfind('.')
        if index_point != -1:
            return nom_fichier[index_point:]
        else:
            return None

        nom_fichier = input("Entrez le nom du fichier : ")
        extension = extraire_extension(nom_fichier)

        if extension:
            print(f"L'extension du fichier est {extension}")
        else:
            print("Le fichier n'a pas d'extension.")

    def exercice24(mot):
        mot = mot.lower()  
        return mot == mot[::-1]  

  
