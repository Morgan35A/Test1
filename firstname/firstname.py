def greet_user(name=None):
    firstname = name if name else input('Veuillez entrer votre prénom : ')
    print(type(firstname))
    # vérifier si le prénom saisi n'est pas vide
    if firstname:
        print(f"Merci {firstname} !")

    else:
        print("Vous n'avez pas saisi un prénom valide")

    
        
greet_user()
