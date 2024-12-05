while True:  # Boucle infinie
    num1 = float(input("Entrer le premier nombre : "))
    num2 = float(input("Entrer le deuxième nombre : "))
    operation = input("Entrer l'opération (+, -, *, /, **) : ")

    if operation == "+":
        print(f"Résultat : {num1 + num2}")
    elif operation == "-":
        print(f"Résultat : {num1 - num2}")
    elif operation == "*":
        print(f"Résultat : {num1 * num2}")
    elif operation == "**":
        print(f"Résultat : {num1 ** num2}")
    elif operation == "/":
        if num2 == 0:
            print("Erreur : Division par 0 impossible !")
        else:
            print(f"Résultat : {num1 / num2}")
    else:
        print("Opération invalide, essayez encore !")