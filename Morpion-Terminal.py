grille = ['|1|', '|2|', '|3|', '|4|', '|5|', '|6|', '|7|', '|8|', '|9|']
joueurX = 0 
joueurO = 0 
gagner = 0

# Dictionary for language translations
translations = {
    'fr': {
        'turn_x': '\nAu tour du joueur X !\nDans quelle case voulez vous jouer ?\n',
        'turn_o': '\nAu tour du joueur O !\nDans quelle case voulez vous jouer ?\n',
        'case_used': 'Case déjà utilisée !!!!!',
        'win_x': "Le joueur X à gagné !",
        'win_o': "Le joueur O à gagné !",
        'draw': "Match nul !",
        'select_language': "Choisissez votre langue: \n1. Français\n2. Anglais\n3. Allemand\n"
    },
    'en': {
        'turn_x': '\nIt\'s player X\'s turn!\nWhich box do you want to play in?\n',
        'turn_o': '\nIt\'s player O\'s turn!\nWhich box do you want to play in?\n',
        'case_used': 'Box already used !!!!!',
        'win_x': "Player X has won!",
        'win_o': "Player O has won!",
        'draw': "Draw match!",
        'select_language': "Select your language: \n1. French\n2. English\n3. German\n"
    },
    'de': {
        'turn_x': '\nEs ist Spieler X\'s Zug!\nIn welchem Feld möchtest du spielen?\n',
        'turn_o': '\nEs ist Spieler O\'s Zug!\nIn welchem Feld möchtest du spielen?\n',
        'case_used': 'Feld bereits benutzt !!!!!',
        'win_x': "Spieler X hat gewonnen!",
        'win_o': "Spieler O hat gewonnen!",
        'draw': "Unentschieden!",
        'select_language': "Wählen Sie Ihre Sprache: \n1. Französisch\n2. Englisch\n3. Deutsch\n"
    }
}

def select_language():
    print(translations['en']['select_language'])  # Display language options
    choice = int(input())
    if choice == 1:
        return 'fr'  # French
    elif choice == 2:
        return 'en'  # English
    elif choice == 3:
        return 'de'  # German
    else:
        print("Invalid choice, defaulting to English.")
        return 'en'

selected_language = select_language()

def affichage():
    print('\n')
    print('%s  %s  %s\n' % (grille[0], grille[1], grille[2])) 
    print('%s  %s  %s\n' % (grille[3], grille[4], grille[5])) 
    print('%s  %s  %s\n' % (grille[6], grille[7], grille[8])) 

def vérifier():
    global gagner

    for i in range(3):
        if grille[3*i] == " X " and grille[3*i+1] == " X " and grille[3*i+2] == " X ":
            gagner = "X"
            print(translations[selected_language]['win_x'])
            return
        elif grille[3*i] == " O " and grille[3*i+1] == " O " and grille[3*i+2] == " O ":
            gagner = "O"
            print(translations[selected_language]['win_o'])
            return
        if grille[i] == " X " and grille[i+3] == " X " and grille[i+6] == " X ":
            gagner = "X"
            print(translations[selected_language]['win_x'])
            return
        elif grille[i] == " O " and grille[i+3] == " O " and grille[i+6] == " O ":
            gagner = "O"
            print(translations[selected_language]['win_o'])
            return
    
    if grille[0] == " X " and grille[4] == " X " and grille[8] == " X ":
        gagner = "X"
        print(translations[selected_language]['win_x'])
        return
    elif grille[0] == " O " and grille[4] == " O " and grille[8] == " O ":
        gagner = "O"
        print(translations[selected_language]['win_o'])
        return
    if grille[2] == " X " and grille[4] == " X " and grille[6] == " X ":
        gagner = "X"
        print(translations[selected_language]['win_x'])
        return
    elif grille[2] == " O " and grille[4] == " O " and grille[6] == " O ":
        gagner = "O"
        print(translations[selected_language]['win_o'])
        return

    if "|1|" not in grille and "|2|" not in grille and "|3|" not in grille and "|4|" not in grille and "|5|" not in grille and "|6|" not in grille and "|7|" not in grille and "|8|" not in grille and "|9|" not in grille and " X " in grille and " O " in grille:
        print(translations[selected_language]['draw'])
        quit()

def TourJoueurX():
    while gagner == 0: 
        vérifier()
        affichage()  
        if gagner in ["O", "X"]:
            break
        print(translations[selected_language]['turn_x'])
        joueurX = int(input())
        if grille[joueurX-1] not in [" X ", " O "]: 
            grille[joueurX-1] = ' X ' 
            TourJoueurO()
        else: 
            print(translations[selected_language]['case_used'])
            TourJoueurX()

def TourJoueurO(): 
    while gagner == 0: 
        vérifier()
        affichage()  
        if gagner in ["O", "X"]:
            break
        print(translations[selected_language]['turn_o'])
        joueurO = int(input())
        if grille[joueurO-1] not in [" X ", " O "]: 
            grille[joueurO-1] = ' O ' 
            TourJoueurX()
        else: 
            print(translations[selected_language]['case_used'])
            TourJoueurO()

for i in range(9): 
    while gagner == 0: 
        TourJoueurX()
