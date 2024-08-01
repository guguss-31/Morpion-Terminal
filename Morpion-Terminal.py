grille = ['|1|','|2|','|3|','|4|','|5|','|6|','|7|','|8|','|9|']
joueurX = 0 
joueurO = 0 
gagner = 0
def affichage() :
	print('\n')
	print('%s  %s  %s\n' % (grille[0], grille[1], grille[2])) 
	print('%s  %s  %s\n' % (grille[3], grille[4], grille[5])) 
	print('%s  %s  %s\n' % (grille[6], grille[7], grille[8])) 

affichage()

def vérifier() :   
        
    if grille[0] == " X " and grille[1] == " X " and grille[2] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")     
    else : 
        if grille[0] == " O " and grille[1] == " O " and grille[2] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
    
    if grille[3] == " X " and grille[4] == " X " and grille[5] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
    else : 
        if grille[3] == " O " and grille[4] == " O " and grille[5] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
    
    if grille[6] == " X " and grille[7] == " X " and grille[8] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
    else : 
        if grille[6] == " O " and grille[7] == " O " and grille[8] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
    
    if grille[0] == " X " and grille[3] == " X " and grille[6] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
        
    else : 
        if grille[0] == " O " and grille[3] == " O " and grille[6] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
            
    if grille[1] == " X " and grille[4] == " X " and grille[7] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
        
    else : 
        if grille[1] == " O " and grille[4] == " O " and grille[7] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
            
    if grille[2] == " X " and grille[5] == " X " and grille[8] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
        
    else : 
        if grille[2] == " O " and grille[5] == " O " and grille[8] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
            
    if grille[0] == " X " and grille[4] == " X " and grille[8] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
        
    else : 
        if grille[0] == " O " and grille[4] == " O " and grille[8] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
            
    if grille[2] == " X " and grille[4] == " X " and grille[6] == " X " : 
        gagner = "X" 
        print("Le joueur X à gagné !")
        
    else : 
        if grille[2] == " O " and grille[4] == " O " and grille[6] == " O " : 
            gagner = "O" 
            print("Le joueur O à gagné !")
    
    if "|1|" not in grille and "|2|" not in grille and "|3|" not in grille and "|4|" not in grille and "|5|" not in grille and "|6|" not in grille and "|7|" not in grille and "|8|" not in grille and "|9|" not in grille and " X " in grille and " O " in grille : 
        print("Match nul !")
        quit()

def TourJoueurX () :
    while gagner == 0 : 
        vérifier()
        print('\nAu tour du joueur X !\nDans quelle case voulez vous jouer ?\n')
        joueurX = int(input())
        if grille[joueurX-1] != " O " or " X " : 
            grille[joueurX-1] = ' X ' 
            affichage()
            TourJoueurO()
        else : 
            print("Case déjà utilisée !!!!!")
            TourJoueurX()

def TourJoueurO () : 
    while gagner == 0 : 
        vérifier()
        print('\nAu tour du joueur O !\nDans quelle case voulez vous jouer ?\n')
        joueurO = int(input())
        if grille[joueurO-1] != " O " or " X " : 
            grille[joueurO-1] = ' O ' 
            affichage()
            TourJoueurX()
        else : 
            print("Case déjà utilisée !!!!!")
            TourJoueurO()

for i in range(9) : 
    while gagner==0 : 
        TourJoueurX()

